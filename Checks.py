import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
                             QMenuBar, QWidget)
from skimage import io


class MainWindow(QWidget):
    """The main display window"""

    def __init__(self):
        """Set up the main window dimensions etc"""
        super().__init__()
        self.resize(1024, 768)
        self.title = "Image and checkboxes"

        self.initwindow()
#        self.initMenuBar()
#        self.loadPicChannels()
        self.initLabels()
        self.initCheckboxes()
        self.initLayout()

    def initwindow(self):

        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)

#    def initMenuBar(self):
#
#        menu = QMenuBar()
#        menu.addMenu("Hi")
#        menu.addMenu("Bye")
#        self.setMenuBar(menu)

#    def loadPicChannels(self):
#        self.picture = io.imread("Japan.jpg")
#        self.pic1 = self.picture[:, :, 0]
#        io.imshow(self.pic1)
#        io.show()
#        self.pic2 = self.picture[:, :, 1]
#        io.imshow(self.pic2)
#        io.show()
#        self.pic3 = self.picture[:, :, 2]
#        io.imshow(self.pic3)
#        io.show()

    def initLabels(self):
        self.labelImage = QLabel(self)
#        japan = io.imread("Japan.jpg")
        pixmap = QPixmap("Japan.jpg")
        self.labelImage.setPixmap(pixmap)

    def initCheckboxes(self):
        self.checkbox1 = QCheckBox("Channel 1")
        self.checkbox2 = QCheckBox("Channel 2")
        self.checkbox3 = QCheckBox("Channel 3")

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.labelImage, 0, 0, 10, 1)

 #       layout.addWidget(self.labelpic, 0, 0, 10, 1)
        layout.addWidget(self.checkbox1, 0, 2)
        layout.addWidget(self.checkbox2, 1, 2)
        layout.addWidget(self.checkbox3, 2, 2)

        self.setLayout(layout)


if __name__ == '__main__':


    App = QApplication(sys.argv)
#    App.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(App.exec())
