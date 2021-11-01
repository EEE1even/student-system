# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtSql import QSqlDatabase
from  PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import enter
import ui_register
import ui_menu
import ui_all_functions
import ui_all_grade
from registerAndSignIn import sign_in
COLUMN_NAME=['学号','姓名','性别','专业','电话号码','班级','高级程序语言','python编程','数据库原理','数据结构与算法','数学分析','高等数学',
             '网络爬虫','数据可视化','数据挖掘','数据分析','总成绩']


class MyWindow(QMainWindow, enter.Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.iniUi()

    def iniUi(self):
        self.pushButton.clicked.connect(self.to_ui_register)
        self.pushButton_2.clicked.connect(self.to_ui_menu)

    def to_ui_mainwindow(self):
        MainWindow.show()
        ui_registerWindow.close()
        ui_MenuWindow.close()

    def to_ui_menu(self):
        _,stu=sign_in(self.lineEdit_2.text(),self.lineEdit.text())
        if stu=='88888888':
            ui_MenuWindow.show()
            self.to_ui_self_information()
            ui_MenuWindow.pushButton_5.clicked.connect(self.to_ui_mainwindow)
            ui_MenuWindow.pushButton.clicked.connect(self.to_ui_all_functions)
            ui_MenuWindow.pushButton_3.clicked.connect(self.to_ui_all_grade)
            ui_all_gradeWindow.close()
            MainWindow.close()
            ui_all_functionsWindow.close()
        elif stu==None:
            QMessageBox.warning(self,'错误','输入账号或密码有误',QMessageBox.Ok)
        else:
            self.to_ui_self_information()


    def to_ui_register(self):
        ui_registerWindow.show()
        ui_registerWindow.pushButton_2.clicked.connect(self.to_ui_mainwindow)
        MainWindow.close()

    def to_ui_all_functions(self):
        ui_all_functionsWindow.show()
        ui_all_functionsWindow.pushButton_5.clicked.connect(self.to_ui_menu)
        ui_all_functionsWindow.inimodel()
        ui_MenuWindow.close()

    def to_ui_all_grade(self):
        ui_all_gradeWindow.show()
        ui_all_gradeWindow.pushButton_4.clicked.connect(self.to_ui_menu)
        # ui_all_gradeWindow.update_combobox()
        ui_all_gradeWindow.inimodel()
        ui_MenuWindow.close()
    def to_ui_self_information(self):
        dic,stu=sign_in(self.lineEdit_2.text(),self.lineEdit.text())
        if stu== '88888888':
            stuInformations=['']
            ui_all_functionsWindow.judge_admin(stuInformations)
        else:
            stuInformations=[v for i,v in dic.items()]
            ui_all_functionsWindow.judge_admin(stuInformations)
            ui_all_functionsWindow.to_ui_self_information()



if __name__ == '__main__':

    app=QApplication(sys.argv)
    MainWindow=MyWindow()
    ui_registerWindow=ui_register.Ui_MainWindow()
    ui_MenuWindow=ui_menu.Ui_MainWindow()
    ui_all_functionsWindow=ui_all_functions.Ui_MainWindow()
    ui_all_gradeWindow=ui_all_grade.Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())


