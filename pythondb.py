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

    data = '{}' # safeguard in case there is a case which slips through
    try:
        stringData = files.read(filename)
    # no except block - let whatever error has occured break out of this function
    # a finally block is needed here to make syntax correct
    finally:
        pass
    
    # Parse the file

    data = {} # safeguard in case there is a case which slips through
    try:
        data = json.loads(stringData)
    except json.decoder.JSONDecodeError as err:
        raise FileCorrupted from err

    return data

def getFieldContents(row, fieldPath):
    try:
        crntDir = row
        for item in fieldPath:
            crntDir = crntDir[item]
        return crntDir
    except Exception as err:
        raise InvalidFieldPath from err

def getRowFromUniqueField(fieldValue, data=None, databaseFileName=None, fieldPath=[]):
    # If data is defined, use that as the database
    # else try to read database from databaseFileName

    if data is not None:
        doNothing() # don't need to do anything - data is how we need it
    elif databaseFileName is not None:
        data = openDatabase(databaseFileName)
    else:
        raise NoDatabaseProvided

    # If the field doesn't exist, exit
    if fieldPath not in data['uniqueFields']:
        raise InvalidFieldPath

    row = None

    for crntRow in data['rows']:
        if getFieldContents(crntRow, fieldPath) == fieldValue:
            row = crntRow
            break
    
    return row

        
def getRowsFromField(fieldValue, data=None, databaseFileName=None, fieldPath=[]):
    # If data is defined, use that as the database
    # else try to read database from databaseFileName

    if data is not None:
        doNothing() # don't need to do anything - data is how we need it
    elif databaseFileName is not None:
        data = openDatabase(databaseFileName)
    else:
        raise NoDatabaseProvided

    # If the field doesn't exist, exit
    if fieldPath not in data['nonUniqueFields']:
        raise InvalidFieldPath

    rows = []
    for crntRow in data['rows']:
        if getFieldContents(crntRow, fieldPath) == fieldValue:
            rows.append(crntRow)
    
    return rows