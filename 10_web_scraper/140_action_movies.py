import requests
from bs4 import BeautifulSoup
import pandas as pd

base_site = "https://editorial.rottentomatoes.com/guide/140-essential-action-movies-to-watch-now/"
response = requests.get(base_site)
print(response.status_code)

html = response.content

soup = BeautifulSoup(html, 'lxml')
with open('rotten_tomatoes_page.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

divs = soup.find_all('div', {'class': 'col-sm-18 col-full-xs countdown-item-content'})
headings = [div.find('h2') for div in divs]

movies_names = [heading.find('a').string for heading in headings]
years = [heading.find('span', class_='start-year').string.strip('()') for heading in headings]
scores = [heading.find('span', class_='tMeterScore').string for heading in headings]

critics_divs = soup.find_all('div', {'class': 'info critics-consensus'})
critics = [div.text for div in critics_divs]
repeated = "Critics Consensus: "
critics = [sentence.replace(repeated, '') for sentence in critics]

directors_divs = soup.find_all('div', {'class':'info director'})
directors = [None if director.find('a') is None else director.find('a').string
             for director in directors_divs]

actors_divs = soup.find_all('div', {'class':'info cast'})

actors = []
for actor_div in actors_divs:
    actors.append([actor.text for actor in actor_div.find_all('a')])

movies = pd.DataFrame({'movie_name':movies_names,
                       'release_year':years,
                       'critics':critics,
                       'rating_score':scores,
                       'directors':directors,
                       'actors':actors})
movies.to_csv('action_movies.csv', index=False)
