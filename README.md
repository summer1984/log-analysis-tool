** Class Project **

# Log Analysis Tool

The log analysis tool is a Python program that prints plain-text reports about a website's user activity.

The program uses the psycopg2 module and SQL queries to analyze web server data.

The program runs from the command line and does not take input from the user.

# Getting Started

Try out the log analysis tool in the following example scenario using a PostgreSQL database containing newspaper articles and web server data.

## Requirements

```
- Python 3.4+
- Psycopg2
- Bleach
- PostgreSQL
```

### Create a virtual machine(VM) with Vagrant and Virtualbox

You'll set up the database and run the code inside of the VM.

Follow the [Getting Started Guide](https://www.vagrantup.com/intro/getting-started/) to install Vagrant and Virtualbox for your operating system and set up the VM on your computer.

### VM configuration

Download and unzip the [VM configuration file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) for this sample use case. The configuration file will generate a new directory where you'll run the code.

### Change to the VM directory

```
$ cd FSND-Virtual Machine

$ cd vagrant
```

### Start the virtual machine and log in

From inside the ***vagrant*** directory:

```
$ vagrant up

$ vagrant ssh
```

## Set up the database

Download and unzip the [data file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Move these files into the ***vagrant*** directory.

Run the following command from inside the ***vagrant*** directory to populate the database tables _Articles, Authors, Log_.

```
$ psql -d news -f newsdata.sql
```

Create the following views:

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

###

Download the newsdb.py program file to the database directory.

Run the program to generate a report:

```
$ python3 newsdb.py
```

### Authors

DM - *Initial work* -
