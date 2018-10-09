#!/usr/bin/env python3

import psycopg2, bleach

def get_top_three_articles():
  """Returns the most popular three articles of all time, sorted by the most popular at the top."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()

  # Test connection to db
  # c.execute("select * from articles")

  # Execute a query for the top three articles using 'toparticles' view of log table
  query = ("select title, hits from articles, topthree where articles.slug = topthree.substring order by hits desc")
  c.execute(query)

  # After you fetch the articles close the db connection
  articles = c.fetchall()
  db.close()

  # Print the article title and number of hits to look like "Princess Shellfish Marries Prince Handsome" — 1201 views
  for article in articles:
      title_format = article[0]
      title = title_format.title()
      hits = article[1]
      print ('{} – {} views'.format(title, hits))
