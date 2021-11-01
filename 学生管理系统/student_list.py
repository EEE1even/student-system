# 黄施洋
# 开发人员：小米甜甜
# 开发时间：2021/1/3      15:25
# 文件名称：student_list.py.py
# 开发工具：PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel,QSqlTableModel
from PyQt5.QtWidgets import QHeaderView, QMenu, QMessageBox, QAbstractItemView

class Ui_stundent_list(QtWidgets.QMainWindow):
    signalRadioButton = pyqtSignal(str)
    signal = pyqtSignal(str)
