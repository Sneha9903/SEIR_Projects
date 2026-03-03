# Python Web Page Reader

## Description
This program takes a URL from the command line, fetches the webpage, and prints:

1. The page title (without HTML tags)
2. The page body text (only visible text, no HTML tags)
3. All URLs (links) that the page points to

## Libraries Used
- sys (to read command-line arguments)
- requests (to send HTTP request)
- BeautifulSoup from bs4 (to parse HTML)

## How to Run

python3 scraper.py http://example.com

Replace the URL with any valid website.
