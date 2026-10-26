# Python Web Scraping and Data Processing

## Overview

A practical web scraping project demonstrating how to extract, clean, validate, and store structured data from web pages using Python.

## Technologies

* Python
* Requests
* BeautifulSoup
* Selenium
* Pandas
* CSV and Excel

## Features

* Extracts quotes, authors, and tags from a practice website.
* Navigates paginated web pages.
* Uses Selenium for browser automation and JavaScript-rendered content.
* Cleans datasets by handling missing values and duplicate records.
* Exports structured data to CSV and Excel.
* Implements basic checkpointing to support resuming interrupted scraping sessions.
* Demonstrates basic network error handling.

## Project Structure

* `scraper.py` — Requests and BeautifulSoup scraper.
* `clean_data.py` — Dataset cleaning and validation.
* `selenium_scraper.py` — Selenium browser automation.
* `resumable_scraper.py` — Scraper with basic checkpointing.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd data-scraping-portfolio
```

### 2. Create and activate a virtual environment

On Windows:

```bash
py -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requests beautifulsoup4 selenium pandas openpyxl
```

### 4. Run the scripts

```bash
python scraper.py
python clean_data.py
python selenium_scraper.py
python resumable_scraper.py
```

Run `clean_data.py` after generating its required input file with `scraper.py`.

## Data Source

The project uses Quotes to Scrape, a practice website designed for web scraping exercises: https://quotes.toscrape.com/

## Purpose

This project was created for learning and demonstrating practical web scraping and data processing skills.

## Limitations

The checkpointing implementation is a basic demonstration. It does not provide transactional recovery or automatic retry of failed pages.

## Author

Daniel Ochuba
