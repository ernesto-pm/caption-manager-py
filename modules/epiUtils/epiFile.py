from modules.epiUtils.epiObject import EpiObject
from modules.epiUtils import ensureFileExists
from typing import Optional
from pydantic import computed_field
import os

# ToDo: make some attributes of this object lazy
class EpiFile(EpiObject):
    absFilePath: str
    extension: Optional[str]
    filenameWithoutExtension: Optional[str]
    filenameWithExtension: Optional[str]

    @classmethod
    def fromFilePath(cls, absFilePath: str, verifyExistence: bool = True):
        if verifyExistence:
            ensureFileExists(absFilePath)

        filenameWithExtension = os.path.basename(absFilePath)
        filenameWithoutExtension, extension = os.path.splitext(filenameWithExtension)

        return cls(absFilePath=absFilePath, extension=extension,
                   filenameWithoutExtension=filenameWithoutExtension,
                   filenameWithExtension=filenameWithExtension
        )

    @computed_field
    @property
    def fileType(self) -> str:
        # simple attempt at knowing which type of file is this, just by reading the file extension
        if self.extension == ".txt":
            return "text"
        elif self.extension == ".jpg" or self.extension == ".jpeg" or self.extension == ".png" or self.extension == ".heic":
            return "image"
        elif self.extension == ".json":
            return "json"
        else:
            return "unknown"

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self), indent=4, width=1)
