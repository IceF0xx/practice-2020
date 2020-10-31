from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from .navbar import Navbar
from .tab import Tab


class MainWindow(QWidget):
    def __init__(self, tabs, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self._tabs = tabs
        self.layout = QVBoxLayout(self)

        self.setMinimumSize(QSize(480, 80))

        self.navbar = Navbar(self, self._tabs)
        self.layout.addWidget(self.navbar)

        self.show()
