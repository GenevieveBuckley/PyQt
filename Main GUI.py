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
        self.init_checkbox_funcs()
        self.init_checkboxes()
        self.init_layout()

        self.dummy_variable = 0

    def init_images(self):
        """Load images"""

        self.image_one = QLabel(self)
        pixmap_one = QPixmap("Images\Japan.jpg")
        self.image_one.setPixmap(pixmap_one)

    def init_checkbox_funcs(self):
        """Set up the functionality of the buttons"""

        self.checkbox_one_func = self.checkbox_closure(1)
        self.checkbox_two_func = self.checkbox_closure(2)
        self.checkbox_three_func = self.checkbox_closure(4)

    def init_checkboxes(self):
        """Create checkboxes"""

        self.checkbox_one = QCheckBox("Placeholder1")
        self.checkbox_one.stateChanged.connect(self.checkbox_one_func)

        self.checkbox_two = QCheckBox("Placeholder2")
        self.checkbox_two.stateChanged.connect(self.checkbox_two_func)

        self.checkbox_three = QCheckBox("Placeholder3")
        self.checkbox_three.stateChanged.connect(self.checkbox_three_func)

    def init_layout(self):
        """Create layout"""
        layout = QGridLayout()

        layout.addWidget(self.image_one, 1, 0, 10, 1)
        layout.addWidget(self.checkbox_one, 1, 2)
        layout.addWidget(self.checkbox_two, 2, 2)
        layout.addWidget(self.checkbox_three, 3, 2)

        self.setLayout(layout)

    def checkbox_closure(self, n):
        """Closure to construct button functionality"""

        def closure(state):
            """Actual implementation of functionality"""

            self.count = self.dummy_variable

            if state == Qt.Checked:
                print('Checked')
                self.count = self.count + n
                print(self.count)

            else:
                print('Unchecked')
                self.count = self.count - n
                print(self.count)

            self.dummy_variable = self.count
            self.update_image()

        return closure

    def update_image(self):
        """Further testing of checkbox actions"""

        if self.dummy_variable == 0:
            pixmap_one = QPixmap("Images\Japan.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 1:
            pixmap_one = QPixmap("Images\_1.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 2:
            pixmap_one = QPixmap("Images\_2.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 3:
            pixmap_one = QPixmap("Images\_3.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 4:
            pixmap_one = QPixmap("Images\_4.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 5:
            pixmap_one = QPixmap("Images\_5.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 6:
            pixmap_one = QPixmap("Images\_6.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()
        elif self.dummy_variable == 7:
            pixmap_one = QPixmap("Images\_7.jpg")
            self.image_one.setPixmap(pixmap_one)
            self.init_layout()


if __name__ == '__main__':
    """If opened as main, run everything"""

    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(App.exec())