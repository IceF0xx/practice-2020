from PyQt5 import QtWidgets
from .table import Table
from Database.utils import fetch_data_from_table


class Tab(QtWidgets.QWidget):
    def __init__(self, table_name, parent=None):
        super(Tab, self).__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        lay.addLayout(hlay)
        lay.addStretch()

        self.table = QtWidgets.QTableView()

        data = fetch_data_from_table(table_name)

        self.model = Table(data)
        self.table.setModel(self.model)
        # self.table.setHorizontalHeaderLabels(data['columns'])

        hlay.addWidget(self.table)




