import random

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
        print('*' * 100)

    # 程序结束，关闭数据库实例的游标
    cur.close()

    # 程序结束，关闭数据库实例连接
    db.close()


class Student:
    # 类变量，定义在方法体之外，引用方法：类名.类变量名
    number = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 类变量引用，统计对象初始化次数
        Student.number = Student.number + 1

    def show(self):
        print("name:{}, score:{}".format(self.name, self.score))

    # 类方法，前面需要用到修饰符@classmethod
    @classmethod
    def total(cls):
        print("instance number:{0}".format(Student.number))


"""
def mybrt():
    student1 = Student("张三", 98)
    student1.show()
    student2 = Student("李四", 99)
    student2.show()
    student3 = Student("王五", 100)
    student3.show()
    # 类方法引用
    Student.total()
"""

# mybrt()

times = 100
while times >= 1:
    stu = "stu" + str(times)
    # stu = Student("三三", random.randint(50, 100))
    print(stu)
    times = times - 1
    continue
Student.total()
