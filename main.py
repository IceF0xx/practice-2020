from PyQt5.QtWidgets import QApplication

import Database as db
from App import MainWindow
from Database.utils import get_table_names

if __name__ == '__main__':
    db.init()  # probably to delete
    app = QApplication([])
    tables = get_table_names()
    window = MainWindow(tabs=tables)
    window.show()
    app.exec_()
