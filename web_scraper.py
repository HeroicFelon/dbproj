
import os
import asyncio
import requests
from crawl4ai import AsyncWebCrawler

ARTICLES_DIR = "articles"
os.makedirs(ARTICLES_DIR, exist_ok=True)

def to_markdown(title, url, content):
    return f"# {title}\n\n[Original Article]({url})\n\n{content}"

async def fetch_and_save_articles():
    url = input("Enter the URL to scrape: ").strip()
    if not url:
        print("No URL entered. Exiting.")
        return
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)
        # Use the URL as the title if no better title is available
        title = url
        markdown = to_markdown(title, url, result.markdown)
        # Generate a safe filename from the URL
        import hashlib
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
        filename = os.path.join(ARTICLES_DIR, f"scraped_{url_hash}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Saved: {filename}")

        # --- LLM Cleanup and Summarization ---
        ollama_url = "http://localhost:11434/api/generate"
        prompt = (
            "You are an expert research assistant. "
            "Given the following markdown scraped from a website, clean up the content (remove navigation, ads, unrelated text), "
            "and provide a concise summary at the top. Output only clean, readable markdown.\n\n" + markdown
        )
        payload = {
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(ollama_url, json=payload, timeout=120)
            response.raise_for_status()
            llm_result = response.json().get("response", "")
            if llm_result:
                cleaned_filename = os.path.join(ARTICLES_DIR, f"scraped_{url_hash}_llm.md")
                with open(cleaned_filename, "w", encoding="utf-8") as f:
                    f.write(llm_result)
                print(f"LLM-cleaned and summarized markdown saved: {cleaned_filename}")
            else:
                print("LLM did not return any content.")
        except Exception as e:
            print(f"Error communicating with Ollama LLM: {e}")

if __name__ == "__main__":
    asyncio.run(fetch_and_save_articles())