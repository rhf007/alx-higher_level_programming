# Python - Object-relational mapping

So..... Object-Relational Mappers **(ORMS)**, huh? okay...

## What are Object-Relational Mappers?

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

![ORM_diagram](https://www.fullstackpython.com/img/visuals/orms-bridge.png)

## Mmm... and why are they useful again?

ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.

For example, without an ORM a developer would write the following SQL statement to retrieve every row in the USERS table where the ```zip_code``` column is ```94107```:

```sql
SELECT * FROM USERS WHERE zip_code=94107;
```

The equivalent **Django ORM** query would instead look like the following Python code:

```python
# obtain everyone in the 94107 zip code and assign to users variable
users = Users.objects.filter(zip_code=94107)
```

The ability to write Python code instead of SQL can speed up web application development, especially at the beginning of a project. The potential development speed boost comes from not having to switch from Python code into writing declarative paradigm SQL statements. While some software developers may not mind switching back and forth between languages, it's typically easier to knock out a prototype or start a web application using a single programming language.

ORMs also make it theoretically possible to switch an application between various relational databases. For example, a developer could use SQLite for local development and MySQL in production. A production application could be switched from MySQL to PostgreSQL with minimal code modifications.

In practice however, it's best to use the same database for local development as is used in production. Otherwise unexpected errors could hit in production that were not seen in a local development environment. Also, it's rare that a project would switch from one database in production to another one unless there was a pressing reason.

## Do I have to use an ORM for my web application?

Python ORM libraries are not required for accessing relational databases. In fact, the low-level access is typically provided by another library called a database connector, such as psycopg (for PostgreSQL) or MySQL-python (for MySQL). Take a look at the table below which shows how ORMs can work with different web frameworks and connectors and relational databases.

![Orm-framework_compatability](https://www.fullstackpython.com/img/visuals/orm-examples.png)

The above table shows for example that SQLAlchemy can work with varying web frameworks and database connectors. Developers can also use ORMs without a web framework, such as when creating a data analysis tool or a batch script without a user interface.

## It's not all dandy, right? There's gotta be a twist

Well, yeah. There are numerous downsides of ORMs, including

**1.** Impedance mismatch

**2.** Potential for reduced performance

**3.** Shifting complexity from the database into the application code

### Impedance mismatch

The phrase "impedance mismatch" is commonly used in conjunction with ORMs. Impedance mismatch is a catch-all term for the difficulties that occur when moving data between relational tables and application objects. The gist is that the way a developer uses objects is different from how data is stored and joined in relational tables.

### Potential for reduced performance

One of the concerns that's associated with any higher-level abstraction or framework is potential for reduced performance. With ORMs, the performance hit comes from the translation of application code into a corresponding SQL statement which may not be tuned properly.

ORMs are also often easy to try but difficult to master. For example, a beginner using Django might not know about the ```select_related()``` function and how it can improve some queries' foreign key relationship performance. There are dozens of performance tips and tricks for every ORM. It's possible that investing time in learning those quirks may be better spent just learning SQL and how to write stored procedures.

There's a lot of hand-waving "may or may not" and "potential for" in this section. In large projects ORMs are good enough for roughly 80-90% of use cases but in 10-20% of a project's database interactions there can be major performance improvements by having a knowledgeable database administrator write tuned SQL statements to replace the ORM's generated SQL code.

### Shifting complexity from the database into the app code

The code for working with an application's data has to live somewhere. Before ORMs were common, database stored procedures were used to encapsulate the database logic. With an ORM, the data manipulation code instead lives within the application's Python codebase. The addition of data handling logic in the codebase generally isn't an issue with a sound application design, but it does increase the total amount of Python code instead of splitting code between the application and the database stored procedures.

## Python ORM Implementations

There are numerous ORM implementations written in Python, including

**1.** SQLAlchemy

**2.** Peewee

**3.** The Django ORM

**4.** PonyORM

**5.** SQLObject

**6.** Tortoise ORM

## Schema migrations

Schema migrations, for example when you need to add a new column to an existing table in your database, are not technically part of ORMs. However, since ORMs typically lead to a hands-off approach to the database (at the developers peril in many cases), libraries to perform schema migrations often go hand-in-hand with Python ORM usage on web application projects.

## Connecting to a MySQL database

```python
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
```

**Note that the parameter for the password is 'passwd' not 'password'.**

## Getting a Cursor in MySQL Python

The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database. They carry messages (commands) written Python to the MySQL database.

Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.

In order to put our new connnection to good use we need to create a cursor object. The cursor object is an abstraction specified in the Python DB-API 2.0. It gives us the ability to have multiple seperate working environments through the same connection to the database. You can create a cursor by executing the 'cursor' function of your database object.

```python
cur = db.cursor()
```
**So in very simple terms?**

The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database. They carry messages (commands) written Python to the MySQL database.

Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.

Cursors carry messages (commands) written in Python to the MySQL database.

By default the cursor is created using the default cursor class. If you like you can specify a different cursor class by setting the 'cursorclass' parameter to the cursor class you would like to use. There are several different cursor classes that give you different functionality when executing queries.

An example of this is using the DictCursor to have your results returned to you as Python dictionaries instead of the default which is a Python list.

## Executing MySQL Queries in Python

Executing queries is very simple in MySQL Python. All you need to do is take your cursor object and call the 'execute' function. The execute function requires one parameter, the query. If the query contains any substitutions then a second parameter, a tuple, containing the values to substitute must be given.

**Example 1: Create Table**

```python
cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")
```

In this example you can see how a basic query without any parameters is executed.

**Example 2: Execute Insert / Single Substitution Query**

```python
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", song)
    print "Auto Increment ID: %s" % cur.lastrowid
```

In this example, you can see how a query is executed with parameters and you can see how to get the id generated from an auto increment column.

**Example 3: Multiple Substitution Query**

```python
cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1,2))
```

It is important to note that when there are multiple parameters to substitue, you must use a tuple to enclose all of the parameters that need to be passed. The parameters are then substituted from left to right with tupe[0] being the left most substitution and tuple[n] being the right most substitution.

**Example 4: Execute Select**

```python
numrows = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows      
print "Selected %s rows" % cur.rowcount
```

From this you can see that executing select queries is very easy. There are two ways you can get the number of rows the query returned. The MySQLdb specific way is to save the return value from the execute statement. This is NOT the preferred way. You should use the second method which is the Python DB-API 2.0 way because it will make it easier if you ever have to change databases. Both method's are illustrated in this example.

## Obtaining Query Results

After you execute any ```SELECT``` statement, you will need to use one of these methods to obtain your results.

**Method 1: Fetch All-at-Once**

```python
# Print results in comma delimited format
cur.execute("SELECT * FROM song")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"
```

**Method 2: Fetch One-at-a-Time**

```python
cur.execute("SELECT * FROM song WHERE id = 1")
print "Id: %s -- Title: %s" % cur.fetchone()
```

There is no "better" way to do things. You should just use the method that works best for what you are trying to do.

**NOTE** Be careful if you are using the cursor class "CursorUseResultMixIn" or any of it's sub-classes. These cursor classes store their results on the server and feed them to your program as you request them. You have to retreive all of the results and close the cursor before you can execute additional queries.

## Exceptions & Errors

According to the Python DB-API errors are indicated by raising exceptions. There is one top-level exception for the DB package that is used to catch all database exceptions raised by that module. In general this package is 'module.Error'. In MySQL it is 'MySQLdb.Error'.

Every DB-API statement that you execute has the potential to raise an exception. So any time you execute a database query you should surround it with a try/exception block. This includes connections, cursor requests, and statement executions.

```python
# Get data from database
try:
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
except MySQLdb.Error, e:
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)
# Print results in comma delimited format
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"
```

## Clean Up

Clean up is an easy process. All you need to do is close all open cursors, and close all open database connections. Each cursor and each database connection has a 'close' function, call this for each instance you have created.

```python
# Close all cursors
cur.close()
# Close all databases
db.close()
```

We haven't doen anything ORM-related yet, just so you know.

## SQLAlchemy ORM

[This tutorial by the SQLAlchemy website is really cool](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
