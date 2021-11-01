#获取班级列表
from PyQt5.QtSql import QSqlDatabase


def get_classes_list(query):

    query.exec_('SELECT class FROM classes')

    classes_list=[]
    while query.next():
        _class=query.record().value('class')
        classes_list.append(_class)

    return classes_list
#求平均成绩
def avg_grade(informations):
    total_grade = 0
    for v in informations:
        total_grade+=int(v)
    return (total_grade/len(informations))
#取得学生资料
def get_informations(querymodel):
    informations = []
    for i in range(0,querymodel.rowCount()):
        var = querymodel.record(i).value(5)  # 返回当前选中行的索引值
        informations.append(var)
    return informations

#学生成绩求和
def sum_grade(informations,COLUMN_NAME):
    total_grade = 0
    for i in range(6,len(COLUMN_NAME)-1):
        if informations[i]=='':
            break
        total_grade+=int(informations[i])
    return total_grade
#取得学生个人资料
def get_stu_informations(COLUMN_NAME,tableView,model):
    informations = []
    for i in COLUMN_NAME:
        var = model.record(tableView.currentIndex().row()).value(i)  # 返回当前选中行的索引值
        informations.append(var)
    return informations

