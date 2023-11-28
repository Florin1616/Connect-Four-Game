from texttable import Texttable

class ConnectFour:
    def __init__(self, rows, columns: int, data):
        self._rows = rows
        self._columns = columns
        self._data = data

    def __str__(self):
        t = Texttable()
        header = []
        for i in range(self._columns):
            header.append(i+1)
        t.header(header)
        for r in range(self._rows):
            t.add_row(self._data[r])
        return t.draw()
