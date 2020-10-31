import typing

from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore

class Table(QAbstractTableModel):
    def __init__(self, data: dict):
        super(Table, self).__init__()
        self._data = data['data']
        self._columns = data['columns']

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            if orientation == Qt.Vertical:
                return section
            elif orientation == Qt.Horizontal:
                return self._columns[section]

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._columns)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            print('click')

        print('boop')