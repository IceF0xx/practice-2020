from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from .tab import Tab


class Navbar(QWidget):
    def __init__(self, parent, tabs):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)

        for tab_name in tabs:
            tab = Tab(tab_name)
            self.tabs.addTab(tab, f"{tab_name}")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

