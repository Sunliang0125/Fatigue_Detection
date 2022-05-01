# -*- coding: utf-8 -*-
# @Time : 2022/2/24 17:25
# @Author : 孙  亮
# @File : Global.py
# @Software: PyCharm

from Utils import helpers, FACIAL_LANDMARKS_68_IDXS

#Global parameters 全局参数

#眼部数据阈值
EYR_THERSHOLD = 0.25
EYR_CONSEC_FRAMES = 4
EYR_CLOSE_FRAMES =23


MAX_DRIVING_TIME = 4#驾驶员正常驾驶时间为：4小时

#嘴部数据
MAR_THRESHOLD = 0.8
MAR_OPEN_FRAMS = 20

#计时器
CURRENT_TIME = None



#初始化计数器
TOTAL = 0

#脸部轮廓
(Jaw_Start, Jaw_End)= FACIAL_LANDMARKS_68_IDXS["jaw"]

#眼睛轮廓数据
(Left_eye_Start, Left_eye_End) = FACIAL_LANDMARKS_68_IDXS["left_eye"]
(Right_eye_Start, Right_eye_End) = FACIAL_LANDMARKS_68_IDXS["right_eye"]

#嘴巴轮廓数据
(Mouth_Start,Mouth_End) = FACIAL_LANDMARKS_68_IDXS["mouth"]


#EAR以及MAR的数据存放
my =[]
ey=[]

