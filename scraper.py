import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://quotes.toscrape.com/"
url = BASE_URL

session = requests.Session()
records = []

while url:
    print(f"Scraping: {url}")

    response = session.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")

    for item in quotes:
        quote_element = item.select_one(".text")
        author_element = item.select_one(".author")

        if not quote_element or not author_element:
            continue

        tags = [
            tag.get_text(strip=True)
            for tag in item.select(".tags .tag")
        ]

        records.append({
            "quote": quote_element.get_text(strip=True),
            "author": author_element.get_text(strip=True),
            "tags": ", ".join(tags)
        })

    next_button = soup.select_one("li.next a")

    if next_button:
        next_page = next_button.get("href")
        url = requests.compat.urljoin(url, next_page)
    else:
        url = None

df = pd.DataFrame(records)

df.to_csv("quotes_raw.csv", index=False)
df.to_excel("quotes_raw.xlsx", index=False)

print(f"\nScraping completed!")
print(f"Total records collected: {len(df)}")
print(df.head())