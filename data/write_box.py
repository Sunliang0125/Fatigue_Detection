# -*- coding: utf-8 -*-
# @Time : 2022/4/16 16:45
# @Author : 孙  亮
# @Site : 
# @File : write_box.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import datetime
import Get_Path





#记录整个过程中驾驶员的状态和信息
def data_show(my,ey):

    #当前日期和时间
    current = datetime.datetime.now()
    current_date_time = current.strftime("%Y%m%d_%H_%M_%S")
    filename = current_date_time
    print(filename)


    #获取存放目录
    path = Get_Path.get_store_Path()
    path_name = path+"\{}".format(filename)+".jpg"

    plt.figure(figsize=[20, 9])
    plt.plot(ey, label="EAR", color="#F08080")
    plt.plot(my, label="MAR", color="#0B7093")
    plt.text(1,1.0,"blinks:{}".format(128),fontsize=15,color = 'r')
    plt.legend()
    plt.savefig(path_name)
    plt.clf()  # 清除当前图形及其所有轴，但保持窗口打开，以便可以将其重新用于其他绘图。
    plt.close()  # 完全关闭图形窗口

