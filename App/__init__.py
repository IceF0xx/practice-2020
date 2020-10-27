from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QTabWidget, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self, tabs, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()

        self.title = kwargs.get('title', 'Database admin tool')

        self.left = 600
        self.top = 250
        self.width = 500
        self.height = 500

        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tabs = Tabs(self, tabs)
        self.setCentralWidget(self.tabs)

        self.show()


class Tabs(QWidget):
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


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
