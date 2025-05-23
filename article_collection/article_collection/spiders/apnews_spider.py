import scrapy # type: ignore
import os

class ApnewsSpider(scrapy.Spider):
    name = "apnews"
    allowed_domains = ["apnews.com"]
    start_urls = ["https://apnews.com/hub/technology"]

    def parse(self, response):
        # Select article links on the technology hub page
        for article in response.css('a[data-key="card-headline"]::attr(href)').getall():
            url = response.urljoin(article)
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        url = response.url

        # Save to articles/ directory
        os.makedirs("articles", exist_ok=True)
        safe_title = "".join(x for x in title if x.isalnum() or x in " _-").strip() if title else "untitled"
        filename = f"articles/{safe_title[:50]}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"<!-- Title: {title}\nURL: {url} -->\n")
            f.write(response.text)

        self.log(f"Saved article HTML: {filename}")