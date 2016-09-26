import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4 import QtCore
from PyQt4.QtGui import *
from constants import *
from add_task import Add_New_Task

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class Principal_View(QtGui.QWidget):
    def __init__(self):
        super(Principal_View, self).__init__()
        self.screenGeometry = QtGui.QApplication.desktop().availableGeometry()
        # Initialize Layout

        # Signal to check total
        self.central_layout = QtGui.QGridLayout()
        self.control_singleton = False

        self.product_group = QtGui.QGroupBox(str("Tareas"), self)
        self.search_group = QtGui.QGroupBox(str("Tipos de Tareas"), self)

        self.central_layout.addWidget(self.search_group, 0, 0)
        self.central_layout.addWidget(self.product_group, 1, 0)

        self.initialize_results_group()
        self.initialize_product_group()

        self.setLayout(self.central_layout)

    def initialize_results_group(self):
        self.layout_task = QtGui.QFormLayout()
        self.done_task = QRadioButton("Tareas Terminadas")
        self.pending_task = QRadioButton("Tareas Pendiente")
        self.pending_task.setChecked(True)
        self.done_task.toggled.connect(self.refresh_table)
        self.pending_task.toggled.connect(self.refresh_table)

        self.layout_task.addRow(self.pending_task, self.done_task)
        self.search_group.setLayout(self.layout_task)

    def add_task(self):
        if(self.control_singleton):
            QMessageBox.warning(self, 'Error', ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
        else:
            self.control_singleton = True
            window = Add_New_Task().exec_()        
        self.control_singleton = False

    def modify_product(self):
        if(self.control_singleton):
            QMessageBox.warning(self, 'Error', ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
        else:
            self.control_singleton = True
            button = qApp.focusWidget()
            index = self.table_items.indexAt(button.pos())
        #if index.isValid():
        #window = Modify_Product(self.query[index.row()], session).exec_()

        self.control_singleton = False
        self.refresh_table()

    def initialize_product_group(self):
        self.layout_line = QtGui.QFormLayout()
        #Creating table
        self.table_items = QtGui.QTableWidget(self)
        self.table_items.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_items.setRowCount(0)

        self.table_items.setColumnCount(6)
        self.table_items.setHorizontalHeaderLabels(['Actividad','Nombre', 
                                        'Fecha Inicio', 'Fecha Fin', 
                                        'Detalle', 'Modificar'])


        header = self.table_items.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)
        self.stringRow = ''

        self.table_items.setVerticalHeaderLabels(QString(self.stringRow).split(','))
        #addin table with the query
            
        self.button_add_task = QtGui.QPushButton('Agregar Tarea')
        self.button_add_task.clicked.connect(self.add_task)
        
        #self.layout_line.addRow(self.label_search, self.edit_search)
        self.layout_line.addRow(self.table_items)
        self.layout_line.addRow(self.button_add_task)
        self.product_group.setLayout(self.layout_line)
        self.refresh_table()

    def clear_table(self):
        self.table_items.clear();
        self.table_items.setRowCount(0);
        self.table_items.setColumnCount(6)
        self.table_items.setHorizontalHeaderLabels(['Actividad','Nombre', 
                                        'Fecha Inicio', 'Fecha Fin', 
                                        'Detalle', 'Modificar'])
    def refresh_table(self):
        self.clear_table()
        conn = connection_data_base()
        session = conn.cursor()

        if self.done_task.isChecked():
            session.execute("SELECT * FROM " +TABLE_TASK+ " WHERE " + KEY_T_FINISHED +"=1" )
            self.query = session.fetchall()
        elif self.pending_task.isChecked():
            session.execute("SELECT * FROM " +TABLE_TASK+ " WHERE " + KEY_T_FINISHED +"=0" )
            self.query = session.fetchall()
        session.close()
        self.table_items.setRowCount(len(self.query))
        self.stringRow = ''
        for task in range(len(self.query)):
            self.table_items.setItem(task, 0,
                                     QtGui.QTableWidgetItem(str(self.query[task][1])))
            self.table_items.setItem(task, 1,
                                     QtGui.QTableWidgetItem(str(self.query[task][2])))
            self.table_items.setItem(task, 2,
                                     QtGui.QTableWidgetItem(str(self.query[task][3])))
            self.table_items.setItem(task, 3,
                                     QtGui.QTableWidgetItem(str(self.query[task][4])))
            self.table_items.setItem(task, 4,
                                     QtGui.QTableWidgetItem(str(self.query[task][5])))
            buttonModify = QtGui.QPushButton()
            buttonModify.clicked.connect(self.modify_product)
            buttonModify.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            #buttonModify.setIcon(QtGui.QIcon('icons/Icon_edit.png'))
            self.table_items.setCellWidget(task, 5, buttonModify)
            self.stringRow = self.stringRow + str(task+1) + ','

        self.table_items.setVerticalHeaderLabels(QString(self.stringRow).split(','))
    