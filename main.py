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
title_element = soup.find('h1').text.strip()

summary_element = ''
p_elements = soup.find_all('p')
for p in p_elements:
    if p.text.strip():
        summary_element = p.text.strip()
        break

# Display the extracted data in Streamlit
st.write('Title:', title_element)
st.write('Summary:', summary_element)
