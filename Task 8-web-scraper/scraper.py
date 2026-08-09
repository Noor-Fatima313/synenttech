import requests
from bs4 import BeautifulSoup
import csv
import json


URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    response = requests.get(URL, timeout=10)

    if response.status_code != 200:
        print("Failed to access the website.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.select(".tags .tag")
        ]

        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    return quotes_data


def save_to_csv(data, filename="quotes.csv"):
    if not data:
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["quote", "author", "tags"]
        )

        writer.writeheader()
        writer.writerows(data)


def save_to_json(data, filename="quotes.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    print("Starting web scraper...")

    data = scrape_quotes()

    if data:
        save_to_csv(data)
        save_to_json(data)

        print(f"Successfully scraped {len(data)} quotes.")
        print("Saved data to:")
        print("- quotes.csv")
        print("- quotes.json")
    else:
        print("No data was scraped.")


if __name__ == "__main__":
    main()