import requests
from bs4 import BeautifulSoup
import streamlit as st

# Set the URL of the page you want to scrape
url = 'https://www.daraz.pk/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract the titles of the products
product_elements = soup.find_all('div', class_='c2prKC')
product_titles = [product.find('a', class_='c16H9d').text.strip() for product in product_elements]

# Display the titles in Streamlit
for title in product_titles:
    st.write(title)
