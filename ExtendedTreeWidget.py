
from PyQt4.QtGui import *

class MyTreeWidgetItem(QTreeWidgetItem):
    def __lt__( self, other ):
        if ( not isinstance(other, MyTreeWidgetItem) ):
            return super(MyTreeWidgetItem, self).__lt__(other)

        tree = self.treeWidget()
        if ( not tree ):
            column = 0
        else:
            column = tree.sortColumn()

        return self.sortData(column) < other.sortData(column)

    def __init__( self, *args ):
        super(MyTreeWidgetItem, self).__init__(*args)
        self._sortData = {}

    def sortData( self, column ):
        return self._sortData.get(column, self.text(column))

    def setSortData( self, column, data ):
        self._sortData[column] = data