import filereadwrite


# News may have a title, a description and a link.

class News:

    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

    # Get the title of the news.
    def news_name(self):
        return self.title

    # Get the description of the news.
    def news_description(self):
        return self.description

    # Get the link of the news.
    def news_link(self):
        return self.link

    # Get all the attributes of the news.

    def __str__(self):
        return "News title: ", self.title, ", news description: ", self.description, ", news link: ", self.link


# News, along with their title and description are added.
def add_news(added_title, added_description, added_link):
    newsfile = filereadwrite.File.file_read_create_if_not_found("news")
    news_dict = dict()
    for item in newsfile:
        n = News(newsfile[item]["title"], newsfile[item]["description"], newsfile[item]["link"])
        news_dict[item] = vars(n)
    n = News(added_title, added_description, added_link)
    news_dict[added_title] = vars(n)
    filereadwrite.File.file_write("news", news_dict)
    print("News found and added! Title:", n.news_name(), ", description: ", n.news_description(), ", link: ",
          n.news_link())


#  News selected by the title are deleted.
def remove_news(removed_title):
    newsfile = filereadwrite.File.file_read("news")
    news_dict = dict()
    news_deleted = False
    for item in newsfile:
        n = News(newsfile[item]["title"], newsfile[item]["description"], newsfile[item]["link"])
        if removed_title == n.news_name():
            news_deleted = True
            print("News found and removed! Title:", n.news_name(), ", description: ", n.news_description(), ", link: ",
                  n.news_link())
            pass
        else:
            news_dict[item] = vars(n)
    filereadwrite.File.file_write("news", news_dict)
    if news_deleted == False:
        print("No news with such name found, therefore no news have been deleted.")


# All the news are printed.
def output_news():
    newsfile = filereadwrite.File.file_read("news")
    news_dict = dict()
    for item in newsfile:
        n = News(newsfile[item]["title"], newsfile[item]["description"], newsfile[item]["link"])
        news_dict[item] = vars(n)
        print(vars(n), "\n")
    filereadwrite.File.file_write("results", news_dict)
