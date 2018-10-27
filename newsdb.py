#!/usr/bin/python3

import psycopg2
import bleach

# TODO refactor - connect once/create connection function

# def test_connection():
#     '''Tests connection to the database'''
#
#     db = psycopg2.connect("dbname=news")
#     c = db.cursor()
#     c.execute("select * from articles limit 5")


def get_top_three_articles():
    '''Prints the three most popular articles of all time'''

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # query for the top three articles using 'popular' view
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
        print("{0} – {1} views".format(title, hits))

    def get_top_authors():
        ''''Prints which authors get the most page views'''

        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        query = ("select * from authorviews limit 5")
        c.execute(query)
        authors = c.fetchall()
        db.close()
        # author = authors[0]
        for author in authors:
            print("{} – {} views".format(author[0], author[1]))

    def get_errors():
        '''Prints days when more than 1% of requests led to errors'''

        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        query = ("select to_char(day, 'Month DD, YYYY') as date, percent from final where percent > 1;")
        c.execute(query)
        errors = c.fetchall()
        db.close()
        for error in errors:
            print("{} – {}% errors".format(error[0], error[1]))

    print("What are the most popular three articles of all time? \n")
    get_top_three_articles()

    print("\nWho are the most popular article authors of all time?\n")
    get_top_authors()

    print("\nOn which days did more than 1% of requests lead to errors?")
    get_errors()
