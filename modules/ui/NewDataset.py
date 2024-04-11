from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFormLayout, QLineEdit, QFileDialog, QPushButton, QHBoxLayout, QMainWindow
from modules.controllers import DatasetController
from functools import partial

class NewDatasetWidget(QtWidgets.QWidget):
    """
    A widget for creating a new dataset from a source directory
    """
    mainWindow: QMainWindow

    datasetName: QLineEdit
    datasetDescription: QLineEdit
    sourceDirectory: str

    datasetController: DatasetController

    def __init__(self, mainWindow: QMainWindow, *args, **kwargs):
        """
        Initializes the widget, sets up the UI layout and connects signals to slots
        :param args:
        :param kwargs:
        """
        super(NewDatasetWidget, self).__init__(*args, **kwargs)
        self.mainWindow = mainWindow

        self.datasetController = DatasetController()

        # Initialize initial instance variables and connect the listeners
        self.datasetName = QLineEdit()
        self.datasetName.textChanged.connect(self.validateForm)
        self.datasetDescription = QLineEdit()
        self.datasetDescription.textChanged.connect(self.validateForm)
        self.sourceDirectory = ""

        # Create layout and add the form
        layout = QVBoxLayout()

        layout.addLayout(self.createHeader())
        layout.addLayout(self.createForm())
        self.setLayout(layout)

    def createHeader(self) -> QHBoxLayout:
        """
        Creates the header of the new dataset page, with a button to go back
        :return:
        """
        layout = QHBoxLayout()

        backButton = QPushButton("Cancel")
        backButton.clicked.connect(partial(self.mainWindow.displayView, 0))

        layout.addWidget(backButton)

        return layout

    def createForm(self) -> QFormLayout:
        """
        Creates the form layout with dataset name, description, and source directory.

        :return: The form layout with all widgets added.
        """
        formLayout = QFormLayout()

        # Simple form inputs for the dataset attributes
        formLayout.addRow(QLabel("Dataset Name"), self.datasetName)
        self.datasetName.textChanged.connect(self.validateForm)
        formLayout.addRow(QLabel("Dataset Description"), self.datasetDescription)

        # Load directory button
        self.loadDirectoryButton = QPushButton("...")
        self.loadDirectoryButton.clicked.connect(self.showLoadDirectory)
        formLayout.addRow(QLabel("Source directory"), self.loadDirectoryButton)

        # Submit button
        self.submitButton = QPushButton("Create")
        self.submitButton.setEnabled(False)  # Initially disabled
        self.submitButton.clicked.connect(self.handleSubmit)
        formLayout.addWidget(self.submitButton)

        return formLayout

    def handleSubmit(self):
        """
        Handles the submission of the form, effectively adding a new dataset to the bag of datasets.
        """
        self.datasetController.newDataset(
            name=self.datasetName.text(),
            description=self.datasetDescription.text(),
            baseDirPath=self.sourceDirectory
        )

        self.mainWindow.displayView(0)

    def showLoadDirectory(self):
        """
        Opens a dialog for the user to select the source directory. Updates the source directory button label
        and validates the form upon directory selection.
        """
        file = QFileDialog.getExistingDirectory(self, "Load directory...")
        sourceDirectory = str(file)

        self.loadDirectoryButton.setText(sourceDirectory)
        self.sourceDirectory = sourceDirectory
        self.validateForm()

    def validateForm(self):
        """
        Validates the form fields to enable the submit button when all required information is filled out.
        Checks dataset name, dataset description, and whether a source directory has been selected.
        """
        if self.datasetName.text() and self.datasetDescription.text() and self.sourceDirectory:
            self.submitButton.setEnabled(True)
        else:
            self.submitButton.setEnabled(False)