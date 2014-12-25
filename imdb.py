import requests # library to fetch the html contect of given page
import sqlite3 # library to connect to SQLite database
from HTMLParser import HTMLParser # Parser used to parse HTML pages
conn = sqlite3.connect("imdb.db") # Connecting to SQLite database named imdb.db
cursor = conn.cursor()
cursor.execute("CREATE TABLE movies (title text, rating real)")
all_time_gross = requests.get('http://www.imdb.com/boxoffice/alltimegross') # acquiring HTML content of the page that has the list
class movies(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.rating = []
    def handle_starttag(self, tag, attrs):
    	if tag == 'span':
            for name, value in attrs:
      		if name == 'itemprop' and value == 'ratingValue':
    			self.flag = 1
    def handle_data(self, data):
        if self.flag:
            self.rating.append(data);
            self.flag = 0

class complete_list(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movie_count = 0
        self.flag = 0
        self.movies_list = []
    def handle_starttag(self, tag, attrs):
        if self.movie_count>=100:
            return;
    	if tag == 'a':
            for name, value in attrs:
                if name == 'href' and value[:6] == '/title':
                    url = 'http://www.imdb.com'+value
                    rating = requests.get(url)
                    movie_parser.feed(rating.text)
                    self.movie_count += 1
                    self.flag = 1
	                
    def handle_data(self, data):
        if self.flag:
            self.flag = 0
            self.movies_list.append(data);

# instantiate the parser and feed it some HTML
movie_parser = movies()
parser = complete_list()
parser.feed(all_time_gross.text)
for i in range(100):
    cursor.execute("INSERT INTO movies VALUES('"+parser.movies_list[i]+"', '"+movie_parser.rating[i]+"')")
    conn.commit()
print "The average of top 100 movies with a gross income of more than 50 million dollars is: ",
for row in cursor.execute('SELECT AVG(rating) FROM movies'):
    print row[0] 
