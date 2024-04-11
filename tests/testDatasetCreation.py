import os
import sys
sys.path.append(os.getcwd())

from modules.epiUtils.epiFile import EpiFile
from modules.epiUtils.epiList import EpiList
from modules.controllers.DatasetController import DatasetController
from os.path import expanduser, join

def testCreateEpiFile():
    testDatasetDirectory = join(expanduser("~"), "Desktop", "testDataset", "58dcz8ll29t21.jpg")
    epiFile = EpiFile.fromFilePath(testDatasetDirectory, verifyExistence=True)

    print(epiFile.dict())

def testEpiList():
    testDatasetDirectory = join(expanduser("~"), "Desktop", "testDataset", "58dcz8ll29t21.jpg")
    epiFile = EpiFile.fromFilePath(testDatasetDirectory, verifyExistence=True)

    epiList = EpiList()
    epiList.append(epiFile)
    epiList.append(epiFile)

    df = epiList.toDataframe()
    for i, row in df.iterrows():
        print(row)

    fileslist: EpiList[EpiFile] = EpiList.fromDataframe(df, EpiFile)
    for element in fileslist:
        print(element)

def testDatasetCreation():
    testDatasetDirectory = join(expanduser("~"), "Desktop", "testDataset")
    datasetController = DatasetController()

    datasetController.newDataset(name="Hello world", description="N/A", baseDirPath=testDatasetDirectory)

def testDatasetDBCreation():
    from modules.dbModels.Dataset import Dataset

    dataset = Dataset(name="Hello world", description="My description", directoryAbsPath="/lolaxo")
    print(dataset.save())

def testGetAllDatasets():
    from modules.dbModels.Dataset import Dataset

    for dataset in Dataset.listAll():
        print(dataset)