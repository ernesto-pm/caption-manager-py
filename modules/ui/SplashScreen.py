from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QListWidgetItem
from modules.controllers.DatasetController import DatasetController
from modules.dbModels.Dataset import Dataset

class SplashScreenWidget(QtWidgets.QWidget):
    datasetController: DatasetController

    def __init__(self, *args, **kwargs):
        super(SplashScreenWidget, self).__init__(*args, **kwargs)
        self.datasetController = DatasetController()

        layout = QVBoxLayout()

        # Adding the layout elements
        self.listWidget = QListWidget()

        layout.addWidget(self.listWidget)
        self.setLayout(layout)
        
        self.refreshDatasets()

    def refreshDatasets(self):
        self.listWidget.clear()

        datasets = Dataset.listAll()
        for dataset in datasets:
            item = QListWidgetItem(dataset.name)
            self.listWidget.addItem(item)

