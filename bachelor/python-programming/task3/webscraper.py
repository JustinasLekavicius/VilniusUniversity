from task3package import movie
from task3package import news
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from multiprocessing import Process
import filereadwrite
import time

movie_count = 0
news_count = 0
regular_time = 0
multithreaded_time = 0
multiprocessed_time = 0
site_movies_coming_soon = 'http://www.forumcinemas.lt/Movies/ComingSoon/'
site_news = 'http://www.forumcinemas.lt/news/kinonaujienos/'
news_result = requests.get(site_news)
movie_result = requests.get(site_movies_coming_soon)
news_r = news_result.content
movie_r = movie_result.content
movie_soup = BeautifulSoup(movie_r, "html.parser")
news_soup = BeautifulSoup(news_r, "html.parser")
movie_samples = movie_soup.find_all("a", "arrowLink")
news_samples = news_soup.find_all("a", "arrowLink")
data = {}
data_2 = {}


def scrape_upcoming_movies():
    global movie_count
    for a in movie_samples:
        if not a.string is None:
            if 'href' in a.attrs.keys():
                data[a] = a.attrs['href']
    for item in data:
        title_lt = "None"
        title_foreign = "None"
        age = "None"
        duration = "None"
        director_name = "None"
        is_3d = False
        site_result = requests.get(data[item])
        re = site_result.content
        soup_coming_soon = BeautifulSoup(re, "html.parser")
        information_samples = soup_coming_soon.find_all("div", attrs={'id': "eventInfoBlock"})
        for a in information_samples:
            text = a.text.strip()
            text = text.split("\n")
            text = [w.replace('\r', '') for w in text]
            for item in text:
                text[text.index(item)] = text[text.index(item)].lstrip()
            text = list(filter(None, text))
            title_lt = text[0]
            title_foreign = text[1]
            title_foreign = title_foreign.lstrip()
            duration = text[text.index("Trukmė: ") + 1] + " " + text[text.index("Trukmė: ") + 2] + " " + text[
                text.index("Trukmė: ") + 3]
            if "Režisierius:" in text and "Vaidina:" in text:
                director_name = (text[(text.index("Režisierius:") + 1):text.index("Vaidina:")])
                director_name = ''.join(director_name)
            if "Režisierius:" in text and "Vaidina:" not in text:
                director_name = text[(text.index("Režisierius:") + 1)]
            if "3D" in title_lt or "3D" in title_foreign:
                is_3d = True
            age = text[text.index("Cenzas: ") + 1]
            if age == "Įvairaus amžiaus žiūrovams":
                age = 0
            if age == "N-7. Jaunesniems būtina suaugusiojo palyda":
                age = 7
            if age == "N-13. 7-12 m. vaikams būtina suaugusiojo palyda":
                age = 13
            if age == "Žiūrovams nuo 16 metų":
                age = 16
            if age == "Suaugusiems nuo 18 metų":
                age = 18

        movie.add_movie(title_lt, title_foreign, director_name, age, duration, is_3d)
        movie_count = movie_count + 1


