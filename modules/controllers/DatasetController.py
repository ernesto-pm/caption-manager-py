from tinydb import TinyDB, Query
from tinydb.table import Table
from modules.models import Dataset
import os

class DatasetController(object):
    db: TinyDB
    datasetsTable: Table

    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "data", "db.json"))
        self.datasetsTable = self.db.table("datasets")

    def getAllDatasets(self):
        return self.datasetsTable.all()

    def insertDataset(self, newDataset: Dataset):
        self.datasetsTable.insert(newDataset.dict())
