# -*- coding: UTF-8 -*-
# ！python3.7

# -----------------------------------
# @Project name: Graduate_design
# @File name   : Timing.py
# @Time    : 2022/4/25 14:38
# @Author  :   孙 亮
# @Software: PyCharm
# -----------------------------------

import threading
import time



class Timing(threading.Thread):
    def __init__(self):
        super().__init__()
        self.Current_time = "0时0分0秒"

        self.flag = threading.Event()
        self.flag.set()

        self.running = threading.Event()
        self.running.set()

        self.hour = 0
        self.minite = 0
        self.second = 0



    def run(self) -> None:
        self.Timing()

    #计时功能
    def Timing(self):

            while self.running.isSet():
                self.flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
                self.second += 1
                time.sleep(1)

                if self.second == 60:
                    self.second = 0
                    self.minite += 1
                    if self.minite == 60:
                        self.hour += 1
                        self.second = 0
                        self.minite = 0

                self.Current_time = "{}时".format(round(self.hour))+"{}分".format(round(self.minite))+"{}秒".format(self.second)

    #标志位置Flase
    def pause(self):
        self.flag.clear()

    def resume(self):
        self.flag.set()

    def stop(self):
        # self.flag.set()
        self.running.clear()
        self.hour = 0
        self.minite = 0
        self.second = 0





