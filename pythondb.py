import simpleFileManager as files
import json
from errors import *

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

def getRowFromUniqueField(data=None, databaseFileName=None, fieldPath=[]):
    # 
    # If data is defined, use that as the database
    # else if 

def getRowsFromField()