from .table import Table


class CustomTable(Table):
    def __init__(self, tablename, data, parent=None):
        super(CustomTable, self).__init__(tablename, parent)
        self.update_data(data)
