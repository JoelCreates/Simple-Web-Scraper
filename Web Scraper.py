import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://innovatewithjoel.online'
response = requests.get(url)
print('Status code:', response.status_code)  # Check the response status code

# Print the webpage content for inspection
print(response.content)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the latest five articles
articles = soup.find_all('article')[:5]
print('Number of articles found:', len(articles))  # Check the number of articles found

# Scrape the title and URL of each article
for article in articles:
    title = article.find('h2').text.strip()
    url = article.find('a')['href']
    print('Title:', title)
    print('URL:', url)
    print()
