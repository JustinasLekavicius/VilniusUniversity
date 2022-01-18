import json
import datetime
import os
import re
import sys
# Movie may have a title, a director, an age rating, a duration. It may also be in 3D.
class Movie:

    def __init__(self, title, director, age_rating, duration, is_3d):
        self.title = title
        self.director = director
        self.age_rating = age_rating
        self.duration = duration
        self.is_3d = is_3d

    # Get the title of the movie.
    def movie_name(self):
        return self.title

    # Get the director of the movie.
    def movie_director(self):
        return self.director

    # Get the age-rating of the movie.
    def movie_age_rating(self):
        return self.age_rating

    # Get the duration of the movie.
    def movie_duration(self):
        return self.duration

    # Get the 3D status of the movie.

    def movie_is_3d(self):
        return self.is_3d
    # Get all the attributes of the movie.

    def __str__(self):
        return "Movie title: ", self.title, " director: ", self.director, ", age rating: ",  self.age_rating, "duration in minutes: ", self.duration, ", the movie is in 3D: ", self.is_3d

    # Every movie, along with its attributes, is printed.
    def output_movies(self):
        with open('movies.json', encoding=('UTF-8')) as f:
            movie_dict = dict()
            if os.stat('movies.json').st_size == 0:
                print("movies.json file is empty!")
                exit(0)
            movies = json.load(f)
        for movie in movies:
            title = movies[movie]["title"]
            director = movies[movie]["director"]
            age_rating = movies[movie]["age_rating"]
            duration = movies[movie]["duration"]
            is_3d = movies[movie]["is_3d"]
            m = Movie(title, director, age_rating, duration, is_3d)
            movie_dict[movie] = vars(m)
            with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                json.dump(movie_dict, outfile, ensure_ascii=False)
            print(vars(m), "\n")

# News may have a title, a description and a date.
class News:

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date


    # Get the title of the news.
    def news_name(self):
        return self.title

    # Get the description of the news.
    def news_description(self):
        return self.description

    # Get the date of the news.
    def news_date(self):
        return self.date

    # Get all the attributes of the news.

    def __str__(self):
        return "News title: ", self.title, ", news description: ", self.description, ", news date: ",  self.date

    # All the news are printed
    def output_news(self):
        with open('news.json', encoding=('UTF-8')) as f:
            news_dict = dict()
            if os.stat('news.json').st_size == 0:
                print("news.json file is empty!")
                exit(0)
            news = json.load(f)
        for new in news:
            title = news[new]["title"]
            description = news[new]["description"]
            date = news[new]["date"]
            n = News(title, description, date)
            news_dict[new] = vars(n)
            with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                json.dump(news_dict, outfile, ensure_ascii=False)
            print(vars(n), "\n")

# Ticket may have a movie title, price, seat number, row number, date, movie beginning time and movie ending time.
class Ticket:
    def __init__(self, title, price, seat_number, row_number, date, movie_start_time, movie_end_time):
        self.title = title
        self.price = price
        self.seat_number = seat_number
        self.row_number = row_number
        self.date = date
        self.movie_start_time = movie_start_time
        self.movie_end_time = movie_end_time

    # Get the title of the movie which the ticket is bought for.

    def ticket_name(self):
        return self.title

     # Get the price of the ticket.

    def ticket_price(self):
        return self.price

    # Get the seat number of the ticket.

    def ticket_seat_number(self):
        return self.seat_number()

    # Get the date of the ticket.

    def ticket_date(self):
        return self.date

    # Get the movie beginning time.

    def ticket_movie_start_time(self):
        return self.movie_start_time

    # Get the movie ending time.

    def ticket_movie_end_time(self):
        return self.movie_end_time

    # Get all the attributes of the ticket.

    def __str__(self):
        return "Ticket movie name: ", self.title, ", ticket price: ", self.price, ", seat number: ",  self.seat_number, ", ticket date: ", self.date, ", movie start time: ", self.movie_start_time, ", movie end time: ", self.movie_end_time

 # News are added to the news.json file.
def add_news(added_title, added_description):
    with open('news.json', encoding=('UTF-8')) as f:
        news_dict = dict()
        if os.stat('news.json').st_size != 0:
            news = json.load(f)
            for new in news:
                title = news[new]["title"]
                description = news[new]["description"]
                date = news[new]["date"]
                n = News(title, description, date)
                news_dict[new] = vars(n)
        n = News(added_title, added_description, str(datetime.datetime.now().date()))
        news_dict[added_title] = vars(n)
        with open('news.json', 'w', encoding=('UTF-8')) as outfile:
            json.dump(news_dict, outfile, ensure_ascii=False)
        print(vars(n), "\n")


