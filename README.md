** Class Project **

# Log Analysis Tool

The log analysis reporting tool prints plain-text reports based on the data in a database. The tool is a Python program using the psycopg2 module to connect to the database.

## Requirements

```
- Python 3.4+
- Psycopg
- Bleach
- PostgreSQL
```

## Getting Started

Try out the reporting tool with a sample PostgreSQL database containing newspaper articles and web server data. The code uses SQL queries to analyze data and answer questions about the site's user activity.

The program runs from the command line and does not take any input from the user.

### Installation

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

```sql
CREATE VIEW totals as 
SELECT date_trunc('day', time) as day, count(status) as totals 
FROM log 
GROUP BY day;
```

```sql
CREATE VIEW errors as
SELECT date_trunc('day', time) as day, count(status) as errors 
FROM log
WHERE status like '%4%' group by day;
```

```sql
CREATE VIEW final as
SELECT errors.day, round(errors.errors * 100.00/totals.totals, 2) as percent 
FROM errors, totals
WHERE errors.day = totals.day;
```

## Authors

DM - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Coming Soon
