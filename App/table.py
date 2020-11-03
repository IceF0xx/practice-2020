from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView

from Database.utils import fetch_data_from_table
from .tablemodel import TableModel


class Table(QtWidgets.QWidget):
    def __init__(self, table_name, parent=None):
        super(Table, self).__init__(parent)

        self.tv = QtWidgets.QTableView()
        self.tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.data = fetch_data_from_table(table_name)

        self.model = TableModel(self.data, table_name)

        self.tv.setModel(self.model)

    def remove_rows(self):
        self.model.remove_rows(self.tv.selectionModel().selectedRows())
        self.tv.model().layoutChanged.emit()

    def add_empty_row(self):
        self.model.add_empty_row()
        self.tv.model().layoutChanged.emit()
