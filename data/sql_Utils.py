# -*- coding: UTF-8 -*-
# ！python3.7

# -----------------------------------
# @Project name: Graduate_design
# @File name   : sql_Utils.py
# @Time    : 2022/4/29 16:10
# @Author  :   孙 亮
# @Software: PyCharm
# -----------------------------------
# Import Files

import pymysql
# -----------------------------------



class sql_Utils:
    def __init__(self):
        super().__init__()

        self.db = pymysql.connect(host='localhost',user='root',password='root',port=3306,charset='utf8',database="ft")
        #游标
        self.cursor = self.db.cursor()

    def insert(self,list):
        sql = '''insert into infor values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(sql,list)
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def delete(self,str_name):
        sql = "delete from infor where name = %s" %str_name
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()



if __name__ == '__main__':
    operate = sql_Utils()
    # data = ()
    # data
    str = "G:\Graduate_design\Login_informain\孙亮4.jpg".replace('\\', '/')
    list = []
    list.append("孙亮")
    list.append("男")
    list.append("1236454")
    list.append("478445545514")
    list.append(str)
    list.append(str)
    list.append(str)
    list.append(str)
    list.append(str)
    data = ('孙亮','男','12366455','845145121',str,str,str,str,str)

    operate.insert(list=list)