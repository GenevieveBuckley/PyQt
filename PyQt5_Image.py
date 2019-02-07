import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
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


        self.show()

App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())

