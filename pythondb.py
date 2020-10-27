import simpleFileManager as files
import json
from errors import *

def doNothing(*args, **kwargs):
    pass

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

def getDatabaseName(database):
    return database['name']

def setDatabaseName(database, newName):
    database['name'] = newName

def getFieldContents(row, fieldPath):
    try:
        crntDir = row
        for item in fieldPath:
            crntDir = crntDir[item]
        return crntDir
    except Exception as err:
        raise InvalidFieldPath from err

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

def setField(database, row, fieldPath, fieldValue):
    if fieldPath in database['uniqueFields']:
        # Check if the field of that value has already been taken - 
        # they need to be unique
        fieldTaken = False
        for row in database['rows']:
            if getFieldContents(row, fieldPath) == fieldValue:
                fieldTaken = True;
                break
        
        if fieldTaken:
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

def saveDatabase(database, filename=None):
    if filename is None:
        filename = database['name'] + '.json'
    try:
        databaseStr = json.dumps(database)
        files.write(filename, databaseStr)
    except json.encoder.JsonEncodeError as err:
        raise DatabaseObjectCorrupted from err