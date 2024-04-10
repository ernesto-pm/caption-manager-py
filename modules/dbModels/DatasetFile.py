from pydantic import BaseModel

class DatasetFile(BaseModel):
    datasetID: str
    filenameWithExtension: str
    filenameWithoutExtension: str
    fileExtension: str
    absPath: str
    ignored: bool
