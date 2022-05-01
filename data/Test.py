# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:13
# @Author : 孙  亮
# @Site :
# @File : Test.py
# @Software: PyCharm

import winsound
from data.Distance import get_euclidean_distance
from data.Class import face_dectection
import datetime
import os
# for i in range(15):
#     winsound.Beep(450, 1000)



from data import Class

aaa = face_dectection()
path = aaa.get_modelPath()
print(path)


# 需求，生成日志文件名，包含日期。形成每日一个日志文件
date = datetime.datetime.now()
date.time()

name = date.strftime("%Y-%m-%d-%H:%M:%S")
print(name)


############################

import Get_Path

path = Get_Path.get_store_Path()
print(path)






