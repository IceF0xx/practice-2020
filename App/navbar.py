from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget


class Bar(QWidget):
    def __init__(self, parent, tables):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)

        for table in tables:
            tab = QWidget()
            self.tabs.addTab(tab, f"{table}")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

