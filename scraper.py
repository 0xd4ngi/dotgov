import requests
from bs4 import BeautifulSoup

def scrape_website(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    updates = soup.find_all('div', class_=class_name)  # Use the provided class name for each website
    extracted_data = [update.text for update in updates]
    return extracted_data

def scrape_multiple_websites(websites):
    all_updates = {}
    for site in websites:
        url = site['url']
        class_name = site['class_name']
        updates = scrape_website(url, class_name)
        all_updates[url] = updates
    return all_updates
