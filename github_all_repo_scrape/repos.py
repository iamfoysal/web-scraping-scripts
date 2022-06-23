from bs4 import BeautifulSoup
import requests
from csv import writer 

url_obj = "https://github.com/iamfoysal?tab=repositories"
page = requests.get(url_obj)
#print (page)

soup = BeautifulSoup(page.content, 'html.parser')
#print (soup)
lists = soup.find_all('h3', class_="wb-break-all")
#print (lists)


with open('mohiful_repositories.csv', 'w', encoding='utf8', newline='') as f:
    callwriter = writer(f)
    header = ['name', 'address'] # csv header name 
    callwriter.writerow(header)

    for link in lists:
        a_tag=link.find('a')
        name = a_tag.string.text.replace('\n', '') # refo name 
        address_collect = a_tag.get('href')
        address = ('https://github.com' + address_collect ) # Github url + repo url
        infos = [name, address]
        #print(info)
        callwriter.writerow(infos)

    