from PyQt4 import QtGui
from PyQt4 import QtCore
from collections import namedtuple
from datetime import datetime, timedelta, date
from principal_view import Principal_View

if __name__ == '__main__':
    app = QtGui.QApplication([])
    mw = Principal_View()
    screenGeometry = QtGui.QApplication.desktop().availableGeometry()
    mw.resize(screenGeometry.width(), screenGeometry.height())
    mw.showMaximized()
    app.exec_()