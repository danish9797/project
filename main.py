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
title = soup.find('h1', class_='firstHeading').text.strip()
summary = soup.find('div', class_='mw-parser-output').p.text.strip()

# Print the extracted data
print('Title:', title)
print('Summary:', summary)
