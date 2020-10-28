import simpleFileManager as files
import json
from errors import *

def doNothing(*args, **kwargs):
    pass

# File stuff
# ----------

def openDatabase(filename):
    # Open and load the database at filename, return it as an object

    # Read the file

    # This try-except-finally is not needed as of now
    # as the only error which is expected doesn't get caught,
    # but it will make for easier modification in future

    stringData = '{}' # safeguard in case there is a case which slips through
    try:
        stringData = files.read(filename)
    # no except block - let whatever error has occured break out of this function
    # a finally block is needed here to make syntax correct
    finally:
        pass
    
    # Parse the file

    try:
        database = json.loads(stringData)
        return database
    except json.decoder.JSONDecodeError as err:
        raise FileCorrupted from err

def saveDatabase(database, filename=None):
    if filename is None:
        filename = database['name'] + '.json'
    try:
        databaseStr = json.dumps(database)
        files.write(filename, databaseStr)
    except json.encoder.JsonEncodeError as err:
        raise DatabaseObjectCorrupted from err

# Get stuff
# ---------

def getDatabaseName(database):
    return database['name']

def getFieldContents(row, fieldPath):
    try:
        crntDir = row
        for item in fieldPath:
            crntDir = crntDir[item]
        return crntDir
    except Exception as err:
        raise InvalidFieldPath from err

def getColumn(database, fieldPath):
    if fieldPath not in database['uniqueFields'] or \
        fieldPath not in database['nonUniqueFields']:
        raise InvalidFieldPath

    column = []
    for crntRow in database['rows']:
        column.append(getFieldContents(crntRow, fieldPath))
    
    return column

def getRowFromUniqueField(database, fieldPath, fieldValue):
    # Find the row which has fieldPath set to fieldValue

    # If the field doesn't exist, exit
    if fieldPath not in database['uniqueFields']:
        raise InvalidFieldPath

    row = None

    for crntRow in database['rows']:
        if getFieldContents(crntRow, fieldPath) == fieldValue:
            row = crntRow
            break
    
    return row

        
def getRowsFromField(database, fieldPath, fieldValue):
    # Find all of the fields in which fieldPath is set to fieldValue
    
    # If the field doesn't exist, exit
    if fieldPath not in database['nonUniqueFields']:
        raise InvalidFieldPath

    rows = []
    for crntRow in database['rows']:
        if getFieldContents(crntRow, fieldPath) == fieldValue:
            rows.append(crntRow)
    
    return rows

# Set stuff
# ---------

def setDatabaseName(database, newName):
    database['name'] = newName

def setField(database, row, fieldPath, fieldValue):
    if fieldPath in database['uniqueFields']:
        existingValues = getColumn(database, fieldPath)
        if fieldValue in existingValues:
            raise FieldAlreadyTaken
        else:
            # Navigate to the dir containing the field
            containingDir = getFieldContents(row, fieldPath[:-1])
            # Then set the last part (the actual field) to the value
            containingDir[fieldPath[-1]] = fieldValue
            
    elif fieldPath in database['nonUniqueFields']:
        containingDir = getFieldContents(row, fieldPath[:-1])
        containingDir[fieldPath[-1]] = fieldValue
    else:
        raise InvalidFieldPath

# Add stuff
# ---------

def createRow(database, rowContents):
    # Row contents is in the form:
    # [(fieldPath, value), (fieldPath, value)]
    # eg:
    # [ (['username'], 'pete'), (['color'], 'red') ] 

    row = {}
    # Set the keys and values of the row object
    for fieldSet in rowContents:
        fieldPath, value = fieldSet
        print(fieldPath, value)

        # Check if the fieldPath is a valid field
        if fieldPath in database['uniqueFields'] or \
            fieldPath in database['nonUniqueFields']:
            setField(database, row, fieldPath, value)
        else:
            raise InvalidFieldPath
    
    # Now check if the row has any duplicate unique fields
    if not canAddRow(database, row):
        raise FieldAlreadyTaken
    
    return row

def addRow(database, row):
    # somehow create the row
    
    if canAddRow(database, row):
        database['rows'].append(row)
    else:
        raise FieldAlreadyTaken

# Other
# -----

def canAddRow(database, row):
    # Check whether any of the row's unique fields are not actually unique

    duplicateFieldFound = False
    for fieldPath in database['uniqueFields']:
        column = getColumn(database, fieldPath)
        if getFieldContents(row, fieldPath) in column:
            duplicateFieldFound = True
            break
    
    return duplicateFieldFound
