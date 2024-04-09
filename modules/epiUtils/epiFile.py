from modules.epiUtils import ensureFileExists
from typing import Optional
import os

# ToDo: make some attributes of this object lazy
class EpiFile(object):
    absFilePath: str
    extension: Optional[str]
    filenameWithoutExtension: Optional[str]
    filenameWithExtension: Optional[str]

    def __init__(self, absFilePath: str, verifyExistence: bool = True):
        self.absFilePath = absFilePath

        if verifyExistence:
            ensureFileExists(self.absFilePath)

        filenameWithExtension = os.path.basename(absFilePath)
        filenameWithoutExtension, extension = os.path.splitext(filenameWithExtension)

        self.extension = extension
        self.filenameWithoutExtension = filenameWithoutExtension
        self.filenameWithExtension = filenameWithExtension

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self), indent=4, width=1)

    def dict(self) -> dict:
        attributes = vars(self)
        attributes['type'] = self.type()

        return attributes

    def type(self) -> str:
        # simple attempt at knowing which type of file is this, just by reading the file extension
        if self.extension == ".txt":
            return "text"
        elif self.extension == ".jpg" or self.extension == ".jpeg" or self.extension == ".png" or self.extension == ".heic":
            return "image"
        elif self.extension == ".json":
            return "json"
        else:
            return "unknown"
