from tinydb import TinyDB, Query
import os
from pathlib import Path

class DatasetController(object):
    def __init__(self):
        self.datasetDir = os.path.join(os.getcwd(), "data")

        if not os.path.isdir(self.datasetDir):
            # dataset path is not initialized (maybe the first time we ran this)

    def initializeDirectoriesAndFiles(self):
        # check if data directory is available here
        currentDir = os.getcwd()

        if not os.path.isdir(path)
