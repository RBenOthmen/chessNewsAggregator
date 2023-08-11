import requests
from bs4 import BeautifulSoup
import csv

# URL of the chess news website you want to scrape
url = "https://fide.com/news"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the news article elements on the page (adjust selectors as needed)
article_elements = soup.find_all("a", class_="first-section-news")

# Initialize a list to store scraped data
scraped_data = []

# Loop through each article element and extract relevant information
for article in article_elements:
    title = article.find("div", class_="one-news").text
    article_url = article["href"]  # You can directly access the href attribute

    scraped_data.append({"title": title, "article_url": article_url})

# Specify the CSV file name
csv_file = "chess_news.csv"

# Save the scraped data to a CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["title", "article_url"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for item in scraped_data:
        writer.writerow(item)

print(f"Scraped data saved to {csv_file}")
