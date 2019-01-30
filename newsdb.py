#!/usr/bin/python3

# IN PROGRESS

import psycopg2
import bleach

# def test_connection():
#     '''Tests connection to the database'''
#
#     db = psycopg2.connect("dbname=news")
#     c = db.cursor()
#     c.execute("select * from articles limit 5")

"""
def connect(database_name):
    '''Connect to the PostgreSQL database. Returns a database connection.'''
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        # Exit program
        sys.exit(1)
        
        # TODO - throw an error instead of exit       

db, c = connect(database_name)
        
def get_query_results(query):
    # connect to the database, get cursor
    
    # execute
    c.execute(query)
    # commit
    
    # store the results
    results = c.fetchall()
    #close the connection
    db.close() 
    return results
    

# Call get_query_results and print results based on query

results = get_query_results("Send in query here")


# ARTICLES - top three articles
top_articles = ("select * from popular limit 3")
title_format = article[0]
title = title_format.title()
hits = article[1]
print("{0} – {1} views".format(title, hits))
print("What are the most popular three articles of all time? \n")


# AUTHORS - popular authors
top_authors = ("select * from authorviews limit 5")
for author in authors:
    print("{} – {} views".format(author[0], author[1]))
print("\nWho are the most popular article authors of all time?\n")

    
# ERRORS - days with > 1 % errors
bad_days = ("select to_char(day, 'Month DD, YYYY') as date, percent from final where percent > 1;")
for error in errors:
    print("{} – {}% errors".format(error[0], error[1]))
print("\nOn which days did more than 1% of requests lead to errors?")
