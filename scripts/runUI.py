import os
import sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

def initializeConfigFiles():
    dataDir = os.path.join(os.getcwd(), "data")
    databaseFilePath = os.path.join(dataDir, "db.json")

    # Check if our 'data' directory is initalized, we create it if not
    if not os.path.isdir(dataDir):
        os.mkdir(dataDir)

    # Check if our 'database' has been initialised, we initialize it if not
    if not os.path.exists(databaseFilePath):
        open(databaseFilePath, 'w').close()

if __name__ == "__main__":
    # Initalize the config files
    initializeConfigFiles()

    app = QApplication(sys.argv)

    from modules.ui.MainUIQt import MainWindow
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
