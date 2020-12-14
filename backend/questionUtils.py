# @Time    : 2020/12/12 17:06
# @Author  : Cosmos
# @Site    : 
# @File    : questionUtils.py
# @Software: PyCharm

# import speech_recognition as sr
from backend.AI_module.prediction import predict_picture


class Q1score:
    def __init__(self):
        self.score = 0
        self.string = '1甲2乙3丙4丁5戊'

    def getScore(self, anwstring):
        if anwstring == self.string:
            self.score = 1
        return self.score


class Q2score:
    def __init__(self, image_path):
        self.score = 0
        self.image_path = image_path

    def getScore(self):
        if predict_picture(self.image_path) == 1:
            self.score = 1
        return self.score


class Q7score:
    def __init__(self, response_json):
        self.score = 0
        self.response_json = response_json

    def getScore(self):
        # 第一步：先将response_json反序列化为对象

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score

        return self.score


class Q8score:
    def __init__(self, response_json):
        self.score = 0
        self.response_json = response_json

    def getScore(self):
        # 第一步：先将response_json反序列化为对象

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score

        return self.score


class Q13score:
    def __init__(self, response_json):
        self.score = 0
        self.response_json = response_json

    def getScore(self):
        # 第一步：先将response_json反序列化为对象

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score

        return self.score


# 语音转文字的工具类

# if __name__ == '__main__':
#     print(Q2score('moca/png_resource/2_1607928274.png').getScore())
