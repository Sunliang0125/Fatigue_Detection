# -*- coding: utf-8 -*-
# @Time : 2022/4/11 20:13
# @Author : 孙  亮
# @Site : 
# @File : Test_jishi.py
# @Software: PyCharm

import time
from Global import CURRENT_TIME
import Driving_Timing

import Timing

hour_meter = Timing.Timing()
hour_meter.start()


for i in range(1000000000):
    time.sleep(1)

    if i == 5:
        hour_meter.pause()


    if i == 10:
        hour_meter.resume()
    if i ==15 :
        hour_meter.stop()

    if i == 20:
        hour_meter.start()
    print(hour_meter.Current_time)











