import PyQt5.QtWidgets as widgets
from PyQt5.QtCore import Qt
from MainTable import MainTable 
import datetime as dt

class MainWindow(widgets.QWidget):
    TABLE_ROWS = 1
    TABLE_COLS = 7
    HEADER_LABELS = ['Ebay Order #', 'Date', 'Time', 'Name', 'Address', 'Amount / £', 'Status']

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
        self.table = MainTable(self.TABLE_ROWS, self.TABLE_COLS, self.HEADER_LABELS)
        topLayout.addWidget(self.table)
    
    def make_top_toolbar(self):
        self.top_toolbar = widgets.QToolBar()
        
        get_orders_action = widgets.QAction("Get orders", self)
        get_orders_action.triggered.connect(self.get_orders)
        
        self.info_label = widgets.QLabel(" | Ready", self)
        
        self.top_toolbar.addAction(get_orders_action)
        self.top_toolbar.addWidget(self.info_label)
        # self.top_toolbar.actionTriggered[widgets.QAction].connect(self.get_orders)
        
    def get_orders(self):
        """
        Request the orders through the ebay getOrders Sell API call
        
        Arguments:
            action: 
        """
        ########### placeholder to fill in fake order details #############
        orders = [{'order_id':1236835171, 'datetime':dt.datetime.now(), 'name':'John Doe', 'address':'31 Address lane, Somewhere, S32 1HJ', 'amount':10, 'status':'New'}, 
                    {'order_id':4856159381, 'datetime':dt.datetime.now(), 'name':'Jane Doe', 'address':'50 Address lane, Somewhere, S32 1IJ', 'amount':3, 'status':'Processing'}]
        ###################################################################
        

        
        #set the size of the table to the number of orders
        if len(orders) != self.table.rowCount():
            self.table.setRowCount(len(orders))

        #fill in the orders
        statuses = []
        for r, order in enumerate(orders):
            statuses.append(order['status'])
        
            self.table.setItem(r,0,widgets.QTableWidgetItem('{}'.format(order['order_id'])))
            self.table.setItem(r,1,widgets.QTableWidgetItem('{}'.format(order['datetime'].date())))
            self.table.setItem(r,2,widgets.QTableWidgetItem('{0:02d}:{1:02d}:{2:02d}'.format(order['datetime'].hour, order['datetime'].minute, order['datetime'].second)))
            self.table.setItem(r,3,widgets.QTableWidgetItem(order['name']))
            self.table.setItem(r,4,widgets.QTableWidgetItem(order['address']))
            self.table.setItem(r,5,widgets.QTableWidgetItem('{}'.format(order['amount'])))
            self.table.setItem(r,6,widgets.QTableWidgetItem(order['status']))
        
        #set the info label
        if "Overdue" in statuses:
            self.info_label.setText('| Found overdue orders')
        elif "Processing" in statuses:
            self.info_label.setText('| Found orders being processed')
        elif "New" in statuses:
            self.info_label.setText('| Found new orders')
        else:
            self.info_label.setText('| All orders complete')
        
        
        
        
        
        
        
        
   