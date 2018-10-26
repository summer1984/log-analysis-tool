** Class Project **

# Log Analysis Tool

The log analysis reporting tool is a Python program run from the command line. Using the psycopg2 module and SQL queries, the program analyzes data and prints plain-text reports about the site's user activity.

## Requirements

```
- Python 3.4+
- Psycopg
- Bleach
- PostgreSQL
```

## Getting Started

Try out the reporting tool with a sample PostgreSQL database containing newspaper articles and web server data. 

### Installation

Create a test environment using Vagrant and VirtualBox 

> Install Vagrant and Virtualbox for your operating system – Ensure that the versions you download are compatible!

Once you've launched your virtual machine, download the newsdb.py program file and newsdata.sql file to populate the following tables in the sample database

  * Articles 
  * Authors 
  * Log

Then create the following views

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
WHERE status like '%4%' 
GROUP BY day;
```

```sql
CREATE VIEW final as
SELECT errors.day, round(errors.errors * 100.00/totals.totals, 2) as percent 
FROM errors, totals
WHERE errors.day = totals.day;
```

Run the newsdby.py file from within the test environment to generate a report

> python newsdb.py

## Authors

DM - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Coming Soon
