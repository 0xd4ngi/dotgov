import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    updates = soup.find_all('div', class_='update-class')  # Example: change as needed
    extracted_data = [update.text for update in updates]
    return extracted_data
