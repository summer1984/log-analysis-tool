** Class Project **

# Log Analysis Tool

The log analysis reporting tool is a Python program run from the command line. 

Using the psycopg2 module and SQL queries, the program analyzes data and prints plain-text reports about a site's user activity.

## Requirements

```
- Python 3.4+
- Psycopg
- Bleach
- PostgreSQL
```

# Getting Started

Try out the reporting tool with a sample PostgreSQL database containing newspaper articles and web server data. 

### Create a virtual environment with Vagrant and Virtualbox

Follow the [Getting Started](https://www.vagrantup.com/intro/getting-started/) guide to install and set up the required versions of Vagrant and Virtualbox for your operating system. 

### Download the VM configuration

Download and unzip the configuration file [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip). This will give you a new directory called FSND-Virtual-Machine. 

### Change to the VM directory

```$ cd FSND-Virtual Machine```

```$ cd vagrant```

### Start the virtual machine and log in

From inside the ***vagrant*** directory

```$ vagrant up```

```$ vagrant ssh``` 

## Set up the database

### Download the data

Download and unzip the [data file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Move the files into the ***vagrant*** directory.

### Create the database tables

Run the following command from inside the ***vagrant*** directory to populate the database tables Articles, Authors, Log

`$ psql -d news -f newsdata.sql`

### Create the views 

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

### Generate a report

```$ python newsdb.py```

### Authors

DM - *Initial work* - 

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

Coming Soon
