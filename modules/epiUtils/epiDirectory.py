from modules.epiUtils.epiObject import EpiObject
from modules.epiUtils import ensureDirectoryExists
from os import listdir
from os.path import join, isfile
from typing import List
from modules.epiUtils.epiFile import EpiFile
from modules.epiUtils.epiList import EpiList
import pandas as pd

class EpiDirectory(EpiObject):
    directoryAbsPath: str

    @classmethod
    def fromFilePath(cls, directoryAbsPath: str, verifyExistence: bool = True):
        if verifyExistence:
            ensureDirectoryExists(directoryAbsPath)

        return cls(directoryAbsPath=directoryAbsPath)

    def getListOfFilePathStrings(self) -> List[str]:
        files = [join(self.directoryAbsPath, f) for f in listdir(self.directoryAbsPath) if isfile(join(self.directoryAbsPath, f))]
        return files

    def getListOfEpiFiles(self) -> EpiList[EpiFile]:
        epiList = EpiList()
        for path in self.getListOfFilePathStrings():
            epiList.append(EpiFile.fromFilePath(absFilePath=path))

        return epiList
