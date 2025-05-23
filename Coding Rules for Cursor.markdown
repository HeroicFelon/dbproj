# Coding Rules for Cursor

Below are 10 coding rules for Cursor, designed for a project leveraging a software stack that includes Python with libraries like SpaCy, Scrapy, and PyTorch, alongside Elasticsearch or PostgreSQL for the database, and Flask or Django for the UI. These rules ensure best practices, maintainability, and scalability, with a specific emphasis on modularity to prevent large, unwieldy files.

---

## 1. **Modularity Rule: Directory Structure and File Size Limits**
- **Description**: Organize the codebase into directories based on functionality, with each directory containing files specific to sub-functionalities. No single file should exceed 500 lines of code.
- **Implementation**:
  - `article_collection/`: Split into `web_scraper.py`, `rss_feeds.py`, `academic_journals.py`, `api_interactions.py`, and `scheduler.py`.
  - `database_enhancement/`: Divide into `sentiment_analysis.py`, `ner.py`, `keyword_extraction.py`, `eei_identification.py`, `lead_generation.py`, `research_plan_generation.py`, and `analytics.py`.
  - `ui/`: Adhere to Flask/Django conventions (e.g., `app.py`, `templates/`, `static/`).
- **Purpose**: Enhances readability, maintainability, and debugging by keeping code organized and manageable.

---

## 2. **NLP Best Practices: Efficient Multilingual Model Use**
- **Description**: Leverage SpaCy’s language models for multilingual support, loading the appropriate model based on detected article language and caching it for reuse.
- **Implementation**: Use `langdetect` to identify the language, then load and cache SpaCy models (e.g., `en_core_web_sm` for English) to optimize memory and performance.
- **Purpose**: Ensures efficient NLP processing across multiple languages without redundant overhead.

---

## 3. **Database Design: Schema and Indexing for Performance**
- **Description**: Define a clear schema for articles and metadata, indexing frequently queried fields like publication date, language, and topics.
- **Implementation**:
  - For Elasticsearch, apply language-specific analyzers to text fields.
  - For PostgreSQL, use full-text search indexes and index foreign keys.
- **Purpose**: Optimizes retrieval speed and storage efficiency for large datasets.

---

## 4. **Ethical Data Collection: Respecting Constraints**
- **Description**: Check `robots.txt` before scraping websites, respect API rate limits, and securely store credentials.
- **Implementation**: Use `robotparser` for scraping permissions, implement exponential backoff for APIs, and store keys in environment variables or a secrets manager.
- **Purpose**: Ensures ethical and sustainable data collection practices.

---

## 5. **Robust Error Handling and Logging**
- **Description**: Wrap external interactions (web requests, database queries) in try-except blocks and log errors and events with context.
- **Implementation**: Use Python’s `logging` module to record errors, warnings, and info messages with timestamps and file details.
- **Purpose**: Facilitates debugging and ensures system reliability.

---

## 6. **Comprehensive Testing: Unit Tests and Mocking**
- **Description**: Write unit tests for each module, covering happy paths and error conditions, using mocking for external dependencies.
- **Implementation**: Employ `pytest` and `unittest.mock` to test edge cases like network failures or invalid inputs.
- **Purpose**: Guarantees code reliability and catches issues early.

---

## 7. **Configuration Management: Centralized Settings**
- **Description**: Store settings like source URLs, API keys, and database connections in a `config.yaml` file, loaded at runtime.
- **Implementation**: Use `PyYAML` to parse the file, organizing settings into sections (e.g., `article_collection`, `database`).
- **Purpose**: Simplifies configuration updates without code changes.

---

## 8. **Optimized Performance: Asynchronous and Parallel Processing**
- **Description**: Use asynchronous programming for concurrent article fetching and offload intensive tasks like NLP to separate processes.
- **Implementation**: Utilize `asyncio` with `aiohttp` for fetching and `multiprocessing` or Celery for NLP tasks.
- **Purpose**: Maximizes efficiency on available hardware for large-scale processing.

---

## 9. **Security Measures: Data Protection**
- **Description**: Encrypt sensitive data and use secure coding practices to prevent vulnerabilities like SQL injection or XSS.
- **Implementation**: Enforce HTTPS, sanitize inputs, and use parameterized queries for database operations.
- **Purpose**: Protects the system and its data from threats.

---

## 10. **Detailed Documentation: Docstrings and READMEs**
- **Description**: Include docstrings for all modules and functions, detailing purpose, inputs, outputs, and side effects, plus a project-wide README.
- **Implementation**: Use Google-style docstrings and maintain READMEs in each directory with setup and usage instructions.
- **Purpose**: Improves code understanding and maintainability.

---

These rules are designed to work within Cursor’s Project Rules framework, stored in `.cursor/rules` as MDC files. Below is an example rule file implementing the modularity rule:

```markdown
description: Enforce modularity by organizing code into directories and limiting file size
globs:
  - "**/*.py"
alwaysApply: true

- Organize the codebase into directories: `article_collection/`, `database_enhancement/`, `ui/`.
- Split `article_collection/` into `web_scraper.py`, `rss_feeds.py`, `academic_journals.py`, `api_interactions.py`, `scheduler.py`.
- Split `database_enhancement/` into `sentiment_analysis.py`, `ner.py`, `keyword_extraction.py`, `eei_identification.py`, `lead_generation.py`, `research_plan_generation.py`, `analytics.py`.
- For `ui/`, follow Flask/Django conventions (e.g., `app.py`, `templates/`, `static/`).
- No file should exceed 500 lines of code to maintain readability and manageability.
```

---

These rules ensure a modular, efficient, and maintainable codebase tailored to the specified stack, aligning with Cursor’s best practices for project-specific guidance.