from bs4 import BeautifulSoup
import requests
from csv import writer 

url_obj = "https://www.imdb.com/chart/top/"
page = requests.get(url_obj)

#print (page)

soup = BeautifulSoup(page.content, 'html.parser')

#print (soup)

lists = soup.find('tbody', class_="lister-list").find_all('tr')
#print (len(lists))


with open('top_movie.csv', 'w', encoding='utf8', newline='') as f:
    callwriter = writer(f)
    header = ['Rank & Title', 'Publish Date','Rating']
    callwriter.writerow(header)

    for list in lists:
        Movie_name = list.find('td', class_="titleColumn").a.text
        publish = list.find('span', class_="secondaryInfo").text.strip('()')
        rating = list.find('td', class_="imdbRating").text.replace('\n', '')
        
        movie_info = [Movie_name, publish,rating]
        #print(movie_info)
        callwriter.writerow(movie_info)