# /----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def scrape_news_and_additional_movies():
    global movie_count, news_count
    for b in news_samples:
        if not b.string is None:
            if 'href' in b.attrs.keys():
                data_2[b] = b.attrs['href']

    for item in data_2:
        if ".lt/Event" in data_2[item]:
            title_lt = "None"
            title_foreign = "None"
            age = "None"
            duration = "None"
            director_name = "None"
            is_3d = False
            site_result = requests.get(data_2[item])
            re = site_result.content
            soup_coming_soon = BeautifulSoup(re, "html.parser")
            information_samples = soup_coming_soon.find_all("div", attrs={'id': "eventInfoBlock"})
            for a in information_samples:
                text = a.text.strip()
                text = text.split("\n")
                text = [w.replace('\r', '') for w in text]
                for item in text:
                    text[text.index(item)] = text[text.index(item)].lstrip()
                text = list(filter(None, text))
                title_lt = text[0]
                title_foreign = text[1]
                title_foreign = title_foreign.lstrip()
                duration = text[text.index("Trukmė: ") + 1] + " " + text[text.index("Trukmė: ") + 2] + " " + text[
                    text.index("Trukmė: ") + 3]
                if "Režisierius:" in text and "Vaidina:" in text:
                    director_name = (text[(text.index("Režisierius:") + 1):text.index("Vaidina:")])
                    director_name = ''.join(director_name)
                if "Režisierius:" in text and "Vaidina:" not in text:
                    director_name = text[(text.index("Režisierius:") + 1)]
                if "3D" in title_lt or "3D" in title_foreign:
                    is_3d = True
                age = text[text.index("Cenzas: ") + 1]
                if age == "Įvairaus amžiaus žiūrovams":
                    age = 0
                if age == "N-7. Jaunesniems būtina suaugusiojo palyda":
                    age = 7
                if age == "N-13. 7-12 m. vaikams būtina suaugusiojo palyda":
                    age = 13
                if age == "Žiūrovams nuo 16 metų":
                    age = 16
                if age == "Suaugusiems nuo 18 metų":
                    age = 18

            movie.add_movie(title_lt, title_foreign, director_name, age, duration, is_3d)
            movie_count = movie_count + 1
        elif ".lt/News" in data_2[item]:
            link = data_2[item]
            site_result = requests.get(data_2[item])
            re = site_result.content
            soup_coming_soon = BeautifulSoup(re, "html.parser")
            information_samples = soup_coming_soon.find_all("div", attrs={'class': "contboxBasic"})
            text = information_samples[0].text.strip()
            text = text.split("\n")
            text = [w.replace('\r', '') for w in text]
            for item in text:
                text[text.index(item)] = text[text.index(item)].lstrip()
            text = list(filter(None, text))
            title = text[1]
            description = text[3]
            news.add_news(title, description, link)
            news_count = news_count + 1

    print("Total movie count: ", movie_count)
    print("Total news count: ", news_count)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def webscraping_regular():
    global regular_time
    global movie_count
    global news_count
    print("Starting regular web scraper in 5 seconds...")
    time.sleep(5)
    start_time = datetime.now()
    print(f'[{start_time}] {"Starting!"}')
    scrape_upcoming_movies()
    scrape_news_and_additional_movies()
    end_time = datetime.now()
    print(f'[{datetime.now()}] {"Regular web scraping ending!"}')
    regular_time = end_time - start_time
    movie_count = 0
    news_count = 0


def webscraping_multithreaded():
    global multithreaded_time
    global movie_count
    global news_count
    print("Starting multithreaded web scraper in 5 seconds...")
    time.sleep(5)
    start_time = datetime.now()
    print(f'[{start_time}] {"Starting!"}')
    Thread(target=scrape_upcoming_movies()).start()
    Thread(target=scrape_news_and_additional_movies()).start()
    end_time = datetime.now()
    print(f'[{end_time}] {"Multithreading web scraping ending!"}')
    multithreaded_time = end_time - start_time
    movie_count = 0
    news_count = 0


def webscraping_multiprocessed():
    global multiprocessed_time
    print("Starting multiprocessed web scraper in 5 seconds...")
    time.sleep(5)
    start_time = datetime.now()
    print(f'[{start_time}] {"Starting!"}')
    Process(target=scrape_upcoming_movies()).start()
    Process(target=scrape_news_and_additional_movies()).start()
    end_time = datetime.now()
    print(f'[{end_time}] {"Multiprocessing web scraping ending!"}')
    multiprocessed_time = end_time - start_time

print("Welcome! Would you like to start the regular, multithreaded or multiprocessed version of the web scraper, or all of them?")
mode = input("Please input regular, multithreaded, multiprocessed or all:   ")
if mode == "regular":
    webscraping_regular()
    print("Regular scraping completed in: ", regular_time)
if mode == "multithreaded":
    webscraping_multithreaded()
    print("Multithreaded scraping completed in: ", multithreaded_time)
if mode == "multiprocessed":
    webscraping_multiprocessed()
    print("Multiprocessed scraping completed in: ", multiprocessed_time)
if mode == "all":
    webscraping_regular()
    filereadwrite.File.file_delete("movies")
    filereadwrite.File.file_delete("news")
    webscraping_multithreaded()
    filereadwrite.File.file_delete("movies")
    filereadwrite.File.file_delete("news")
    webscraping_multiprocessed()
    print("Regular scraping completed in: ", regular_time)
    print("Multithreaded scraping completed in: ", multithreaded_time)
    print("Multiprocessed scraping completed in: ", multiprocessed_time)

