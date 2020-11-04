from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLineEdit

from Database.utils import execute_raw_sql
from .custom_table import CustomTable
from .tab import Tab


class CustomTab(Tab):
    def __init__(self, tab_name, parent=None):
        super(CustomTab, self).__init__(tab_name, parent)
        self.table = None
        self.remove_button = None
        self.add_button = None

        self.textbox = QLineEdit(self)
        self.textbox.setAlignment(Qt.AlignCenter)
        self.textbox.editingFinished.connect(self.on_click)

        self.exec_btn = QPushButton('Execute')
        self.exec_btn.clicked.connect(self.on_click)

        self.hlay.addWidget(self.textbox)
        self.hlay.addWidget(self.exec_btn)

        self.f = True

    def on_click(self):
        self.data = execute_raw_sql(self.textbox.text())

        if self.data.get('error'):
            print(self.data['message'])
            return

        if self.table:
            self.lay.removeWidget(self.table.tv)

        self.table = CustomTable(**self.data)
        self.lay.addWidget(self.table.tv)
