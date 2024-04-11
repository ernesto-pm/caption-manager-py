from pydantic import BaseModel
from tinydb.table import Table
from typing import List
from modules.globals import getDatasetTable

class Dataset(BaseModel):
    name: str
    description: str
    directoryAbsPath: str
    _table: Table

    @staticmethod
    def listAll() -> 'List[Dataset]':
        typedDatasets: List[Dataset] = []
        for dataset in getDatasetTable().all():
            typedDatasets.append(Dataset.parse_obj(dataset))

        return typedDatasets

    # Returns the ID of the newly inserted document
    def save(self) -> int:
        return getDatasetTable().insert(self.dict())