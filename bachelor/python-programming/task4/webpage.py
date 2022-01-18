from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from random import randint

import sqlite3

app = Flask(__name__)
Bootstrap(app)
search_criterion = ""


@app.route("/")
@app.route("/home")
def main():
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    movies = cursor.execute('SELECT * FROM movies').fetchall()
    return render_template('index.html', movie=movies[randint(0, len(movies)) - 1])


@app.route("/addmovie", methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movie_is_3d = request.form.get('movieIs3D')
        movie_image = request.form['movieImage']
        if movie_is_3d:
            movie_is_3d = True
        else:
            movie_is_3d = False
        if movie_image:
            pass
        else:
            movie_image = "None"
        title = request.form['movieTitle']
        title_foreign = request.form['movieTitleForeign']
        movie_director = request.form['movieDirector']
        age_rating = request.form['movieAgeRating']
        movie_duration = request.form['movieDuration']
        connect = sqlite3.connect('task4.db')
        cursor = connect.cursor()
        cursor.execute(
            'INSERT INTO movies (title, foreign_title, director, age_rating, duration, is_3d, image) VALUES (?,?,?,?,?,?,?)',
            (title, title_foreign, movie_director, age_rating, movie_duration, movie_is_3d, movie_image))
        connect.commit()
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        return render_template('template_movie.html', movie=movies[randint(0, len(movies)) - 1], data=movies, count=len(movies))
    else:
        connect = sqlite3.connect('task4.db')
        cursor = connect.cursor()
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        return render_template('template_add_movie.html', movie=movies[randint(0, len(movies)) - 1])


@app.route("/addnews", methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        news_link = request.form['newsLink']
        if news_link:
            pass
        else:
            news_link = "None"
        title = request.form['newsTitle']
        description = request.form['newsDescription']
        connect = sqlite3.connect('task4.db')
        cursor = connect.cursor()
        cursor.execute(
            'INSERT INTO news (title, description, link) VALUES (?,?,?)',
            (title, description, news_link))
        connect.commit()
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        news = connect.execute('SELECT * FROM news').fetchall()
        return render_template('template_news.html', data=news, count=len(news),
                               movie=movies[randint(0, len(movies)) - 1])
    else:
        connect = sqlite3.connect('task4.db')
        cursor = connect.cursor()
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        return render_template('template_add_news.html', movie=movies[randint(0, len(movies)) - 1])


@app.route("/editmovie/<movie_id>", methods=['GET', 'POST'])
def update_movie(movie_id):
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    if request.method == 'POST':
        movie_is_3d = request.form.get('movieIs3D')
        movie_image = request.form['movieImage']
        if movie_is_3d:
            movie_is_3d = True
        else:
            movie_is_3d = False
        if movie_image:
            pass
        else:
            movie_image = "None"
        title = request.form['movieTitle']
        title_foreign = request.form['movieTitleForeign']
        movie_director = request.form['movieDirector']
        age_rating = request.form['movieAgeRating']
        movie_duration = request.form['movieDuration']
        cursor.execute('UPDATE movies SET title = ?, foreign_title = ?, director = ?, age_rating = ?, duration = ?, is_3d = ?, image = ? WHERE id = ? ', (title, title_foreign, movie_director, age_rating, movie_duration, movie_is_3d, movie_image, movie_id) )
        connect.commit()
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        cursor.execute('SELECT * FROM movies WHERE id = (?)',
                       (movie_id,))
        movie_info = cursor.fetchall()
        return render_template('template_selected_movie.html', movie=movies[randint(0, len(movies)) - 1], data=movie_info)
    else:
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        cursor.execute('SELECT * FROM movies WHERE id = (?)',
                       (movie_id,))
        movie_info = cursor.fetchall()
        return render_template('template_edit_movie.html', movie=movies[randint(0, len(movies)) - 1], data=movie_info)


@app.route("/editnews/<news_id>", methods=['GET', 'POST'])
def update_news(news_id):
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    if request.method == 'POST':
        news_link = request.form['newsLink']
        if news_link:
            pass
        else:
            news_link = "None"
        title = request.form['newsTitle']
        description = request.form['newsDescription']
        connect = sqlite3.connect('task4.db')
        cursor = connect.cursor()
        cursor.execute(
            'UPDATE news SET title = ?, description = ?, link = ? WHERE id = ?',
            (title, description, news_link, news_id))
        connect.commit()
        news = connect.execute('SELECT * FROM news').fetchall()
        movies = connect.execute('SELECT * FROM movies').fetchall()
        return render_template('template_news.html', data=news, count=len(news),
                               movie=movies[randint(0, len(movies)) - 1])
    else:
        movies = cursor.execute('SELECT * FROM movies').fetchall()
        news = connect.execute('SELECT * FROM news WHERE id = (?)', (news_id,)).fetchall()
        return render_template('template_edit_news.html', movie=movies[randint(0, len(movies)) - 1], data=news)


@app.route("/movies", methods=['GET', 'POST'])
def outputmovies():
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    if request.method == 'POST':
        movie_id = request.form['delete']
        cursor.execute('DELETE FROM movies WHERE id = (?)',
                       (movie_id,))
        connect.commit()
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        return render_template('template_movie.html', data=movies, count=len(movies),
                               movie=movies[randint(0, len(movies)) - 1])
    else:
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        return render_template('template_movie.html', data=movies, count=len(movies),
                               movie=movies[randint(0, len(movies)) - 1])


@app.route("/news", methods=['GET', 'POST'])
def outputnews():
    conn = sqlite3.connect('task4.db')
    c = conn.cursor()
    if request.method == 'POST':
        news_id = request.form['delete']
        c.execute('DELETE FROM news WHERE id = (?)',
                  (news_id,))
        conn.commit()
        news = c.execute('SELECT * FROM news').fetchall()
        movies = c.execute('SELECT * FROM movies').fetchall()
        return render_template('template_news.html', data=news, count=len(news),
                               movie=movies[randint(0, len(movies)) - 1])
    else:
        news = c.execute('SELECT * FROM news').fetchall()
        movies = c.execute('SELECT * FROM movies').fetchall()
        return render_template('template_news.html', data=news, count=len(news),
                               movie=movies[randint(0, len(movies)) - 1])


@app.route("/movie/<movie_id>", methods=['GET', 'POST'])
def singlemovie(movie_id):
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM movies WHERE id = (?)',
                   (movie_id,))
    movie_info = cursor.fetchall()
    return render_template('template_selected_movie.html', data=movie_info)


@app.route("/search", methods=['GET', 'POST'])
def outputsearch():
    connect = sqlite3.connect('task4.db')
    cursor = connect.cursor()
    criterion = request.values.get('search_input')
    movie_id = request.values.get('delete')
    if movie_id:
        movie_id = request.form.get('delete')
        cursor.execute('DELETE FROM news WHERE id = (?)',
                       (movie_id,))
        connect.commit()
    else:
        pass
    cursor.execute('SELECT * FROM news WHERE title LIKE ? OR description LIKE ?',
                   ('%' + criterion + '%', '%' + criterion + '%',))
    data_news = cursor.fetchall()
    cursor.execute('SELECT * FROM movies WHERE title LIKE ? OR foreign_title LIKE ? OR director LIKE ?',
                   ('%' + criterion + '%', '%' + criterion + '%', '%' + criterion + '%',))
    data_movies = cursor.fetchall()
    movies = cursor.execute('SELECT * FROM movies').fetchall()
    return render_template('template_search.html', data_news=data_news, data_movies=data_movies,
                           count_news=len(data_news), count_movies=len(data_movies), criterion=criterion,
                           movie=movies[randint(0, len(movies)) - 1])
