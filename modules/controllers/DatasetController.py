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
    def newDataset(self, name: str, description: str, baseDirPath: str):
        # Load files in directory
        datasetSourceDir = EpiDirectory.fromFilePath(directoryAbsPath=baseDirPath)
        filesEpiList = datasetSourceDir.getListOfEpiFiles()

        # Only keep images and text
        filesDataframe = filesEpiList.toDataframe()
        filesDataframe = filesDataframe.loc[filesDataframe['fileType'].isin(['image', 'text'])]

        # Create the things we are going to store in the databse
        newDatasetID = Dataset(name=name, description=description, directoryAbsPath=baseDirPath).save()

        # Get back a list of epi files, we want to transform this into
        filesList: EpiList[EpiFile] = EpiList.fromDataframe(filesDataframe, EpiFile)
        for file in filesList:
            pass

        # Get back our filtered list of epifiles, so we can do stuff with it
        #
        #for file in filesList:
            #print(file.filenameWithExtension)

