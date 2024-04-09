from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStackedWidget, QWidget, QVBoxLayout, QLabel, QMenuBar, QMenu
from functools import partial
from modules.ui.SplashScreen import SplashScreenWidget
from modules.ui.NewDataset import NewDatasetWidget
from enum import Enum

# The indexes are determined by the order we added stuff to the stacked view, we need to be careful with this
class ViewsEnum(Enum):
    SPLASH_SCREEN = 0
    NEW_DATASET = 1
    IMPORT_DIRECTORY = 2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle("Dataset Manager")

        self.viewContainer = QStackedWidget()
        self.setCentralWidget(self.viewContainer)

        self.setupMenu()

        self.viewContainer.addWidget(SplashScreenWidget())
        self.viewContainer.addWidget(NewDatasetWidget(self))

    def setupMenu(self):
        # Setup the menu
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')

        newAction = QAction('New', self)
        newAction.triggered.connect(partial(self.displayView, ViewsEnum.NEW_DATASET.value))
        fileMenu.addAction(newAction)

        importDirectoryAction = QAction('Import Directory', self)
        importDirectoryAction.triggered.connect(partial(self.displayView, ViewsEnum.IMPORT_DIRECTORY.value))
        fileMenu.addAction(importDirectoryAction)

    def displayView(self, withIndex: int):
        print(f"Displaying view: {withIndex}")
        self.viewContainer.setCurrentIndex(withIndex)

    def initUI(self):
        # Create two widgets that can be switched between
        self.first_widget = QWidget()
        self.first_widget_layout = QVBoxLayout()
        self.first_widget_layout.addWidget(QLabel("This is the first window"))
        self.first_widget.setLayout(self.first_widget_layout)

        self.second_widget = QWidget()
        self.second_widget_layout = QVBoxLayout()
        self.second_widget_layout.addWidget(QLabel("This is the second window"))
        self.second_widget.setLayout(self.second_widget_layout)

        # Add widgets to the stacked layout
        self.viewContainer.addWidget(self.first_widget)
        self.viewContainer.addWidget(self.second_widget)