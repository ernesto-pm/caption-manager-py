from modules.epiUtils import ensureFileExists, fileExists
from typing import Optional

class EpiFile(object):
    absolutePath: str
    

    def __init__(self, filepath: str, verifyExistence: bool = True):
        if verifyExistence:
            ensureFileExists(filepath)






