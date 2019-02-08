from PyQt5.QtWidgets import (QApplication, QMenuBar, QLabel, QWidget,
                             QGridLayout, QCheckBox)
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Image and checkboxes"
        self.left = 100
        self.top = 100
        self.width = 100
        self.height = 100

        self.initWindow()
#        self.initMenuBar()
        self.initLabels()
        self.initCheckboxes()
        self.initLayout()


    def initWindow(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

#    def initMenuBar(self):
#
#        menu = QMenuBar()
#        menu.addMenu("Hi")
#        menu.addMenu("Bye")
#        self.setMenuBar(menu)

    def initLabels(self):
        self.labelImage = QLabel(self)
        pixmap = QPixmap("Japan.jpg")
        self.labelImage.setPixmap(pixmap)

    def initCheckboxes(self):
        self.checkbox1 = QCheckBox("Channel 1")
        self.checkbox2 = QCheckBox("Channel 2")
        self.checkbox3 = QCheckBox("Channel 3")

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.labelImage, 0, 0, 10, 1)

        layout.addWidget(self.checkbox1, 0, 2)
        layout.addWidget(self.checkbox2, 1, 2)
        layout.addWidget(self.checkbox3, 2, 2)

        self.setLayout(layout)


if __name__ == '__main__':

    import sys
    App = QApplication(sys.argv)
#    App.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(App.exec())
