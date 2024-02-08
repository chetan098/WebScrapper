# WebScraper.py
# Created by Chetan Pujari

import requests
from bs4 import BeautifulSoup

print("Created by chetan pujari");
def scrape(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            endpoints = []
            for link in soup.find_all('a'):
                links.append(link.get('href'))
            for form in soup.find_all('form'):
                endpoints.append(form.get('action'))
            return links, endpoints
        else:
            print("Error: Unable to fetch URL")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

if __name__ == "__main__":
    url = input("Enter the URL: ")
    found_links, found_endpoints = scrape(url)
    if found_links and found_endpoints:
        print("Hidden URLs found:")
        for link in found_links:
            print(link)
        print("\nEndpoints found:")
        for endpoint in found_endpoints:
            print(endpoint)
    else:
        print("No hidden URLs or endpoints found.")
