## linkedin https://www.linkedin.com/posts/noor-fatima-2501b240a_task-8-difficulty-level-high-python-activity-7492207903622340608-a2Bp?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGhS9dwBbGp1DjhFPZGT0Q7ib3ko4pit5Yk

# Web Scraper

A simple Python web scraping project that extracts structured data from a website using **Requests** and **BeautifulSoup**. The scraped data is stored in both **CSV** and **JSON** formats for easy use and analysis.

## Objective

The objective of this project is to demonstrate how to:

* Send HTTP requests to a website
* Parse HTML using BeautifulSoup
* Extract useful information from web pages
* Organize scraped data into a structured format
* Save the extracted data as CSV and JSON files

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* CSV
* JSON

## Features

* Scrapes quotes from a practice website
* Extracts:

  * Quote text
  * Author name
  * Tags
* Stores the extracted information in `quotes.csv`
* Stores the extracted information in `quotes.json`
* Handles unsuccessful website requests
* Displays the number of successfully scraped records

## Website Used

The project uses **Quotes to Scrape**, a website specifically designed for practicing web scraping.

Website:

https://quotes.toscrape.com/

## Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the scraper with:

```bash
python scraper.py
```

The program will connect to the website, extract the available quotes, and save the results.

Example output:

```text
Starting web scraper...
Successfully scraped 10 quotes.
Saved data to:
- quotes.csv
- quotes.json
```

## Output

### CSV

The `quotes.csv` file contains structured data like:

```text
quote,author,tags
"The world as we have created it is a process of our thinking...",Albert Einstein,change deep-thoughts thinking
"It is our choices, Harry, that show what we truly are...",J.K. Rowling,abilities choices
```

### JSON

The `quotes.json` file stores the same information in JSON format:

```json
[
    {
        "quote": "The world as we have created it is a process of our thinking...",
        "author": "Albert Einstein",
        "tags": "change deep-thoughts thinking"
    }
]
```

## Error Handling

The scraper checks whether the website request was successful. If the website cannot be accessed, an error message is displayed instead of attempting to process invalid data.

## Learning Outcomes

Through this project, I learned how to:

* Work with HTTP requests in Python
* Use BeautifulSoup to navigate HTML
* Select and extract elements from a webpage
* Convert scraped information into structured data
* Write data to CSV and JSON files
* Handle basic errors during web scraping

## Conclusion

This project demonstrates the basic process of web scraping with Python. It takes information from a webpage, extracts the required fields, and stores the results in reusable structured formats such as CSV and JSON.