# A specified news is removed from the news.json file.
def remove_news(removed_title):
    with open('news.json', encoding=('UTF-8')) as f:
        news_dict = dict()
        if os.stat('news.json').st_size == 0:
            print("news.json file is empty!")
            exit(0)
        news = json.load(f)
        news_deleted = False
    for new in news:
        title = news[new]["title"]
        description = news[new]["description"]
        date = news[new]["date"]
        n = News(title, description, date)
        if removed_title == n.news_name():
            news_deleted = True
            pass
        else: news_dict[new] = vars(n)
    with open('news.json', 'w', encoding=('UTF-8')) as outfile:
        json.dump(news_dict, outfile, ensure_ascii=False)
    if news_deleted == False:
        print("No news with such name found, therefore no news have been deleted.")
    else: print(news_dict, "\n")

 # A new movie is added to the movies.json file.
def add_movie(added_title, added_director, added_age_rating, added_duration, added_is_3d):
    with open('movies.json', encoding=('UTF-8')) as f:
        movie_dict = dict()
        if os.stat('movies.json').st_size != 0:
            movies = json.load(f)
            for movie in movies:
                title = movies[movie]["title"]
                director = movies[movie]["director"]
                age_rating = movies[movie]["age_rating"]
                duration = movies[movie]["duration"]
                is_3d = movies[movie]["is_3d"]
                m = Movie(title, director, age_rating, duration, is_3d)
                if m.movie_name() == added_title:
                    print ("Movie already exists!")
                    exit(0)
                movie_dict[movie] = vars(m)
    m = Movie(added_title, added_director, added_age_rating, added_duration, added_is_3d)
    movie_dict[m.movie_name()] = vars(m)
    with open('movies.json', 'w', encoding=('UTF-8')) as outfile:
        json.dump(movie_dict, outfile, ensure_ascii=False)
    print(movie_dict, "\n")


# A specified movie is removed from the movies.json file.
def remove_movie(removed_title):
    with open('movies.json', encoding=('UTF-8')) as f:
        movie_dict = dict()
        if os.stat('movies.json').st_size == 0:
            print("movies.json file is empty!")
            exit(0)
        movies = json.load(f)
        movie_deleted = False
    for movie in movies:
        title = movies[movie]["title"]
        director = movies[movie]["director"]
        age_rating = movies[movie]["age_rating"]
        duration = movies[movie]["duration"]
        is_3d = movies[movie]["is_3d"]
        m = Movie(title, director, age_rating, duration, is_3d)
        if removed_title == m.movie_name():
            movie_deleted = True
            pass
        else: movie_dict[movie] = vars(m)
    with open('movies.json', 'w', encoding=('UTF-8')) as outfile:
        json.dump(movie_dict, outfile, ensure_ascii=False)
    if movie_deleted == False:
        print("No movie with such name found, therefore no movies have been deleted.")
    else: print(movie_dict, "\n")


 # Only movies that are in 3D are printed.
def output_3d_movies():
    with open('movies.json',  encoding=('UTF-8')) as f:
        if os.stat('movies.json').st_size == 0:
            print("movies.json file is empty!")
            exit(0)
        movies = json.load(f)
        count = 0
        movie_dict = dict()
    for movie in movies:
        title = movies[movie]["title"]
        director = movies[movie]["director"]
        age_rating = movies[movie]["age_rating"]
        duration = movies[movie]["duration"]
        is_3d = movies[movie]["is_3d"]
        m = Movie(title, director, age_rating, duration, is_3d)
        if m.movie_is_3d() == True:
            movie_dict[movie] = vars(m)
            print(vars(m), "\n")
            count = count + 1
            with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                json.dump(movie_dict, outfile, ensure_ascii=False)

    if count == 0:
        print("No 3D movies found!")
    else: print ("3D movies found: ", count)

 # Only movies specified by the age rating are printed.
def output_movies_age_rating(rating, criterion):
    with open('movies.json',  encoding=('UTF-8')) as f:
        if os.stat('movies.json').st_size == 0:
            print("movies.json file is empty!")
            exit(0)
        movies = json.load(f)
        count = 0
        movie_dict = dict()
    for movie in movies:
        title = movies[movie]["title"]
        director = movies[movie]["director"]
        age_rating = movies[movie]["age_rating"]
        duration = movies[movie]["duration"]
        is_3d = movies[movie]["is_3d"]
        m = Movie(title, director, age_rating, duration, is_3d)
        if criterion == "Up to" or criterion == "up to":
            if int(age_rating) <= int(rating):
                movie_dict[movie] = vars(m)
                print(vars(m), "\n")
                count = count + 1
                with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                    json.dump(movie_dict, outfile, ensure_ascii=False)
        if criterion == "From" or criterion == "from":
            if int(age_rating) >= int(rating):
                movie_dict[movie] = vars(m)
                print(m.__str__(), "\n")
                count = count + 1
                with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                    json.dump(movie_dict, outfile, ensure_ascii=False)
    if count == 0:
         print("No movies with such age rating found!")
    else: print ("Movies ", criterion, " ", rating, " found: ", count)

