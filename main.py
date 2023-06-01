import requests
from bs4 import BeautifulSoup
import streamlit as st

# Set the URL of the page you want to scrape
url = 'https://www.daraz.pk/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract specific elements from the HTML
product_elements = soup.find_all('div', class_='c2prKC')

# Create a Streamlit table to display the scraped data
table_data = []
for product in product_elements:
    name = product.find('a', class_='c16H9d').text.strip()
    price = product.find('div', class_='c3gUW0').text.strip()
    rating = product.find('div', class_='c15YQ9').text.strip()

    table_data.append([name, price, rating])

st.table(table_data)
