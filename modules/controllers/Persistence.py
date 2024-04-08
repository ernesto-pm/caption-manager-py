from tinydb import TinyDB, Query
import os
from pathlib import Path

class Persistence(object):
    def __init__(self):
        self.datasetDir = os.path.join(os.getcwd(), "data")

        if not os.path.isdir(self.datasetDir):
            # no dataset directory initialized
        else:

    def initializeDirectoriesAndFiles(self):
        # check if data directory is available here
        currentDir = os.getcwd()

        if not os.path.isdir(path)
