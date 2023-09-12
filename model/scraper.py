from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, **kwargs):
        raise NotImplementedError
    
    def fetch_data(self):
        pass

    def get_titles(self):
        pass

    def get_title_showings(self, title):
        pass

    def get_title_imdb_score(self, title):
        pass

    def get_title_rotten_tomatoes_score(self, title):
        pass

    def get_title_trailer_url(self, title):
        pass

    def get_title_image_url(self, title):
        pass

    def get_title_age_rating(self, title):
        pass

    def get_title_description(self, title):
        pass

    # 1. Create a batch
    # 2. Run scraper for all theaters
    # 3. Save scraped data to DB
    # 3a. Titles - Unique (also make sure to handle for arabic titles)
    # 3b. Showings - 
