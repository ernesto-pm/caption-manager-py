import os
import sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    from modules.ui.MainUIQt import MainWindow
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
