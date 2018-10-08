# Top Articles

This is an internal reporting tool for a newspaper site to discover what kind of articles the site's readers like.

#### How it Works

The program connects to a PostgreSQL database that contains newspaper articles and web server data. The code uses SQL queries to analyze data and answer questions about the site's user activity.

The program runs from the command line and does not take any input from the user.

### Requirements

```
- Python 3.4+
- Psycopg
- Bleach
- PostgreSQL
```


### Getting Started

The database includes three tables: 

  * Authors

  > name | bio | id

  * Articles

  > author | title  | slug | text | lead | body | time | id

  * Public Log
  > path | ip | method | status | time | id 

Create a view of the log to return data about the three articles accessed the most

  ```sql
  create view topthree as
  select substring(path from 10), count(path) as hits
  from log
  group by path
  order by hits desc
  limit 3 offset 1;
  ```

## PostgreSQL documentation

Learn more about the kinds of queries that you can use https://www.postgresql.org/docs/9.5/static/index.html

## Authors

DM - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Coming Soon
