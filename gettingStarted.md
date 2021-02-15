# Getting started

[Back to README](README.md)

This a basic guide on using pythondb. For a full reference, go to [userReference.md](userReference.md)

## Importing pythondb:
This is very straightforward.
```python
import pythondb
```
This line will import everything you need to manage python databases.

## Database structure:
A pythondb database is made up of rows. Each row represents one of the items that the database manages. These items could be cars, users or transactions. A pythondb database also has columns. These are similar to rows, except that they don't correspond to items - instead they correspond to the properties of the items.

Each row contains fields. These are what hold the data in the row. Each field can contain integers, floats, strings and lists. Fields are accessed using strings called fieldPaths. It is possible to nest fields. To nest a field, put slashes between the 'directories' that hold it, just like file paths.

## Creating a database:
Now you probably want to create a database. To do this, use `pythondb.createDatabase()`. It accepts four arguments:
- The name of the database (in this example, `my database`)
- A list of unique fields (in this example, just `name`)
- A list of non-unique fields (in this example, just `age`)
- And a list of rows to initialise the database with.
This function then returns the database. It is important you store the database in a variable, as pythondb needs direct access to the database for most operations.
```python
import pythondb

db = pythondb.createDatabase('my database', ['name'], ['age'], [])
```