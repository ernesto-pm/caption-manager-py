from tinydb import TinyDB, Query
from tinydb.table import Table
from modules.dbModels import Dataset
from modules.dbModels import DatasetFile
from modules.epiUtils.epiDirectory import EpiDirectory
from modules.epiUtils.epiFile import EpiFile
from modules.epiUtils.epiList import EpiList
from typing import List, Optional
from os.path import isfile, join
from os import listdir
import os

class DatasetController(object):
    db: TinyDB
    datasetsTable: Table

    def __init__(self, overrideDBPath: Optional[str] = None):
        dbPath = os.path.join(os.getcwd(), "data", "db.json")
        if overrideDBPath:
            dbPath = overrideDBPath

        self.db = TinyDB(dbPath)
        self.datasetsTable = self.db.table("dataset")
        self.datasetFilesTable = self.db.table("datasetFile")

    def getAllDatasets(self) -> List[Dataset]:
        typedDatasets: List[Dataset] = []
        for dataset in self.datasetsTable.all():
            typedDatasets.append(Dataset.parse_obj(dataset))

        return typedDatasets

    def newDataset(self, name: str, description: str, baseDirPath: str):
        datasetSourceDir = EpiDirectory.fromFilePath(directoryAbsPath=baseDirPath)
        filesEpiList = datasetSourceDir.getListOfEpiFiles()

        # Only keep images and text
        filesDataframe = filesEpiList.toDataframe()
        filesDataframe = filesDataframe.loc[filesDataframe['fileType'].isin(['image', 'text'])]

        filesList: EpiList[EpiFile] = EpiList.fromDataframe(filesDataframe, EpiFile)
        for item in filesList:
            print(item.fileType)

        # Get back our filtered list of epifiles, so we can do stuff with it
        #
        #for file in filesList:
            #print(file.filenameWithExtension)

