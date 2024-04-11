import os
from functools import partial
from tinydb import TinyDB
from tinydb.table import Table
from typing import Callable

def _getTableFor(name: str) -> Table:
    return TinyDB(databasePath).table(name)

databasePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "db.json")
getDatasetTable: Callable[[], Table] = partial(_getTableFor, "dataset")
getDatasetFileTable: Callable[[], Table] = partial(_getTableFor, "datasetFile")
