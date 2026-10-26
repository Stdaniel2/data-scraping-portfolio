
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

records = []

try:
    driver.get("https://quotes.toscrape.com/js/")

    while True:
        # Wait until the quotes appear on the page
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "quote")
            )
        )

        # Extract quotes and authors
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text

            records.append({
                "quote": text,
                "author": author
            })

        print(f"Collected {len(records)} quotes so far.")

        # Find the Next button
        try:
            next_button = driver.find_element(
                By.CSS_SELECTOR, "li.next a"
            )
            next_button.click()

        except NoSuchElementException:
            print("No more pages.")
            break

    # Save results
    df = pd.DataFrame(records)
    df = df.drop_duplicates(subset=["quote", "author"])

    df.to_csv(
        "selenium_quotes_all.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\nScraping completed!")
    print("Total unique quotes:", len(df))
    print("Saved to selenium_quotes_all.csv")

finally:
    driver.quit()