from pydantic import BaseModel
from typing import List
from modules.globals import getDatasetFileTable

class DatasetFile(BaseModel):
    datasetID: int
    filenameWithExtension: str
    filenameWithoutExtension: str
    fileExtension: str
    absPath: str
    type: str
    ignored: bool

    @staticmethod
    def insertMany(input: 'List[DatasetFile]') -> list[int]:
        dictList = [file.dict() for file in input]
        ids = getDatasetFileTable().insert_multiple(dictList)
        return ids

    def save(self):
        return getDatasetFileTable().insert(self.dict())