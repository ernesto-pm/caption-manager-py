from modules.dbModels import Dataset
from modules.epiUtils.epiDirectory import EpiDirectory
from modules.epiUtils.epiFile import EpiFile
from modules.epiUtils.epiList import EpiList

class DatasetController(object):
    def newDataset(self, name: str, description: str, baseDirPath: str):
        # Load files in directory
        datasetSourceDir = EpiDirectory.fromFilePath(directoryAbsPath=baseDirPath)
        filesEpiList = datasetSourceDir.getListOfEpiFiles()

        # Only keep images and text
        filesDataframe = filesEpiList.toDataframe()
        filesDataframe = filesDataframe.loc[filesDataframe['fileType'].isin(['image', 'text'])]

        # Create the things we are going to store in the database
        newDatasetID = Dataset(name=name, description=description, directoryAbsPath=baseDirPath).save()

        # Get back a list of all files
        filesList: EpiList[EpiFile] = EpiList.fromDataframe(filesDataframe, EpiFile)
        for file in filesList:
            pass

        # Get back our filtered list of epifiles, so we can do stuff with it
        #
        #for file in filesList:
            #print(file.filenameWithExtension)

