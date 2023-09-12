from bs4 import BeautifulSoup
import requests

from scraper import Scraper

class Prime(Scraper):
    
    url = "https://www.prime.jo/Browsing/Movies/NowShowing"

    titles = []
    title_links = []
    showings = {}

    def __init__(self):
        pass

    def fetch_data(self):
        self.get_titles()

    def get_titles(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')

        article = soup.find('article', attrs={'id':'movies-list'})
        title_wrappers = article.find_all('div',class_='title-wrapper')

        titles=[]
        title_links=[]
        for wrapper in title_wrappers:
            link = wrapper.find('a')['href']
            title = wrapper.find('h3').text
            titles.append(title.strip())
            title_links.append({'title':title.strip(),'link':link})
        self.title_links = title_links
        self.titles=titles
        return titles
    
    def get_title_showings(self):

        showings = {}

        for title in self.title_links:

            title_url = title['link']
            if title_url[:2] == '//':
                title_url = "https:" + title_url

            r = requests.get(title_url)

            soup = BeautifulSoup(r.content, 'lxml')

            locations = soup.find_all('div', class_='film-item')
            title_showings = {}

            for location in locations:
                theater = location.find('h3', class_="film-title").text
                sessions = location.find_all('time')
                sessions = [i['datetime'] for i in sessions]
                title_showings[theater] = sessions
            
            showings[title['title']] = title_showings
            
        self.showings = showings
        return showings
    

if __name__ == '__main__':
    from pprint import pprint
    from model.title import Title
    # p = Prime()
    # prime_titles = p.get_titles()
    # prime_showings = p.get_title_showings()
    # print(p.titles)

    # Title.bulk_insert([Title(title=name) for name in p.titles])
    # print(Title.all_from_where_clause(""))
    # print(prime_titles)
    # pprint(prime_showings)

    response = requests.get("https://www.prime.jo/Browsing/Movies/NowShowing")
    soup = BeautifulSoup(response.content, 'lxml')

    movies = soup.find('article', attrs={'id':'movies-list'})
    movies_list = movies.find_all('div',class_='title-wrapper')

    print(movies)

