import requests
from bs4 import BeautifulSoup

# from bs4 import BeautifulSoup

URL = 'https://na.op.gg'
page = requests.get(URL)

print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
# results = soup.find(id='input.summoner-search-form__text')
# print(results.prettify()