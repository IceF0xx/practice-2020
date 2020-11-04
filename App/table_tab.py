from PyQt5.QtWidgets import QPushButton

from .tab import Tab
from .table import Table


class TableTab(Tab):
    def __init__(self, table_name, parent=None):
        super(TableTab, self).__init__(table_name, parent)

        self.table = Table(table_name=table_name)

        add_button = QPushButton('+', self)
        add_button.clicked.connect(self.table.add_empty_row)
        self.lay.addWidget(add_button)
        remove_button = QPushButton('-', self)
        remove_button.clicked.connect(self.table.remove_rows)
        self.lay.addWidget(remove_button)

        self.hlay.addWidget(self.table.tv)

    def on_change(self):
        self.table.update_data()
