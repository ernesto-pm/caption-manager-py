import os
import sys
sys.path.append(os.getcwd())

from modules.epiUtils.epiDirectory import EpiDirectory

def testEpiFile():
    directory = EpiDirectory('C:\\Users\\Ernesto\\Desktop\\datasets\\rr1eDataset')
    dataframe = directory.getDataframeOfFiles()

    print(dataframe['type'])