from task4package import movie
from task4package import news
import mysql.connector
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread, Lock
from multiprocessing import Process
import filereadwrite
import time

movie_count = 0
regular_time = 0
multithreaded_time = 0
multiprocessed_time = 0
site_movies_coming_soon = 'http://www.forumcinemas.lt/Movies/ComingSoon/'
movie_result = requests.get(site_movies_coming_soon)
movie_r = movie_result.content
movie_soup = BeautifulSoup(movie_r, "html.parser")
movie_samples = movie_soup.find_all("a", "arrowLink")
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
        image = "None"
        genre = "None"
        is_3d = False
        site_result = requests.get(data[item])
        re = site_result.content
        soup_coming_soon = BeautifulSoup(re, "html.parser")
        information_samples = soup_coming_soon.find_all("div", attrs={'id': "eventInfoBlock"})
        for a in information_samples:
            image = a.img['src']
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
         #   print("////////////////////////TIME:" +           + "//////////////////////////" )
            if "Žanras:" in text and "Sukurta:" in text:
                genre = (text[(text.index("Žanras:") + 1):text.index("Sukurta:")])
                genre = ''.join(genre)
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
            else:
                age = 0
        lock = Lock()
        lock.acquire()
        movie_dict = dict()
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root", database="psa")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM movies WHERE (title=%s AND title_foreign=%s )', (title_lt, title_foreign))
        entry = mycursor.fetchone()
        if entry is None:
            mycursor.execute(
				'INSERT INTO movies (title, title_foreign, age_rating, duration, is_3d, image_url, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (title_lt, title_foreign, age, duration, is_3d, image, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        else:
            pass
        movie_id = mycursor.execute('SELECT id FROM movies WHERE (title=%s AND title_foreign=%s )', (title_lt, title_foreign))
		
        mydb.commit()
        mydb.close()
        lock.release()


# /----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def scrape_additional_movies():

    for item in data_2:
        if ".lt/Event" in data_2[item]:
            title_lt = "None"
            title_foreign = "None"
            age = "None"
            duration = "None"
            director_name = "None"
            image = "None"
            genre = "None"
            is_3d = False
            site_result = requests.get(data_2[item])
            re = site_result.content
            soup_coming_soon = BeautifulSoup(re, "html.parser")
            information_samples = soup_coming_soon.find_all("div", attrs={'id': "eventInfoBlock"})
            for a in information_samples:
                image = a.img['src']
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
                if "Žanras:" in text and "Sukurta:" in text:
                    genre = (text[(text.index("Žanras:") + 1):text.index("Sukurta:")])
                    genre = ''.join(genre)
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
            lock = Lock()
            lock.acquire()
            movie.add_movie(title_lt, title_foreign, director_name, age, duration, is_3d, image, genre)
            lock.release()
            movie_count = movie_count + 1

    print("Total movie count: ", movie_count)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def webscraping_multithreaded():
    global multithreaded_time
    global movie_count
    print("Pradedamas multithreaded webscraper po 5 sekundžių...")
    time.sleep(5)
    start_time = datetime.now()
    print(f'[{start_time}] {"Pradžia!"}')
    Thread(target=scrape_upcoming_movies()).start()
   # Thread(target=scrape_news_and_additional_movies()).start()
    end_time = datetime.now()
    print(f'[{end_time}] {"Pabaiga!"}')
    movie_count = 0

webscraping_multithreaded()


