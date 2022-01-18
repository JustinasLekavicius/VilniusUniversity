import filereadwrite
import datetime
from task4package import movie


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
        return self.seat_number

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
        return "Ticket movie name: ", self.title, ", ticket price: ", self.price, ", seat number: ", self.seat_number, ", ticket date: ", self.date, ", movie start time: ", self.movie_start_time, ", movie end time: ", self.movie_end_time


# Purchase a ticket.
def buy_ticket(moviename, time, seat, row):
    moviefile = filereadwrite.File.file_read("movies")
    movie_found = False
    ticket_dict = dict()
    ticketfile = filereadwrite.File.file_read_create_if_not_found("tickets")
    for item in ticketfile:
        t = Ticket(ticketfile[item]["title"], ticketfile[item]["price"], ticketfile[item]["seat_number"],
                   ticketfile[item]["row_number"], ticketfile[item]["date"], ticketfile[item]["movie_start_time"],
                   ticketfile[item]["movie_end_time"])
        ticket_dict[item] = vars(t)
    for item in moviefile:
        m = movie.Movie(moviefile[item]["title"], moviefile[item]["foreign_title"], moviefile[item]["director"],
                        moviefile[item]["age_rating"],
                        moviefile[item]["duration"], moviefile[item]["is_3d"])
        timestring = moviefile[item]["duration"]
        hours = int(timestring[0:(timestring.index("h"))])
        minutes = int(timestring[timestring.index("h") + 1: timestring.index("min")])
        movie_end_time = datetime.datetime.strptime(time, '%H:%M') + datetime.timedelta(
            minutes=((hours * 60) + minutes))
        movie_end_time = str(movie_end_time.time())
        if m.movie_is_3d():
            price = 5
        else:
            price = 4.5
        if m.movie_name() == moviename or m.movie_foreign_title() == moviename:
            movie_found = True
            t = Ticket(m.movie_name(), price, seat, row, str(datetime.date.today()), time, movie_end_time)
            ticket_dict[item] = vars(t)
            print("Ticket bought! Movie title: ", t.ticket_name(), ", ticket price: ", t.ticket_price(),
                  ", seat number: ", t.ticket_seat_number(), ", movie start time: ", t.ticket_movie_start_time(),
                  ", movie end time: ", t.ticket_movie_end_time())
        filereadwrite.File.file_write("tickets", ticket_dict)
    if not movie_found:
        print("No movies with such name found!")
