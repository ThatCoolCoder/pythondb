import pythondb

print('beginning: create db')
db = pythondb.createDatabase('db', ['name', 'age'],
    ['height', 'preferences', 'preferences/color', 'test\/thing\/'])
print('db created')

print('beginning: save db')
pythondb.saveDatabase(db)
print('db saved')

print('beginning: open db')
db2 = pythondb.openDatabase('db.json')
print('db opened')

print('beginning: create row')
data = {'name' : 'me', 'age' : 13,
    'height' : 122, 'preferences' : {}, 'preferences/color' : 'red', 'test\/thing\/' : 'testy'}
row = pythondb.createRow(db2, data)
print('row created')

print('beginning: append row')
pythondb.appendRow(db2, row)
print('row appended')

print('beginning: db saved again')
pythondb.saveDatabase(db2)
print('db saved again')

print('beginning: open db again')
db3 = pythondb.openDatabase('db.json')
print('db opened again')

print('db name is:', pythondb.getDatabaseName(db3))

print('beginning: create second row')
data = {'name' : 'me2', 'age' : 14,
    'height' : 122, 'preferences' : {}, 'preferences/color' : 'red', 'test\/thing\/' : 'testy'}
row = pythondb.createRow(db3, data)
print('second row created')

print('beginning: insert second row')
pythondb.insertRow(db3, row, 0)
print('inserted second row')

print('beginning: create third row')
data = {'name' : 'a', 'age' : 11,
    'height' : 1, 'preferences' : {}, 'preferences/color' : 'orange', 'test\/thing\/' : 'testy2'}
row = pythondb.createRow(db3, data)
print('third row created')

print('beginning: append third row')
pythondb.insertRow(db3, row)
print('inserted third row')

row = pythondb.getRowByUniqueField(db3, 'name', 'a')
print('unique row:', row)

rows = pythondb.getRowsByField(db3, 'test\/thing\/', 'testy')
print('non-unique rows:', rows)

print('field value is:', pythondb.getFieldContents(row, 'preferences/color'))

print('column is:', pythondb.getColumn(db3, 'preferences'))

print('beginning: set field value')
row = pythondb.setFieldValue(db3, row, 'preferences/color', 'not a real color')
print('field value set')

print('beginning: set db name')
row = pythondb.setDatabaseName(db3, 'db2')
print('field value set')

print('beginning: db saved again 2')
pythondb.saveDatabase(db3)
print('db saved again 2')

print('Testing weird field names', db3['rows'][0]['test\/thing\/'])