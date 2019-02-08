import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Image"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("Japan.jpg")
        labelImage.setPixmap(pixmap)

        vbox.addWidget(labelImage)

        self.setLayout(vbox)

        check1 = QCheckBox("Channel 1")
        check2 = QCheckBox("Channel 2")
        check3 = QCheckBox("Channel 3")

        vbox.addWidget(check1)
        vbox.addWidget(check2)
        vbox.addWidget(check3)

        self.show()





App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())

