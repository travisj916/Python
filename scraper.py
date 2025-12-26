import sys
import urllib.parse

from playwright.sync_api import sync_playwright


def scrape_and_build_response(query: str) -> str:
    cleaned_query = query.strip()
    if not cleaned_query:
        return "Empty query provided. Send a keyword or URL to scrape."

    search_url = "https://duckduckgo.com/?q=" + urllib.parse.quote(cleaned_query)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(search_url, wait_until="domcontentloaded")
        title = page.title()
        browser.close()

    return f"Results for '{cleaned_query}': {search_url} (page title: {title})"


def main() -> None:
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        raise SystemExit("Usage: python scraper.py <query>")
    print(scrape_and_build_response(query))


if __name__ == "__main__":
    main()
