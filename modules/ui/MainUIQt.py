import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStackedWidget, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.viewContainer = QStackedWidget()
        self.setCentralWidget(self.viewContainer)

        self.viewContainer.addWidget(self.buildSplashScreen())

        # Add widgets (consider these as individual "windows") to the stacked layout
        #self.initUI()

    def buildSplashScreen(self):
        splashScreen = QWidget()

        # Build the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Splash Screen"))

        # code for adding a toolbar
        menuBar = self.menuBar()
        fileMenu = QtWidgets.QMenu("&File", self)

        # Adding the "New Dataset" action to the "File" menu
        self.newDatasetAction = QAction(self)
        self.newDatasetAction.setText("&New Dataset")
        fileMenu.addAction(self.newDatasetAction)


        splashScreen.setLayout(layout)

        return splashScreen

    def displayView(self, withIndex: int):
        self.viewContainer.setCurrentIndex(withIndex)

    def newDataset(self):
        print("lolaxo")

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

        # Setup the menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # Add actions to the menu
        newAct = QAction('New', self)
        newAct.triggered.connect(self.display_second_window)
        fileMenu.addAction(newAct)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())