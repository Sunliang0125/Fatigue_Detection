# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:40
# @Author : 孙  亮
# @Site : 
# @File : main.py
# @Software: PyCharm

from data.write_box import data_show
from data.Class import face_dectection
from data.Global import TOTAL
from data.Global import my,ey

#变量
COUNTER =0

#获取检测类对象
pro = face_dectection()

#检测
pro.detect(TOTAL=TOTAL,COUNTER=COUNTER)

#“白匣子”
data_show(my=my,ey=ey)


