"""Python script to talk to SQLite3 databse
"""
import sqlite3


connection=None
cursor=None

def getConnection():
    """ creates the database if does not exist and opens a database connection
    """
    global connection,cursor
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

def create():
    """ drops(if exists) and creates a sql table
    """
    cursor.execute("""DROP TABLE  if exists student;""")
    
    sql_command = """
    CREATE TABLE student ( 
    sid INTEGER PRIMARY KEY, 
    fname VARCHAR(20), 
    lname VARCHAR(30), 
    gender CHAR(1), 
    birth_date DATE);"""

    cursor.execute(sql_command)
    connection.commit()

def insert():
    """insert data in the tables
    """
    sql_command = """INSERT INTO student (sid, fname, lname, gender, birth_date)
        VALUES (1, "Joe", "Dimaggio", "m", "1914-11-25");"""
    cursor.execute(sql_command)


    sql_command = """INSERT INTO student (sid, fname, lname, gender, birth_date)
        VALUES (2, "Mickey", "Mantle", "m", "1931-10-20");"""
    cursor.execute(sql_command)
    connection.commit()

def fetch():
    """retrives data from the tables
    """
    cursor.execute("SELECT * FROM student") 
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    cursor.execute("SELECT * FROM student") 
    print("\nfetch one:")
    res = cursor.fetchone() 
    print(res)

def closeConnection():
    """closes the connection
    """
    connection.close()
    
getConnection()    
create()
insert()
fetch()
closeConnection()
