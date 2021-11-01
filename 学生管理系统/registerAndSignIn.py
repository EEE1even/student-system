import pymysql

#登陆
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

COLUMN_NAME=['学号','姓名','性别','专业','电话号码','班级','高级程序语言','python编程','数据库原理','数据结构与算法','数学分析',
             '高等数学','网络爬虫','数据可视化','数据挖掘','数据分析','总成绩']


def sign_in(user_name,password):
    # 连接数据库
    db= QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("127.0.0.1")
    db.setPort(3306)
    db.setDatabaseName("students")
    db.setUserName("root")
    db.setPassword("hsy010424")
    db.open()
    query=QSqlQuery()

    #sql语句查询是否存在
    sql = "select * from users WHERE user='%s' and password=%s"%(user_name,password)
    #执行
    query.exec_(sql)

    dic={}
    if query.next() ==False:
        stu=None
        return dic,stu
    else:
        stu=query.record().value('id')
        sql="select * from students WHERE 学号=%s"%stu
        query.exec_(sql)
        query.next()
        for v in COLUMN_NAME:
            dic[v]=query.record().value(v)
    db.close()
    return dic,stu


#注册
def register(id,user_name,password):
    if user_name=="" or password=="":
        return False
    #连接数据库
    db= QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("127.0.0.1")
    db.setPort(3306)
    db.setDatabaseName("students")
    db.setUserName("root")
    db.setPassword("hsy010424")
    db.open()
    query=QSqlQuery()
    #创建游标
    sql="select * from students WHERE 学号=%s"%id
    query.exec_(sql)
    if query.next()==False:
        return 'No'
    else:
        sql="insert into users(id,user,password)VALUES(%s,'%s',%s)"%(id,user_name,password)
    #判断输入的注册数据
        query.exec_(sql)
        if query.lastError().type()==2:
            return 'hasregist'
    db.close()
    return True