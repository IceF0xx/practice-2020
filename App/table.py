from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

from Database.utils import update_table_value


class Table(QAbstractTableModel):
    def __init__(self, data: dict, table_name: str):
        super(Table, self).__init__()
        self.table_name = table_name
        self._data = data['data']
        self._columns = data['columns']

    def data(self, index, role: int = ...):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, role: int = ...):
        return len(self._data)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole:
            if orientation == Qt.Vertical:
                return section
            elif orientation == Qt.Horizontal:
                return self._columns[section]

    def columnCount(self, index: int = ...):
        return len(self._columns)

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        self._data[index.row()][index.column()] = value
        new_data = {'id': self._data[index.row()][0]}
        new_data['new_value'] = value
        new_data['column_name'] = self._columns[index.column()]
        update_table_value(self.table_name, new_data)
        return True

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if index.column() != 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsSelectable
