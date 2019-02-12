import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
                             QMainWindow, QMenuBar, QWidget)


class MainWindow(QMainWindow):
    """The outer window to hold everything"""

    def __init__(self):
        """Set up the main window dimension etc"""
        super().__init__()

        self.resize(1024, 768)
        self.title = "Fibsem GUI"
        self.setWindowTitle(self.title)

        self.centre = MainWidget()
        self.setCentralWidget(self.centre)

        self.init_menu_bar()
        self.init_status_bar()

    def init_menu_bar(self):
        """Set up the menu bar"""

        self.menu = QMenuBar()

        self.menu.addMenu("Placeholder1")
        self.menu.addMenu("Placeholder2")
        self.menu.addMenu("Placeholder3")

        self.setMenuBar(self.menu)

    def init_status_bar(self):
        """Set up the status bar"""

        self.statusBar().showMessage('Ready')


class MainWidget(QWidget):
    """The main widget (images and checkboxes etc)"""

    def __init__(self):
        """Testing displaying an image"""
        super().__init__()

        self.init_images()
        self.init_checkboxes()
        self.init_layout()

        self.dummy_variable = 0;

    def init_images(self):
        """Load images"""

        self.image_one = QLabel(self)
        pixmap_one = QPixmap("Japan.jpg")
        self.image_one.setPixmap(pixmap_one)

    def init_checkboxes(self):
        """Create checkboxes"""

        self.checkbox_one = QCheckBox("Placeholder1")
        self.checkbox_one.stateChanged.connect(self.checkbox_do_thing)
        self.checkbox_two = QCheckBox("Placeholder2")
        self.checkbox_two.stateChanged.connect(self.checkbox_do_thing)
        self.checkbox_three = QCheckBox("Placeholder3")
        self.checkbox_three.stateChanged.connect(self.checkbox_do_thing)



    def init_layout(self):
        """Create layout"""
        layout = QGridLayout()

        layout.addWidget(self.image_one, 1, 0, 10, 1)
        layout.addWidget(self.checkbox_one, 1, 2)
        layout.addWidget(self.checkbox_two, 2, 2)
        layout.addWidget(self.checkbox_three, 3, 2)

        self.setLayout(layout)

    def checkbox_do_thing(self, state):
        """just something to make the checkbox do something"""

        self.count = self.dummy_variable

        if state == Qt.Checked:
            print('Checked')
            self.count = self.count + 2
            print(self.count)

        else:
            print('Unchecked')
            self.count = self.count - 1
            print(self.count)

        self.dummy_variable = self.count


    def change_image(self):
        """Further testing of checkbox actions"""



if __name__ == '__main__':
    """If opened as main, run everything"""

    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(App.exec())