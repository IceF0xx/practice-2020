from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton

from .table import Table


class Tab(QtWidgets.QWidget):
    def __init__(self, tab_name, parent=None):
        super(Tab, self).__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        lay.setAlignment(Qt.AlignCenter)
        lay.addLayout(hlay)
        lay.addStretch()

        self.table = Table(table_name=tab_name)

        add_button = QPushButton('+', self)
        add_button.clicked.connect(self.table.add_empty_row)
        lay.addWidget(add_button)
        remove_button = QPushButton('-', self)
        remove_button.clicked.connect(self.table.remove_rows)
        lay.addWidget(remove_button)

        hlay.addWidget(self.table.tv)
