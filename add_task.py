import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from constants import *
from datetime import datetime

class Add_New_Task(QDialog):
    def __init__(self, parent = None):
        #QDialog.__init__(self, parent)
        super(Add_New_Task, self).__init__(parent)

        self.acceptButton = QPushButton("Crear Producto", self)
        self.cancelButton = QPushButton("Cancelar")

        activity = QLabel(KEY_T_ID_A)
        name = QLabel(KEY_T_NAME)
        detail = QLabel(KEY_T_DESCRIPTION)
        begin_date = QLabel(KEY_T_MOD_DATETIME)
        end_date = QLabel(KEY_T_FINISH_DATETIME)
        status = QLabel(KEY_T_FINISHED)

        self.edit_activity = QComboBox()
        #query
        #for activities in range(len(self.query)):
        #    self.edit_category.addItems(self.query[activities])

        self.edit_name = QLineEdit()
        self.edit_detail = QTextEdit()
        self.edit_begin_date = QDateTimeEdit(datetime.now())
        self.edit_begin_date.setCalendarPopup(True)
        self.edit_begin_date.setDisplayFormat(('yyyy-MM-dd HH:mm:ss'))
        self.edit_end_date = QDateTimeEdit(datetime.now())
        self.edit_end_date.setCalendarPopup(True)
        self.edit_end_date.setDisplayFormat(('yyyy-MM-dd HH:mm:ss'))
        self.edit_status = QSpinBox(self)
        self.edit_status.setSingleStep(1)
        self.edit_status.setMaximum(1)
        self.edit_status.setMinimum(0)

        grid = QGridLayout()
        grid.addWidget(activity, 1, 0)
        grid.addWidget(self.edit_activity, 1, 1)

        grid.addWidget(name, 2, 0)
        grid.addWidget(self.edit_name, 2, 1)

        grid.addWidget(detail, 3, 0)
        grid.addWidget(self.edit_detail, 3, 1)

        grid.addWidget(begin_date, 4, 0)
        grid.addWidget(self.edit_begin_date, 4, 1)

        grid.addWidget(end_date, 5, 0)
        grid.addWidget(self.edit_end_date, 5, 1)

        grid.addWidget(status, 6, 0)
        grid.addWidget(self.edit_status, 6, 1)

        grid.addWidget(self.acceptButton, 8, 1)
        grid.addWidget(self.cancelButton, 8, 2)

        self.setLayout(grid)

        size = self.size()
        desktopSize = QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2)-(size.height() / 2)
        left = (desktopSize.width() / 2)-(size.width() / 2)

        self.move(left, top)
        self.setWindowTitle('Agregar Tarea')
        self.show()
        self.cancelButton.clicked.connect(self.close)
        self.connect(self.acceptButton, SIGNAL("clicked()"), self.create_Product)

    def create_Product(self):
        activity = str(self.edit_activity.currentText())
        name = str(self.edit_name.text())
        detail = str(self.edit_detail.toPlainText())
        begin_date = self.edit_begin_date.dateTime() 
        begin_date = str(begin_date.toString("yyyy-MM-dd HH:mm:ss"))
        end_date = self.edit_begin_date.dateTime()
        end_date = str(end_date.toString("yyyy-MM-dd HH:mm:ss"))
        status = str(self.edit_status.value())
        insert_tupla = (activity, name, detail, begin_date, end_date, status)
        conn = connection_data_base()
        session = conn.cursor()
        session.execute("INSERT INTO "+TABLE_TASK+" VALUES (NULL,?,?,?,?,?,?)", insert_tupla)
        conn.commit()
        session.close()
        self.close()