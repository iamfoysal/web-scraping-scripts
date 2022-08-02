import requests
from bs4 import BeautifulSoup

url = 'https://www.goodfirms.co/software/inflow-inventory'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

try:
    url = soup.find("div", class_="entity-detail-header-visit-website")
    print(url.a.get('href'))
except AttributeError:
    url = "Couldn't Find"
    print(url)
