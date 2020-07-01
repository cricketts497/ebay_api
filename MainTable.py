import PyQt5.QtWidgets as widgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class MainTable(widgets.QTableWidget):
    STATUS_SETTINGS = {"New":QColor(0,0,255,100), "Processing":QColor(255,165,0,100), "Complete":QColor(0,255,0,100), "Overdue":QColor(255,0,0,100)}
    def __init__(self, rows, cols, headerLabels):
        """
        Set the size of the table, create a right click menu, set up the formatting connections
        
        Arguments:
            rows: Number of rows in the table
            cols: Number of columns in the table
            headerLabels: column names to place at the top of the table
        """
        super().__init__()
        
        self.setRowCount(rows)
        self.setColumnCount(cols)
        
        self.setHorizontalHeaderLabels(headerLabels)
        
        self.setSizeAdjustPolicy(
            widgets.QAbstractScrollArea.AdjustToContents)
            
        #create the menu that opens on right click
        self.table_right_click_menu = widgets.QMenu(self)
        order_details_action = widgets.QAction("Open order details", self)
        order_details_action.triggered.connect(self.open_order_details)
        self.table_right_click_menu.addAction(order_details_action)
        
        #Open the menu on right click on table
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_table_menu)
        
        #If the status is 'completed', change row colour to green
        self.cellChanged[int, int].connect(self.setOrderColour)
        
        #fill all cells with space so have items
        #########################################
        for r in range(self.rowCount()):
            for c in range(self.columnCount()):
                self.setItem(r,c,widgets.QTableWidgetItem(' '))
        #########################################
            
    def open_table_menu(self, pos):
        #Open the table right-click menu at the mouse position
        action = self.table_right_click_menu.exec_(self.mapToGlobal(pos))
        
    def open_order_details(self):
        #Get the order belonging to the selected row
        item = self.item(self.currentRow(), 0)
        try:
            order_id = int(item.text())
        except (ValueError, TypeError):
            order_id = 0
            
        print(order_id)
        
    def setOrderColour(self, row, col):
        """
        Set the Background colour of the order row based on the "Status" column value and the STATUS_SETTINGS dict
        
        Arguments:
            row: row index of the changed cell
            col: column index of the changed cell
        """
        if col == self.columnCount()-1:#status column
            status = self.item(row, col).text()
            
            if status in self.STATUS_SETTINGS.keys():
                for c in range(self.columnCount()):
                    self.item(row, c).setBackground(self.STATUS_SETTINGS[status])
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        