# Purchase a ticket.
def buy_ticket (moviename, time, seat, row):
    with open('movies.json',  encoding=('UTF-8')) as f:
        if os.stat('movies.json').st_size == 0:
            print("movies.json file is empty!")
            exit(0)
        movies = json.load(f)
        movie_found = False
        ticket_dict = dict()
    with open ('tickets.json', encoding=('UTF-8')) as f2:
        if os.stat('tickets.json').st_size != 0:
            tickets = json.load(f2)
            for ticket in tickets:
                title = tickets[ticket]["title"]
                price = tickets[ticket]["price"]
                seat_number = tickets[ticket]["seat_number"]
                row_number = tickets[ticket]["row_number"]
                date = tickets[ticket]["date"]
                movie_start_time = tickets[ticket]["movie_start_time"]
                movie_end_time = tickets[ticket]["movie_end_time"]
                t = Ticket (title, price, seat_number, row_number, date, movie_start_time, movie_end_time)
                ticket_dict[ticket] = vars(t)
    for movie in movies:
        title = movies[movie]["title"]
        director = movies[movie]["director"]
        age_rating = movies[movie]["age_rating"]
        duration = movies[movie]["duration"]
        is_3d = movies[movie]["is_3d"]
        m = Movie(title, director, age_rating, duration, is_3d)
        movie_end_time = datetime.datetime.strptime(time, '%H:%M') + datetime.timedelta(minutes=int(m.movie_duration()))
        movie_end_time = str(movie_end_time.time())
        if m.movie_is_3d() == True:
            price = 5
        else: price = 4.5
        if m.movie_name() == moviename:
            movie_found = True
            t = Ticket(m.movie_name(), price, seat, row, str(datetime.date.today()), time, movie_end_time)
            ticket_dict[movie] = vars(t)
            print(vars(t))
            with open('tickets.json', 'w', encoding=('UTF-8')) as outfile:
                json.dump(ticket_dict, outfile, ensure_ascii=False)
    if movie_found == False:
         print("No movies with such name found!")
    else: print ("Ticket bought!")

# Print only movies that have been featured on the news.
def output_featured_movies ():
    if os.stat('movies.json').st_size == 0:
        print("movies.json file is empty!")
        exit(0)
    if os.stat('news.json').st_size == 0:
        print("news.json file is empty!")
        exit(0)
    movie_found = False
    movie_dict = dict()
    with open('movies.json', encoding=('UTF-8')) as f:
        movies = json.load(f)
    with open('news.json', encoding=('UTF-8')) as f2:
        news = json.load(f2)
    for new in news:
        news_title = news[new]["title"]
        description = news[new]["description"]
        date = news[new]["date"]
        n = News(news_title, description, date)
        for movie in movies:
            title = movies[movie]["title"]
            director = movies[movie]["director"]
            age_rating = movies[movie]["age_rating"]
            duration = movies[movie]["duration"]
            is_3d = movies[movie]["is_3d"]
            m = Movie(title, director, age_rating, duration, is_3d)

            if m.movie_name() in n.news_name() or m.movie_name() in n.news_description():
                movie_found = True
                movie_dict[movie] = vars(m)
                print(vars(m))
                with open('results.json', 'w', encoding=('UTF-8')) as outfile:
                    json.dump(movie_dict, outfile, ensure_ascii=False)
    if movie_found == False:
        print("No movies with such name found in the news!")


print("Welcome! Available functions: \n \n buy ticket \n add movie \n remove movie \n add news \n remove news \n output all news \n output all movies \n output 3D movies \n output featured movies \n output movies by specified age rating \n")
action = input("Please select a function by typing it in here:   ")
if action == "buy ticket":
    moviename = input("Please select a movie name:  ")
    time = input("Please select the time:   ")
    seat = input("Please select the seat:   ")
    row = input("Please select the row:    ")
    buy_ticket(moviename, time, seat, row)
if action == "add movie":
    title = input("Please enter the title of the movie you would like to add:   ")
    director = input("Who is the director of the movie?:   ")
    age_rating = input("What is the age rating of the movie?:    ")
    duration = input("What is the duration of the movie (in minutes)?:  ")
    is_3d = input("Is the movie in 3D?:  ")
    add_movie(title, director, age_rating, duration, is_3d)
if action == "remove movie":
    title = input("Please enter the title of the movie you would like to remove:    ")
    remove_movie(title)
if action == "add news":
    title = input("Please give a title for the news:    ")
    description = input("Please give a description for the news:    ")
    add_news(title, description)
if action == "remove news":
    title = input("Please enter the title of the news you would like to remove:    ")
    remove_news(title)
if action == "output all news":
    News.output_news(News)
if action == "output all movies":
    Movie.output_movies(Movie)
if action == "output featured movies":
    output_featured_movies()
if action == "output 3D movies" or action == "output 3d movies":
    output_3d_movies()
if action == "output movies by specified age rating":
    rating = input("What age rating?    ")
    criterion = input("Up to " + rating +" or from " + rating + "?      ")
    output_movies_age_rating(rating, criterion)

