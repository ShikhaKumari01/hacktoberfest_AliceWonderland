import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://example.com'  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract the title of the webpage
    title = soup.title.string
    print(f"Title: {title}")

    # Example: Extract all the links on the webpage
    links = [link.get('href') for link in soup.find_all('a')]
    print("Links:")
    for link in links:
        print(link)

    # You can continue to extract other information as needed

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
