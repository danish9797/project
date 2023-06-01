import requests
from bs4 import BeautifulSoup
import streamlit as st

# Set the URL of the Wikipedia page you want to scrape
url = 'https://en.wikipedia.org/wiki/OpenAI'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract specific elements from the HTML
title_element = soup.find('h1')
summary_element = soup.find('div', attrs={'id': 'mw-content-text'}).find('p')

# Extract the text from the elements
title = title_element.text.strip() if title_element else 'Title not found'
summary = summary_element.text.strip() if summary_element else 'Summary not found'

# Print the extracted data
print('Title:', title)
print('Summary:', summary)
