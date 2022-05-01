# -*- coding: utf-8 -*-
# @Time : 2022/4/11 20:04
# @Author : 孙  亮
# @Site : 
# @File : Test_yuyin.py
# @Software: PyCharm

import pyttsx3

msg = "阿萨德  "
engine = pyttsx3.init()


# 调节语速
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)

# 调节音量
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+20)

# 变换声音（文字为英文或数字时才有多种声音）
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

engine.say(msg)


engine.runAndWait()
