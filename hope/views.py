from django.http import HttpResponse
from django.shortcuts import render
import pymysql

content = '''
Hello world ! \n
Welcome to Guangzhou ! \n
Great! \n
管若彤小朋友！\n
李伯阳小朋友！\n
大家好！
'''

'''
def hello(request):
    return HttpResponse(content)
'''


def runoob(request):
    context = {'hello': content,
               'dataset': query(),
               'mybrother': mybrt()}

    return render(request, 'runoob.html', context)


def query():
    # 建立数据库连接实例
    db = pymysql.connect(user="root", password="123", host='localhost', database="mytest")
    # 获取数据库实例的游标
    cur = db.cursor()

    # SQL语句
    query_sql = "select * from mybook_tbl"
    # 游标执行SQL语句查询，返回记录数量int
    rs = cur.execute(query_sql)

    # 利用查询结果（int），cur.fetchone 逐条输出数据库记录
    for i in range(rs):
        print(cur.fetchone())
        print('*' * 60)

    # 程序结束，关闭数据库实例的游标
    cur.close()

    # 程序结束，关闭数据库实例连接
    db.close()


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print("name:{}, score:{}".format(self.name, self.score))


def mybrt():
    student1 = Student("张三", 98)
    student1.show()
    student2 = Student("李四", 99)
    student2.show()


mybrt()
