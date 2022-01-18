import filereadwrite
from task3package import news


class Movie:

    def __init__(self, title, foreign_title, director, age_rating, duration, is_3d):
        self.title = title
        self.foreign_title = foreign_title
        self.director = director
        self.age_rating = age_rating
        self.duration = duration
        self.is_3d = is_3d

    # Get the title of the movie.
    def movie_name(self):
        return self.title

    # Get the 3D status of the movie.

    def movie_foreign_title(self):
        return self.foreign_title

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
        return "Movie title: ", self.title, " director: ", self.director, ", age rating: ", self.age_rating, "duration in minutes: ", self.duration, ", the movie is in 3D: ", self.is_3d


# A new movie is added to the movies.json file.
def add_movie(added_title, added_foreign_title, added_director, added_age_rating, added_duration, added_is_3d):
    movie_file = filereadwrite.File.file_read_create_if_not_found("movies")
    movie_dict = dict()
    for item in movie_file:
        m = Movie(movie_file[item]["title"], movie_file[item]["foreign_title"], movie_file[item]["director"],
                  movie_file[item]["age_rating"],
                  movie_file[item]["duration"], movie_file[item]["is_3d"])
        if m.movie_name() == added_title or m.movie_foreign_title() == added_foreign_title:
            print("Movie already exists!")
            pass
        movie_dict[item] = vars(m)
    if added_is_3d == "true" or added_is_3d == "True" or added_is_3d == "yes" or added_is_3d == "Yes":
        added_is_3d = True
    if added_is_3d == "false" or added_is_3d == "False" or added_is_3d == "no" or added_is_3d == "No":
        added_is_3d = False
    m = Movie(added_title, added_foreign_title, added_director, added_age_rating, added_duration, added_is_3d)
    movie_dict[m.movie_name()] = vars(m)
    filereadwrite.File.file_write("movies", movie_dict)
    print("Movie  added! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(), ", director: ",
          m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ", m.movie_duration(),
          ", is in 3D: ", m.movie_is_3d())


# A specified movie is removed from the movies.json file.
def remove_movie(removed_title):
    movie_file = filereadwrite.File.file_read("movies")
    movie_dict = dict()
    movie_deleted = False
    for item in movie_file:
        m = Movie(movie_file[item]["title"], movie_file[item]["foreign_title"], movie_file[item]["director"],
                  movie_file[item]["age_rating"],
                  movie_file[item]["duration"], movie_file[item]["is_3d"])
        if removed_title == m.movie_name() or removed_title == m.movie_foreign_title():
            movie_deleted = True
            pass
        else:
            movie_dict[item] = vars(m)
    filereadwrite.File.file_write("movies", movie_dict)
    if not movie_deleted:
        print("No movie with such name found, therefore no movies have been deleted.")
    else:
        print("Movie removed! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(), ", director: ",
              m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ", m.movie_duration(),
              ", is in 3D: ", m.movie_is_3d())


# Only movies that are in 3D are printed.
def output_3d_movies():
    movie_file = filereadwrite.File.file_read("movies")
    movie_dict = dict()
    count = 0
    for item in movie_file:
        m = Movie(movie_file[item]["title"], movie_file[item]["foreign_title"], movie_file[item]["director"],
                  movie_file[item]["age_rating"],
                  movie_file[item]["duration"], movie_file[item]["is_3d"])
        if m.movie_is_3d():
            movie_dict[item] = vars(m)
            print("Movie  added! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(), ", director: ",
                  m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ", m.movie_duration(),
                  ", is in 3D: ", m.movie_is_3d())

            count = count + 1
    filereadwrite.File.file_write("results", movie_dict)
    if count == 0:
        print("No 3D movies found!")
    else:
        print("3D movies found: ", count)


# Only movies specified by the age rating are printed.
def output_movies_age_rating(rating, criterion):
    movie_file = filereadwrite.File.file_read("movies")
    movie_dict = dict()
    count = 0
    for item in movie_file:
        m = Movie(movie_file[item]["title"], movie_file[item]["foreign_title"], movie_file[item]["director"],
                  movie_file[item]["age_rating"],
                  movie_file[item]["duration"], movie_file[item]["is_3d"])

        if criterion == "Up to" or criterion == "up to" or criterion == "up" or criterion == "Up":
            if movie_file[item]["age_rating"] == "Nenurodyta":
                pass
            elif int(movie_file[item]["age_rating"]) < int(rating):
                movie_dict[item] = vars(m)
                print("Movie  added! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(),
                      ", director: ", m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ",
                      m.movie_duration(), ", is in 3D: ", m.movie_is_3d())

                count = count + 1
                filereadwrite.File.file_write("results", movie_dict)
        if criterion == "From" or criterion == "from":
            if movie_file[item]["age_rating"] == "Nenurodyta":
                pass
            elif int(movie_file[item]["age_rating"]) >= int(rating):
                movie_dict[item] = vars(m)
                print("Movie  added! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(),
                      ", director: ", m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ",
                      m.movie_duration(), ", is in 3D: ", m.movie_is_3d())

                count = count + 1
                filereadwrite.File.file_write("results", movie_dict)
    if count == 0:
        print("No movies with such age rating found!")
    else:
        print("Movies ", criterion, " ", rating, " found: ", count)


# Output only movies that have been featured on the news.
def output_featured_movies():
    movie_found = False
    movie_dict = dict()
    movie_file = filereadwrite.File.file_read("movies")
    news_file = filereadwrite.File.file_read("news")

    for item in news_file:
        n = news.News(news_file[item]["title"], news_file[item]["description"], news_file[item]["link"])
        for item2 in movie_file:
            m = Movie(movie_file[item2]["title"], movie_file[item2]["foreign_title"], movie_file[item2]["director"],
                      movie_file[item2]["age_rating"],
                      movie_file[item2]["duration"], movie_file[item2]["is_3d"])

            if m.movie_name() in n.news_name() or m.movie_name() in n.news_description():
                movie_found = True
                movie_dict[item] = vars(m)
                print("Movie  added! Title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(),
                      ", director: ", m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ",
                      m.movie_duration(), ", is in 3D: ", m.movie_is_3d())

                filereadwrite.File.file_write("results", movie_dict)

    if not movie_found:
        print("No movies with such name found in the news!")


# Every movie, along with its attributes, is printed.
def output_movies():
    movie_dict = dict()
    movie_file = filereadwrite.File.file_read("movies")
    for item in movie_file:
        m = Movie(movie_file[item]["title"], movie_file[item]["foreign_title"], movie_file[item]["director"],
                  movie_file[item]["age_rating"],
                  movie_file[item]["duration"], movie_file[item]["is_3d"])
        movie_dict[item] = vars(m)
        filereadwrite.File.file_write("results", movie_dict)
        print("Movie  title:", m.movie_name(), ", foreign title: ", m.movie_foreign_title(), ", director: ",
              m.movie_director(), ", age rating: ", m.movie_age_rating(), ", duration: ", m.movie_duration(),
              ", is in 3D: ", m.movie_is_3d())
