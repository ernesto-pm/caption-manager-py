from modules.epiUtils import ensureDirectoryExists
from os import listdir
from os.path import join, isfile
from typing import List
from modules.epiUtils.epiFile import EpiFile
import pandas as pd

class EpiDirectory(object):
    directoryAbsPath: str

    def __init__(self, directoryAbsPath: str, verifyExistence: bool = True):
        if verifyExistence:
            ensureDirectoryExists(directoryAbsPath)

        self.directoryAbsPath = directoryAbsPath

    def getListOfFilePathStrings(self) -> List[str]:
        """
        Gets all file paths as a list of strings.
        :return: the absolute paths of files as a string
        """
        files = [join(self.directoryAbsPath, f) for f in listdir(self.directoryAbsPath) if isfile(join(self.directoryAbsPath, f))]
        return files

    def getListOfEpiFiles(self) -> List[EpiFile]:
        """
        Gets all file as epifiles
        :return: a list of epifiles
        """
        files = [EpiFile(path, verifyExistence=False) for path in self.getListOfFilePathStrings()]
        return files

    def getDataframeOfFiles(self) -> pd.DataFrame:
        epiFilesDictionaries = [file.dict() for file in self.getListOfEpiFiles()]
        return pd.DataFrame(epiFilesDictionaries)