# pythondb
## A python database library because I'm too lazy to learn sql or anything

pythondb is a working title. It will remain the repo name but users will be shown a different name.

#### Contents:
- [Getting started](documentation/gettingStarted.md)
- [User reference](documentation/userReference.md)
- [Programming standards](documentation/programmingStandards.md)
- [Database structure and example database](documentation/databaseStructure.md)

#### Fields
(Note: the 'example below' is the example in [Database obj structure](#database-obj-structure))
I like the idea of nested fields. I don't there to be a necessity for multiple databases. Because this is stored as json, you can nest however much you wish to. Therefore, you can have multi level fields such as the `preferences` field in the example below. Each field of the database is actually a list (in both the file and the 'api') which contains steps from how to get from the row to the field data.

To get to the `height` field of a user in the example below, you simply navigate to `height`, so the path (and by extension field name) is `['height']`. The call to `pythondb.getRowsFromField` would be `pythondb.getRowsFromField(data=aDatabaseObject, field=['height'])`.

The `preferences` field in the example below contains fields. To access the `preferences` field as an object containing the subfields, you would call `pythondb.getRowsFromField(data=aDatabaseObject, field=['preferences'])`. To access the `color` field of the `preferences`, the path would be `preferences` -> `color`, or `['preferences', 'color']`. The call to `pythondb.getRowsFromField` would be `pythondb.getRowsFromField(data=aDatabaseObject, field=['preferences', 'color'])`

#### Example basic usage:
```python
import pythondb

data = pythondb.openDatabase('users.json')
```

#### Database obj structure:
(with example data and fields)
This is the entire object that is read and written to files and passed around.
```json
{
    "name" : "testDb",
    "uniqueFields" : [
        ["id"],
        ["username"]
    ],
    "nonUniqueFields" : [
        ["passwordHash"],
        ["height"],
        ["weight"],
        ["preferences"],
        ["preferences", "color"]
    ],
    "rows" : [
        {
            "id" : 555,
            "username" : "james123",
            "passwordHash" : "sgkjdlagkjdasg",
            "height" : 135,
            "weight" : 80,
            "preferences" : {
                "color" : "red"
            }
        },
        {
            "id" : 5566,
            "username" : "james1234",
            "passwordHash" : "sgkjdlagadfkjdasg",
            "height" : 15,
            "weight" : 80,
            "preferences" : {
                "color" : "blue"
            }
        }
    ]
}
```