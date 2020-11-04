from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Tab(QtWidgets.QWidget):
    def __init__(self, tab_name, parent=None):
        super(Tab, self).__init__(parent)
        self.tab_name = tab_name
        self.lay = QtWidgets.QVBoxLayout(self)
        self.hlay = QtWidgets.QHBoxLayout()
        self.lay.setAlignment(Qt.AlignCenter)
        self.lay.addLayout(self.hlay)
        self.lay.addStretch()

    def on_change(self):
        pass
