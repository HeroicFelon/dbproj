## Crawl4AI Documentation (v0.6.x)

**Overview:**

Crawl4AI is an open-source, LLM-friendly web crawler and scraper designed for speed, flexibility, and ease of use. It's built to generate clean Markdown output, making it ideal for RAG pipelines and direct ingestion into large language models. The documentation provides comprehensive guides on setup, usage, and advanced features.

**Key Features:**

*   **Markdown Generation:** Automatically generates clean and structured Markdown output.
*   **Structured Extraction:** Enables parsing of repeated patterns using CSS, XPath, or LLM-based extraction.
*   **Advanced Browser Control:** Offers hooks, proxies, stealth modes, and session reuse for fine-grained control.
*   **High Performance:** Uses parallel crawling and chunk-based extraction.
*   **Open Source:** Free to use, with a vibrant community.
*   **LLM-Friendly:** Minimally processed data to improve LLM consumption.

**Sections:**

1.  **Quick Start:** A hands-on introduction to crawling with Crawl4AI, generating Markdown, and performing simple extraction.
2.  **Setup & Installation:** Instructions for installing Crawl4AI via pip or Docker.
3.  **Core:**
    *   Command Line Interface
    *   Simple Crawling
    *   Deep Crawling
    *   Crawler Result
    *   Browser, Crawler & LLM Config
    *   Markdown Generation
    *   Fit Markdown
    *   Page Interaction
    *   Content Selection
    *   Cache Modes
    *   Local Files & Raw HTML
    *   Link & Media
4.  **Advanced:**
    *   File Downloading
    *   Lazy Loading
    *   Hooks & Auth
    *   Proxy & Security
    *   Session Management
    *   Multi-URL Crawling
    *   Crawl Dispatcher
    *   Identity Based Crawling
    *   SSL Certificate
    *   Network & Console Capture
5.  **Extraction:**
    *   LLM-Free Strategies (CSS, XPath)
    *   LLM Strategies
    *   Clustering Strategies
    *   Chunking
6.  **API Reference:** Details for `AsyncWebCrawler`, `arun()`, `arun_many()`, `CrawlResult`, and `Strategies`.

**Community Support:**

*   **GitHub Repository:** [https://github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
*   **Discord:** Join the community for support and discussions.

**Note:** The old documentation can be accessed [here](https://old.docs.crawl4ai.com).
