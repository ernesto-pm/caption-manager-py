from modules.dbModels import Dataset, DatasetFile
from modules.epiUtils.epiDirectory import EpiDirectory
from modules.epiUtils.epiFile import EpiFile
from modules.epiUtils.epiList import EpiList
from typing import List

class DatasetController(object):
    def newDataset(self, name: str, description: str, baseDirPath: str):
        # Load files in directory
        print("Loading files in directory...")
        datasetSourceDir = EpiDirectory.fromFilePath(directoryAbsPath=baseDirPath)
        filesEpiList = datasetSourceDir.getListOfEpiFiles()

        # Only keep images and text
        print("Keeping images and text...")
        filesDataframe = filesEpiList.toDataframe()
        filesDataframe = filesDataframe.loc[filesDataframe['fileType'].isin(['image', 'text'])]

        # Create the things we are going to store in the database
        print("Inserting new dataset...")
        newDatasetID = Dataset(name=name, description=description, directoryAbsPath=baseDirPath).save()

        # Get back a list of all files, transform them into dataset files
        print("Transform epifiles...")
        filesList: EpiList[EpiFile] = EpiList.fromDataframe(filesDataframe, EpiFile)
        datasetFiles: List[DatasetFile] = [
            DatasetFile(datasetID=newDatasetID,
                        filenameWithExtension=file.filenameWithExtension,
                        filenameWithoutExtension=file.filenameWithoutExtension,
                        fileExtension=file.extension,
                        absPath=file.absFilePath,
                        type=file.fileType,
                        ignored=False) for file in filesList
        ]

        print("Inserting dataset files in database...")
        newFilesIDs = DatasetFile.insertMany(datasetFiles)
        print(newFilesIDs)
