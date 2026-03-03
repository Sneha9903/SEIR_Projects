import sys
import requests
from bs4 import BeautifulSoup

# check if URL is given
if len(sys.argv) < 2:
    print("Please provide a URL")
    sys.exit()
url = sys.argv[1]

# get page
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}
response = requests.get(url, headers=headers)

# make soup object
soup = BeautifulSoup(response.text, "html.parser")

# print title
if soup.title:
    print(soup.title.text)
else:
    print("No title found")

# remove script and style tags
for tag in soup.find_all(["script", "style"]):
    tag.extract()

# print body text (no HTML tags)
text = soup.get_text()
print(text.strip())

# print all links
links = soup.find_all("a")

for link in links:
    if link.get("href") is not None:
        print(link.get("href"))

