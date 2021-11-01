# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_all_functions.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QHeaderView, QMenu, QMessageBox
import ui_self_information
from all_functions import *

COLUMN_NAME=['学号','姓名','性别','专业','电话号码','班级','高级程序语言','python编程','数据库原理','数据结构与算法','数学分析','高等数学',
             '网络爬虫','数据可视化','数据挖掘','数据分析','总成绩']



class Ui_MainWindow(QtWidgets.QMainWindow):
    signalRadioButton=pyqtSignal(str)
    signal =pyqtSignal(str)
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.inimodel()
        self.stuInformations=[]
        self.ui_self_informationWindow=ui_self_information.Ui_MainWindow()
        self.comboBox.addItems(['学号','姓名','电话号码'])
        self.signal.connect(self.show_status)
        self.pushButton_2.clicked.connect(self.remove_row)
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton_6.clicked.connect(self.save_data)
        self.tableView.clicked.connect(self.trigger_signal)
        self.pushButton_3.clicked.connect(self.search_student)
        self.pushButton_7.clicked.connect(self.inimodel)
        self.pushButton_4.clicked.connect(self.to_ui_self_information)
        self.ui_self_informationWindow.comboBox.activated.connect(self.to_ui_self_information)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息修改"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">选择查找内容：</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "查找"))
        self.pushButton_4.setText(_translate("MainWindow", "查看学生个人信息"))
        self.pushButton.setText(_translate("MainWindow", "增加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_6.setText(_translate("MainWindow", "保存"))
        self.pushButton_7.setText(_translate("MainWindow", "刷新"))
        self.pushButton_5.setText(_translate("MainWindow", "返回"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">欢迎</span></p></body></html>"))
    #初始化
    def inimodel(self):
        db= QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setPort(3306)
        db.setDatabaseName("students")
        db.setUserName("root")
        db.setPassword("hsy010424")
        db.open()

        self.model=QSqlTableModel()
        self.qurey=QSqlQuery()
        self.model.setTable("students")
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)
        self.model.select()
        self.classes=get_classes_list(self.qurey)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.generateMenu)

    #移除数据行
    def remove_row(self):
        row=self.tableView.currentIndex().row()
        self.model.removeRow(row)
        reply=QMessageBox.question(self,"确认","确定要删除%d记录？"%(row+1),QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            if self.model.submitAll() != False:
                self.signal.emit("删除第%d行记录"%(row+1))
            else:
                self.signal.emit("删除第%d行记录失败"%(row+1))
        if reply==QMessageBox.No:
            self.signal.emit("取消删除第%d行记录"%(row+1))
        self.model.select()

    #判断是否为管理员
    def judge_admin(self,stuInformations):
        if stuInformations[0] != '88888888':
            self.stuInformations=stuInformations
        else:
            self.stuInformations=stuInformations

    # 增加数据行
    def add_row(self):
        row=self.model.rowCount()
        self.model.insertRows(row,1)
        self.signal.emit("在%d行添加了一条记录"%row)


    #左下方小框信息提示
    def trigger_signal(self):
        self.signal.emit("选中\"%s\"信息"%(self.model.data(self.tableView.currentIndex())))
    #状态框，展示
    def show_status(self,str):
        self.label_4.setText(str)

    #保存数据
    def save_data(self):
        informations=get_stu_informations(COLUMN_NAME,self.tableView,self.model)
        total_grade=sum_grade(informations,COLUMN_NAME)
        index= self.model.createIndex(self.tableView.currentIndex().row(), 16)
        self.model.setData(index,total_grade)
        self.model.submitAll()
        #报错处理
        if self.model.lastError().type() != 0:
            QMessageBox.warning(self,"警告",self.model.lastError().text(),QMessageBox.Ok)
            self.inimodel()
            return
        _class=self.model.record(self.tableView.currentIndex().row()).value('班级')
        if _class in self.classes:
            return
        else:
            sql="INSERT classes(class) VALUES ('%s')"%_class
            self.qurey.exec_(sql)
        self.signal.emit("保存数据成功")
        self.model.select()

    #右键插入
    def generateMenu(self,pos):
        menu=QMenu()
        if self.tableView.currentIndex().column()<=5 and self.tableView.currentIndex().column()>=0:
            item1=menu.addAction(u"插入记录")
            item2=menu.addAction(u"删除记录")
            action=menu.exec_(self.tableView.mapToGlobal(pos))
            if action==item1:
                row=self.tableView.currentIndex().row()
                self.model.insertRow(row)
                self.model.submitAll()
                self.signal.emit("在%d行插入了一条记录"%row)
            if action==item2:
                self.remove_row()
        if self.tableView.currentIndex().column()>5:
            menu=QMenu()
            item1=menu.addAction(u"升序排列")
            item2=menu.addAction(u"降序排列")
            item3=menu.addAction(u"插入记录")
            item4=menu.addAction(u"删除记录")
            action=menu.exec_(self.tableView.mapToGlobal(pos))
            if action==item1:
                self.model.setSort(self.tableView.currentIndex().column(),Qt.AscendingOrder)
                self.model.select()
            if action==item2:
                self.model.setSort(self.tableView.currentIndex().column(),Qt.DescendingOrder)
                self.model.select()
            if action==item3:
                row=self.tableView.currentIndex().row()
                self.model.insertRow(row)
                self.model.submitAll()
                self.signal.emit("在%d行插入了一条记录"%row)
            if action==item4:
                self.remove_row()



    #查找学生个人信息
    def search_student(self):
        str="%s='%s'"%(self.comboBox.currentText(),self.lineEdit.text())
        self.model.setFilter(str)         #设置分类
        self.model.filter()               #执行分类
        #报错处理
        if self.model.lastError().type() != 0:
            QMessageBox.warning(self,"警告",self.model.lastError().text(),QMessageBox.Ok)
            self.inimodel()
            return
        self.model.select()
        if self.model.rowCount() == 0:
            QMessageBox.information(self, "Tip", "无法查询到该学生的信息", QMessageBox.Ok)
            self.inimodel()
            return

    #将学生信息填入成绩表
    def to_ui_self_information(self):
        stu_informations=self.stuInformations
        if stu_informations==['']:
            informations = get_stu_informations(COLUMN_NAME,self.tableView,self.model)
        else:
            informations=stu_informations
        if informations[0] == '':
            QMessageBox.information(self, "Tip", "未选中学生信息", QMessageBox.Ok)
            return
        if self.ui_self_informationWindow.comboBox.currentText()=='成绩':
            self.ui_self_informationWindow.insert_stu_information(informations)
        if self.ui_self_informationWindow.comboBox.currentText()=='等第':
            list=self.transform(informations)
            self.ui_self_informationWindow.insert_stu_information(list)
        self.ui_self_informationWindow.show()


    #等第转换
    def transform(self, informations):
        list=[]
        for i in range(0, 17):
            if i <6:
               list.append(informations[i])

            if i>=6 and i<16:
                if int(informations[i]) < 60 and int(informations[i]) >= 0:
                    list.append('<html><head/><body><p align=\"center\"><span style=\"color:#ff0000;\">不及格</span></p></body></html>')
                elif int(informations[i]) >= 60 and int(informations[i]) < 75:
                    list.append('<html><head/><body><p align=\"center\"><span style=\"color:#ff6430;\">及格</span></p></body></html>')
                elif int(informations[i]) >= 75 and int(informations[i]) < 90:
                    list.append('<html><head/><body><p align=\"center\"><span style=\"color:#efd44b;\">良好</span></p></body></html>')
                elif int(informations[i]) >= 90 and int(informations[i]) <= 100:
                    list.append('<html><head/><body><p align=\"center\"><span style=\"color:#209500;\">优秀</span></p></body></html>')
            if i==16:
                list.append(informations[i])
                return list