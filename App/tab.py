from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHeaderView

from Database.utils import fetch_data_from_table
from .table import Table


class Tab(QtWidgets.QWidget):
    def __init__(self, table_name, parent=None):
        super(Tab, self).__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        lay.addLayout(hlay)
        lay.addStretch()

        self.table = QtWidgets.QTableView()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.data = fetch_data_from_table(table_name)

        self.model = Table(self.data, table_name)
        self.table.setModel(self.model)
        hlay.addWidget(self.table)
