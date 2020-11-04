from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from .custom_tab import CustomTab
from .table_tab import TableTab


class Navbar(QWidget):
    def __init__(self, parent, tabs):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)

        self.tabs_list = []
        for tab_name in tabs:
            tab = TableTab(tab_name)
            self.tabs_list.append(tab)
            self.tabs.addTab(tab, f"{tab_name}")

        raw_input_tab = CustomTab('Raw Input')
        self.tabs.addTab(raw_input_tab, 'Raw Input')

        self.tabs_list.append(raw_input_tab)
        self.tabs.currentChanged.connect(lambda i: self.tabs_list[i].on_change())

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
