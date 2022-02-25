from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs

import time

BASE_URL = "https://www.csfd.cz"
UZIVATEL_URL = BASE_URL + "/uzivatel/"

class Rating:
    def __init__(self, name):
        self.name = name
        self.stars = ""
        self.url = ""
        self.date_rated = ""
        self.info = ""

def get_csfd_ratings(user_id, page_num):
    url = UZIVATEL_URL + str(user_id) + "/hodnoceni/" + f"?page={page_num}"
    print(f"Getting {url}")
    # response = requests.get(url, allow_redirects = True)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(response.text, "html.parser")
    table = soup.find_all("div", {"id": "snippet--ratings"})

    if len(table) == 0:
        return []

    rows = table[0].find_all("tr")
    if rows is None:
        return []

    data = []
    for row in rows:
        rating = Rating(row.select_one("a.film-title-name").text)
        rating_class = row.select("span.star-rating span.stars")[0].get('class')[-1]
        rating.stars = "0" if rating_class == 'trash' else rating_class.split("-")[-1]
        rating.url = BASE_URL + row.find("a", {"class": "film-title-name"}).get("href")
        rating.date_rated = row.select_one("td.date-only").text.strip()
        rating.info = row.select_one("span.film-title-info").text
        data.append(rating)

    return data

def get_csfd_ratings_from_url(url):
    print(f"Getting {url}")
    # response = requests.get(url, allow_redirects = True)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(response.text, "html.parser")
    table = soup.find_all("div", {"id": "snippet--ratings"})

    if len(table) == 0:
        return []

    rows = table[0].find_all("tr")
    if rows is None:
        return []

    data = []
    for row in rows:
        rating = Rating(row.select_one("a.film-title-name").text)
        rating_class = row.select("span.star-rating span.stars")[0].get('class')[-1]
        rating.stars = "0" if rating_class == 'trash' else rating_class.split("-")[-1]
        rating.url = BASE_URL + row.find("a", {"class": "film-title-name"}).get("href")
        rating.date_rated = row.select_one("td.date-only").text.strip()
        rating.info = row.select_one("span.film-title-info").text
        data.append(rating)

    return data


def get_csfd_max_page(user_id):
    url = UZIVATEL_URL + str(user_id) + "/hodnoceni/"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(response.text, "html.parser")
    pagination = soup.find_all("div", {"class": "pagination"})
    if len(pagination) == 0:
        return 1

    pagination = pagination[0]
    pages = pagination.find_all("a")
    page_numbers = [int(page.text) for page in pages if page.text.isdigit()]

    if len(page_numbers) == 0:
        return 1

    max_page = page_numbers[-1]
    return max_page