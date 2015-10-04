##Working with databases in Python

Using Python, programs that interact with the databases for retrieval, updation can be written with ease. There are a lot of popular database softwares available like [MySql](https://www.mysql.com/), [PostgreSQL](http://www.postgresql.org/), [SQLite](https://www.sqlite.org/) etc. that are used in the industry. However, originally each database module had its own interface causing inconsistency in the conventions among the various modules; Code that worked with one database did not run with another database and had to be rewritten.

To solve the problem above, a specification for a consistent interface to relational databases was created : __DB-API__. The objective of defining __DB-API__ was to make the code that interacts with the database __db-agnostic__ i.e. independent of the type of database it is being used with. It made porting of code to a different database much simpler, requiring the change of only a few lines.

In order to use a database with python, the correct python needs to be downloaded and installed. Some examples of the modules are sqlite3 for SQLite database(included in the python standard library), MySQL-python for MySQL database. General procedure to talk to a database is as follows :

* Importing the API module.
* Acquiring a connection with the database.
* Issuing SQL statements and stored procedures.
* Closing the connection

The source-code to access SQLite from python can be found [__here__](https://github.com/joed7/fose_python/blob/master/python-sqlite.py) and for MySQL [__here__](https://github.com/joed7/fose_python/blob/master/python-mysql.py). Note that code of both of python scripts is almost the same except for import statement at the beginning of the file `import MySQLdb` and `import sqlite3` and the line of code which requests connection from the database  ` MySQLdb.connect (host = "localhost",user = "root",passwd = "root",db = "student")` and `sqlite3.connect("student.db")`.

High level description the program  
1. Get the connection of the database and store it in `connection` variable  
2. Get the cursor object from the connection object. Cursor object is used to execute SQL queries.  
3. Execute insert, update, select as per requirements.  
4. Close the connection.  

