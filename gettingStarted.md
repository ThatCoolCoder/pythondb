# Getting started with pythondb

[Back to README](README.md)

This a basic guide on using pythondb. For a full reference, go to [userReference.md](userReference.md)

## Very Basics:
The first step in using pythondb is to import it:
```python
import pythondb
```
Then you will want to either open or create a database. In this example, I will create one.
```python
import pythondb

db = pythondb.createDatabase('my database', ['name'], ['age'], [])
```
This program creates a database with called `'my database'`.
It has only one unique field - `'name'`.
It also has a non-unique field - `'age'`.
The database will be initialised with no rows, because the last argument is an empty list.
Note that you can leave off the last three arguments to `pythondb.createDatabase()` - these default to empty lists.

## fields and fieldPaths
A field is a ?. I can't explain that, sorry. A fieldPath is how you tell pythondb to access a field in a row.