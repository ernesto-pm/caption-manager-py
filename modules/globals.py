import os
from functools import partial
from tinydb import TinyDB

def _getTableFor(name: str):
    return TinyDB(databasePath).table(name)

databasePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "db.json")
getDatasetTable = partial(_getTableFor, "dataset")

