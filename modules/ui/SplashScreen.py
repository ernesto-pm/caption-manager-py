from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel

class SplashScreenWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(SplashScreenWidget, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()

        # Adding the layout elements
        layout.addWidget(QLabel("Splash Screen"))
        self.setLayout(layout)
