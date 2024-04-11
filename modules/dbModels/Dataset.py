from pydantic import BaseModel
from typing import List
from modules.globals import getDatasetTable
from datetime import datetime

class Dataset(BaseModel):
    name: str
    description: str
    directoryAbsPath: str
    createdAt: str = datetime.now().isoformat()

    @staticmethod
    def listAll() -> 'List[Dataset]':
        typedDatasets: List[Dataset] = []
        for dataset in getDatasetTable().all():
            typedDatasets.append(Dataset.parse_obj(dataset))

        return typedDatasets

    # Returns the ID of the newly inserted document
    def save(self) -> int:
        return getDatasetTable().insert(self.dict())
