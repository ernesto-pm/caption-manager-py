from modules.epiUtils import ensureDirectoryExists
from os import listdir
from os.path import join, isfile
from typing import List

class EpiDirectory(object):
    directoryPath: str

    def __init__(self, directoryPath: str, verifyExistence: bool = True):
        if verifyExistence:
            ensureDirectoryExists(directoryPath)

        self.directoryPath = directoryPath

    def getAllFilePaths(self) -> List[str]:
        """
        Gets all file paths as a list of strings.
        :return: the absolute paths of files as a string
        """
        files = [f for f in listdir(self.directoryPath) if isfile(join(self.directoryPath, f))]
        return files

