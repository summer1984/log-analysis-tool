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

## Getting Started

Try out the reporting tool with a sample PostgreSQL database containing newspaper articles and web server data. 

### Create a Test Environment

Use a virtual machine (VM) to run the program. Follow the [Getting Started](https://www.vagrantup.com/intro/getting-started/) guide to install the required versions of Vagrant and Virtualbox for your operating system. 

### Download the VM configuration

Download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip). 

This will give you a new directory called FSND-Virtual-Machine. Change to this directory in your terminal with `cd`. 

Inside, you will find another directory called **vagrant**. Change to the **vagrant** directory: `$ cd vagrant`.

### Start the virtual machine

From inside the vagrant subdirectory, run the command ` $vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is. 

When you get your shell prompt back, run `$ vagrant ssh` to log in to your newly installed VM.

### Download the data

[Download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the file after downloading it. 

Move the newsdata.sql file into the Vagrant directory shared with your VM.

### Create the database tables

`cd` into the Vagrant directory and run the following command to populate the sample database tables for Articles, Authors, and Log

`$ psql -d news -f newsdata.sql`

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
