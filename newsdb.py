#!/usr/bin/python3

import psycopg2, bleach

# Requires hits view count for time an article slug appears in the server log

"""
Test connection to db
def test_connection():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from articles limit 5")
"""

def get_top_three_articles():
  """Returns the most popular three articles of all time, sorted by the most popular at the top."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  # Execute a query for the top three articles using 'popular' view of log table
  query = ("select * from popular limit 3")
  c.execute(query)
  # Fetch the results of the query then close the db connection
  articles = c.fetchall()
  db.close()
  # Print the article title and no. of hits
  for article in articles:
      title_format = article[0]
      title = title_format.title()
      hits = article[1]
      print ('{} – {} views'.format(title, hits))


def get_top_authors():
  """Returns which authors get the most page views as a sorted list with the most popular author at the top."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  # Execute a query for the top three articles using 'popular' view of log table
  query = ("select name, sum(hits) as views from bylines, popular where bylines.slug = popular.substring news-> group by name order by views desc")
  c.execute(query)
  # Fetch the results of the query then close the db connection
  authors = c.fetchall()
  db.close()
  # Print the article title and no. of hits
  for author in authors:
      author = author[0]
      views = author[1]
      print ('{} – {} views'.format(author, views))
