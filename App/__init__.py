from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .navbar import Navbar
from .table import Table


class MainWindow(QWidget):
    def __init__(self, tabs, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self._tabs = tabs
        self.layout = QVBoxLayout(self)
        self.layout.setStretch(0, 1)
        self.setMinimumSize(QSize(800, 500))

        self.setFixedHeight(500)
        self.navbar = Navbar(self, self._tabs)
        self.layout.addWidget(self.navbar)

        self.show()
