import math

import cv2
import numpy as np

class circle:

    def __init__(self):
        pass

    def setPicture(self,image):
        #grayType = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.binaryInv = self.handlePicture(image)

    def readUrlPicture(self,loc):#读入图片
        grayType = cv2.imread(loc, cv2.IMREAD_GRAYSCALE)#读入一幅灰度图片，第一个参数是图片路径
        self.binaryInv = self.handlePicture(grayType)
        # print(self.binaryInv)

    def handlePicture(self,grayType):#图片处理
        #grayType = cv2.imread("unclosure_" + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
        # 获取二元值的灰度图像 参数1：图片源，参数二：起始值(阈值)，参数三：最大值。参数四：划分算法类型。返回值第一个是阈值（t）,第二个是处理过的图像
        t, binaryInv = cv2.threshold(grayType, 127, 255, cv2.THRESH_BINARY_INV)
        #返回一个特定大小与形态结构用于形态学操作
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        # 将获得的二元值灰度图像进行形态学变化，先进行腐蚀，再进行膨胀操作
        binaryInv = cv2.morphologyEx(binaryInv, cv2.MORPH_OPEN, kernel)
        kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        binaryInv = cv2.morphologyEx(binaryInv, cv2.MORPH_DILATE, kernel1)
        return binaryInv

    def judgeCircle(self):

        contours, hierarchy = cv2.findContours(self.binaryInv, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        n = len(contours)
        contoursImg = []
        circleNum = 0
        R = []
        for i in range(n):
            Acontours = cv2.contourArea(contours[i])
            Pcontours = cv2.arcLength(contours[i], True)
            if Pcontours > 100 and Acontours < 150000:
                circleNum += 1
                r = format(4 * math.pi * Acontours / (Pcontours * Pcontours), '.2f')
                # print("Acontours[" + str(i) + "]=", Acontours)
                # print("Pcontours[" + str(i) + "]=", Pcontours)
                # print("Circularity R = ", str(r))
                R.append(float(r))
                temp = np.zeros(self.binaryInv.shape, np.uint8)
                contoursImg.append(temp)
        if R == []:
            return 0
        avgR = float(sum(R)) / len(R)
        # print("circleNum",circleNum)
        # print("avgR:",avgR)
        if circleNum <= 2 and circleNum > 0 and avgR >= 0.85:
            # print('得1分')
            return 1
        elif circleNum <= 2 and circleNum > 0 and avgR > 0.75:
            # print('得0分')
            return 0
        # print('得0分')
        return 0

    def showPicture(self):
        cv2.imshow('circle', self.binaryInv)
        cv2.waitKey()
