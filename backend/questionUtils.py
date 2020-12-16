# @Time    : 2020/12/12 17:06
# @Author  : Cosmos
# @Site    : 
# @File    : questionUtils.py
# @Software: PyCharm

# import speech_recognition as sr
# from backend.AI_module.prediction import predict_picture
import json
import difflib

from backend import models


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
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans_dic = json.loads(self.response_json)
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        patient_ans = ans_dic['answer']
        correct_ans = ans_dic['cur_answer']
        #  判断年份
        self.score += (1 if str(patient_ans['year']) == str(correct_ans['year']) else 0)
        # 判断月份
        self.score += (1 if str(patient_ans['month']) == str(correct_ans['month'] + 1) else 0)
        # 判断日
        self.score += (1 if str(patient_ans['day']) == str(correct_ans['date']) else 0)
        # 判断周几
        self.score += (1 if str(patient_ans['week']) == str(correct_ans['day']) else 0)
        # 判断地点
        similarity = difflib.SequenceMatcher(None, patient_ans['loc'], correct_ans['loc']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        # 判断城市
        similarity = difflib.SequenceMatcher(None, patient_ans['city'], correct_ans['city']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        models.Q13Res.objects.update_or_create(
            defaults={'answer_string': patient_ans, 'realAnswer_string': correct_ans, 'score': self.score},
            openid=self.openID)
        return self.score

# 语音转文字的工具类

# if __name__ == '__main__':
#     print(Q2score('moca/png_resource/2_1607928274.png').getScore())
