import requests
import csv
from bs4 import BeautifulSoup

# The provided HTML code
url = "https://fide.com/news"

# Create a BeautifulSoup object
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all "one-news" elements
one_news_elements = soup.find_all(class_='one-news')

# Find all "third-section-news__info" elements
third_section_info_elements = soup.find_all(class_='third-section-news__info')

# Extract data and save to a CSV file
with open('chess_news.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Date', 'Image'])

    for one_news in one_news_elements:
        title = one_news.find('p').get_text()
        date = one_news.find(class_='one-news__date').get_text() if one_news.find(class_='one-news__date') else ''
        image_element = one_news.find('img')
        image_url = image_element['src'] if image_element else ''
        csv_writer.writerow([title, date, image_url])

    for third_info in third_section_info_elements:
        title = third_info.find('p').get_text()
        csv_writer.writerow([title, '', ''])

print("Data saved to chess_news.csv")
