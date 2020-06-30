import PyQt5.QtWidgets as widgets
from PyQt5.QtCore import Qt

class MainWindow(widgets.QWidget):
    TABLE_ROWS = 3
    TABLE_COLS = 6
    HEADER_LABELS = ['Ebay Order #', 'Date', 'Time', 'Name', 'Address', 'Amount / £']

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
    
        #top bar title
        self.setWindowTitle("Ebay comms.")
    
        #Set the main layout for the app
        topLayout = widgets.QVBoxLayout()
        self.setLayout(topLayout)
        
        #Create the top button bar
        self.make_top_toolbar()
        topLayout.addWidget(self.top_toolbar)
        
        #Create the main table object
        self.make_table(self.TABLE_ROWS, self.TABLE_COLS, self.HEADER_LABELS)
        topLayout.addWidget(self.table)
    
    def make_top_toolbar(self):
        self.top_toolbar = widgets.QToolBar()
        
        self.top_toolbar.addAction("Get orders")
    
    def make_table(self, rows, cols, headerLabels):
        self.table = widgets.QTableWidget()
        
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        
        self.table.setHorizontalHeaderLabels(headerLabels)
        
        self.table.setSizeAdjustPolicy(
            widgets.QAbstractScrollArea.AdjustToContents)
            
        #create the menu that opens on right click
        self.table_right_click_menu = widgets.QMenu(self)
        order_details_action = widgets.QAction("Open order details", self)
        order_details_action.triggered.connect(self.open_order_details)
        self.table_right_click_menu.addAction(order_details_action)
        
        #Open the menu on right click on table
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.open_table_menu)
        
            
    def open_table_menu(self, pos):
        action = self.table_right_click_menu.exec_(self.table.mapToGlobal(pos))
        
    def open_order_details(self):
        order_id = int(self.table.item(self.table.currentRow(), 0).text())
        
        print(order_id)
        
        