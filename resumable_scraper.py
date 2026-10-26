
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
import time

BASE_URL = "https://quotes.toscrape.com"
DATA_FILE = Path("resumable_quotes.csv")
PROGRESS_FILE = Path("last_page.txt")

session = requests.Session()
session.headers.update({
    "User-Agent": "EducationalScraper/1.0"
})

# Load previously saved records
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE)
    records = df.to_dict("records")
else:
    records = []

# Load the last successfully completed page
if PROGRESS_FILE.exists():
    with open(PROGRESS_FILE, "r") as file:
        last_page = int(file.read().strip())
else:
    last_page = 0

page_number = last_page + 1

while True:
    url = f"{BASE_URL}/page/{page_number}/"

    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".quote")

        # An empty page signals the end of the dataset
        if not quotes:
            print("No more quotes found.")
            break

        page_records = []

        for quote in quotes:
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [
                tag.get_text(strip=True)
                for tag in quote.select(".tag")
            ]

            page_records.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags),
                "page": page_number
            })

        # Save the current page's data
        records.extend(page_records)

        df = pd.DataFrame(records)
        df = df.drop_duplicates(subset=["quote", "author"])
        df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

        # Update progress only after saving the data
        with open(PROGRESS_FILE, "w") as file:
            file.write(str(page_number))

        print(
            f"Page {page_number} saved. "
            f"Total unique quotes: {len(df)}"
        )

        page_number += 1
        time.sleep(1)

    except requests.RequestException as error:
        print(f"Page {page_number} failed: {error}")
        print("Progress saved. Fix the issue and rerun the script.")
        break

print("Scraping session finished.")
