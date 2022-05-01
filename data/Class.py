# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:07
# @Author : 孙  亮
# @Site : 
# @File : Class.py
# @Software: PyCharm

import winsound
import dlib
import Utils
import cv2 as cv
import Get_Path
import time
from scipy.spatial import distance as dist


#引入常量

from data.Global import EYR_THERSHOLD,EYR_CONSEC_FRAMES,Left_eye_Start,Left_eye_End,\
    Right_eye_Start,Right_eye_End,Mouth_Start,Mouth_End,EYR_CLOSE_FRAMES,my,ey

class face_dectection:

    #获取model路径
    def get_modelPath(self):
       shape_detector_path = Get_Path.get_model_Path()
       return  shape_detector_path

    #获取人脸分类器
    def get_detector(self):
        # 人脸分类器
        detector = dlib.get_frontal_face_detector()
        return detector

    #获取人脸检测器
    def get_predictor(self):
        #获取路径
        shape_detector_path = self.get_modelPath()
        # 人脸检测器
        predictor = dlib.shape_predictor(shape_detector_path)
        return predictor



    #计算EAR
    def eye_aspect_ratio(self,eye):
        # 计算欧式距离，竖直的
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        # 计算欧式距离，水平的
        C = dist.euclidean(eye[0], eye[3])
        # ear值
        EAR = (A + B) / (2.0 * C)
        return EAR


    #计算MAR
    def mouth_aspect_ratio(self,mouth):
        # 计算欧式距离，竖直的
        A = dist.euclidean(mouth[2], mouth[10])
        B = dist.euclidean(mouth[4], mouth[8])
        # 计算欧式距离，水平的
        C = dist.euclidean(mouth[0], mouth[6])
        # ear值
        MAR = (A + B) / (2.0 * C)
        return MAR


    #检测人脸
    def detect(self, TOTAL,COUNTER):

        print("[INFO] loading facial landmark predictor...")
        video1_Path = Get_Path.get_test1_Path()
        # video2_Path = Get_Path.get_test2_Path()

        # 得到人脸数据
        detector = self.get_detector()

        # 获取人脸检测器
        predictor = self.get_predictor()

        # cap = cv.VideoCapture(video1_Path)
        cap = cv.VideoCapture(0)
        print("[INFO] starting video stream thread...")


        while True:
            #开始计时
            time_start = time.time()
            #计时器：

            # 预处理
            frame = cap.read()[1]
            if frame is None:
                break



            #设置尺寸
            (h, w) = frame.shape[:2]
            width = 800
            r = width / float(w)
            dim = (width, int(h * r))

            #转换为灰度图，排除颜色干扰
            frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)



             # 检测人脸
            #未检测到人脸
            rects = detector(gray, 0)
            if any(rects) is False:
                cv.putText(frame, " No drivers!", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                #语音播报提示


            #司机检测
            #包括司机的身份



            # 遍历每一帧检测到的人脸
            for rect in rects:
                # 获取坐标
                shape = predictor(gray, rect)
                points = Utils.shape_to_np(shape)

                # 分别计算EAR值
                leftEye = points[Left_eye_Start:Left_eye_End]
                rightEye = points[Right_eye_Start:Right_eye_End]
                leftEAR = self.eye_aspect_ratio(leftEye)
                rightEAR = self.eye_aspect_ratio(rightEye)

                # print("左眼EAR：",leftEAR)
                # print("左眼EAR：",rightEAR)

                # 算一个平均的
                EAR = (leftEAR + rightEAR) / 2.0


                # 绘制眼睛区域
                leftEyeHull = cv.convexHull(leftEye)
                rightEyeHull = cv.convexHull(rightEye)
                cv.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)


                #计算MAR值
                mouth = points[Mouth_Start:Mouth_End]
                MAR = self.mouth_aspect_ratio(mouth)


                #绘制MAR、EAR直线图

                ey.append(EAR)
                my.append(MAR)  # 将MAR和EAR数据放入


                #绘制嘴巴区域
                Mouth = points[Mouth_Start:Mouth_End]
                Mouth_Hull = cv.convexHull(Mouth)
                cv.drawContours(frame,[Mouth_Hull],-1,(0,255,0),1)


                #点头检测


                #检查MAR是否满足阈值


                # 检查EAR是否满足阈值
                if EAR < EYR_THERSHOLD:
                    COUNTER += 1
                    # 1.闭眼检测
                    if COUNTER >= EYR_CLOSE_FRAMES:
                        for i in range(2):
                            winsound.Beep(450,1000)
                        COUNTER = 0


                else:
                    # 如果连续几帧都是闭眼的，总数算一次
                    if COUNTER >= EYR_CONSEC_FRAMES and COUNTER < EYR_CLOSE_FRAMES:
                        TOTAL += 1
                    # 重置
                    COUNTER = 0


                #2.眨眼频率(正常情况下人每分钟眨眼次数为15-20次)
                time_end = time.time()

                current_period = time_end - time_start
                # print("当前时间：",current_period)
                # if (TOTAL/current_period) >= (20/60):
                #     for i in range(5):
                #         print(2)
                #         winsound.Beep(400,1000)



                # 显示眼部轮廓
                cv.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                            cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv.putText(frame, "EAR: {:.2f}".format(EAR), (300, 30),
                            cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv.imshow("Frame", frame)

            if ord('s') == cv.waitKey(10):
                break

        cap.release()
        cv.destroyAllWindows()
        return my,ey
