** Class Project **

# Log Analysis Tool

The log analysis reporting tool prints out reports (in plain text) based on the data in a database. The tool is a Python program using the psycopg2 module to connect to the database.

## Requirements

```
- Python 3.4+
- Psycopg
- Bleach
- PostgreSQL
```

## How it Works

In the following example, the program connects to a PostgreSQL database containing newspaper articles and web server data. The code uses SQL queries to analyze data and answer questions about the site's user activity.

The program runs from the command line and does not take any input from the user.

### Example Tables

Download the newsdata.sql file to populate the following tables in the database

  * Articles 
  * Authors 
  * Log

Create the following views

  ```sql
CREATE VIEW popular as
SELECT substring(path from 10), count(path) as hits
FROM log
WHERE path != '/'
GROUP BY path
ORDER BY hits desc;
  ```
  
```sql
CREATE VIEW bylines as
SELECT name, slug
FROM authors, articles
WHERE authors.id = articles.author
```
## PostgreSQL documentation

Learn more about the kinds of queries that you can use https://www.postgresql.org/docs/9.5/static/index.html

## Authors

DM - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Coming Soon
