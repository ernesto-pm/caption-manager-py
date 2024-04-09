from pydantic import BaseModel

class Dataset(BaseModel):
    name: str
    description: str
    directoryAbsPath: str
