from task3package import movie
from task3package import news
from task3package import ticket

print(
    "Welcome! Available functions: \n \n buy ticket \n add movie \n remove movie \n add news \n remove news \n output all news \n output all movies \n output 3D movies \n output featured movies \n output movies by specified age rating \n")
action = input("Please select a function by typing it in here:   ")
if action == "buy ticket":
    moviename = input("Please select a movie name:  ")
    time = input("Please select the time:   ")
    seat = input("Please select the seat:   ")
    row = input("Please select the row:    ")
    ticket.buy_ticket(moviename, time, seat, row)
if action == "add movie":
    title = input("Please enter the title of the movie you would like to add:   ")
    foreign_title = input(
        "Please enter the alternative (foreign, for example English) title of the movie you would like to add:   ")
    director = input("Who is the director of the movie?:   ")
    age_rating = input("What is the age rating of the movie?:    ")
    duration = input(
        "What is the duration of the movie? Use this format, replace x with hours and minutes respectively: xh x min:  ")
    is_3d = input("Is the movie in 3D?:  ")
    movie.add_movie(title, foreign_title, director, age_rating, duration, is_3d)
if action == "remove movie":
    title = input("Please enter the title of the movie you would like to remove:    ")
    movie.remove_movie(title)
if action == "add news":
    title = input("Please give a title for the news:    ")
    description = input("Please give a description for the news:    ")
    link = input("Please provide an Internet link for the news:    ")
    news.add_news(title, description, link)
if action == "remove news":
    title = input("Please enter the title of the news you would like to remove:    ")
    news.remove_news(title)
if action == "output all news":
    news.output_news()
if action == "output all movies":
    movie.output_movies()
if action == "output featured movies":
    movie.output_featured_movies()
if action == "output 3D movies" or action == "output 3d movies":
    movie.output_3d_movies()
if action == "output movies by specified age rating":
    rating = input("What age rating?    ")
    criterion = input("Up to " + rating + " or from " + rating + "?      ")
    movie.output_movies_age_rating(rating, criterion)
