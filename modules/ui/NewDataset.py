from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFormLayout, QLineEdit

class NewDatasetWidget(QtWidgets.QWidget):
    datasetName = QLineEdit()

    def __init__(self, *args, **kwargs):
        super(NewDatasetWidget, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Adding the layout elements
        layout.addWidget(QLabel("New Dataset"))

    def createForm(self):
        formLayout = QFormLayout()

        formLayout.addRow(QLabel("Name"), self.datasetName)
