# @Time    : 2020/12/12 17:06
# @Author  : Cosmos
# @Site    :
# @File    : questionUtils.py
# @Software: PyCharm

# import speech_recognition as sr
from backend.AI_module.prediction import predict_picture
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

class Q6_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        # self.correct_ans = ['一', '八', '四', '九', '六']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        i = 0
        if '18496' in patient_ans:
            self.score = 1

        models.Q6Res.objects.update_or_create(
            defaults={'normal_text': patient_ans, 'normal_score': self.score},
            openid=self.openID)
        return self.score


class Q6_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        i = 0
        if '481' in patient_ans:
            self.score = 1

        models.Q6Res.objects.update_or_create(
            defaults={'reverse_text': patient_ans, 'reverse_score': self.score},
            openid=self.openID)
        return self.score

class Q7score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans_dic = json.loads(self.response_json)
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        print(ans_dic)
        question_answer = ans_dic['question_answer']
        # print(type(question_answer))
        # print(question_answer[0])
        # print(type(question_answer[0]))
        question_text = ans_dic['question_text']
        # print(type(question_text))
        for i in range(20):
            if question_text[i] == '1' and question_answer[i] == 1:
                # print(question_answer[i])
                self.score += 1
        models.Q7Res.objects.update_or_create(
            defaults={'result_sequence': str(question_text) + str(question_answer), 'score': self.score},
            openid=self.openID)
        print(self.score)
        return self.score


class Q8score:
    def __init__(self, response_json, openid):
        self.score = 0
        self.response_json = response_json
        self.openid = openid

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans_dic = json.loads(self.response_json)
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        ans1 = ans_dic['a']
        ans2 = ans_dic['b']
        ans3 = ans_dic['c']
        ans4 = ans_dic['d']
        if ans1 == 93:
            self.score += 1
        if ans2 == 86:
            self.score += 1
        if ans3 == 79:
            self.score += 1
        if ans4 == 72:
            self.score += 1
        res = str(ans1) + "|" + str(ans2) + "|" + str(ans3) + "|" + str(ans4)
        models.Q8Res.objects.update_or_create(
            defaults={'result': res, 'score': self.score},
            openid=self.openid)
        return self.score

class Q9_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if patient_ans == '我只知道今天张亮是来帮过忙的人':
            self.score = 1
        models.Q9_1Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

class Q9_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if patient_ans == '狗在房间的时候猫总是躲在沙发下面':
            self.score = 1
        models.Q9_2Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

class Q11_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if '交通工具' in patient_ans:
            self.score = 1
        models.Q11_1Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class Q11_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if '测量工具' in patient_ans:
            self.score = 1
        models.Q11_2Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class Q12score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = ['鼻子', '丝绸', '寺庙', '菊花', '红色']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        for item in self.correct_ans:
            if item in patient_ans:
                self.score += 1
        models.Q12Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
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
        similarity = difflib.SequenceMatcher(
            None, patient_ans['loc'], correct_ans['loc']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        # 判断城市
        similarity = difflib.SequenceMatcher(
            None, patient_ans['city'], correct_ans['city']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        models.Q13Res.objects.update_or_create(
            defaults={'answer_string': patient_ans, 'realAnswer_string': correct_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class B_Q1score:
    def __init__(self, anwstring, openID):
        self.score = 0
        self.string = '1一2二3三4四5五6六'
        self.anwstring = anwstring
        self.openID = openID

    def getScore(self):
        if self.anwstring == self.string:
            self.score = 1
        models.B_Q1Res.objects.update_or_create(defaults={'string_from_patient': self.anwstring, 'score': self.score}, openid=self.openID)
        return self.score


class B_Q4score:
    def __init__(self, response_json, openID):
        self.score = 0
        # 判分需要的其他信息
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
        similarity = difflib.SequenceMatcher(
            None, patient_ans['loc'], correct_ans['loc']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        # 判断城市
        similarity = difflib.SequenceMatcher(
            None, patient_ans['city'], correct_ans['city']).quick_ratio()
        self.score += (1 if similarity > 0.5 else 0)
        models.B_Q4Res.objects.update_or_create(
            defaults={'answer_string': patient_ans, 'realAnswer_string': correct_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class B_Q5score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID
        # 判分需要的其他信息

    def getScore(self):
        # 判分逻辑
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        print(ans)
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        thisSet = set()
        for key in ans:
            num = ans[key].split(' ')
            print(num)
            # num.pop()
            num.remove('')
            num.sort()
            t_num = tuple(num)
            thisSet.add(t_num)
        print(thisSet)
        ans_str=""
        for item in thisSet:
            total = 0
            for i in range(len(item)):
                total += int(item[i])
                ans_str =ans_str+item[i]
            if total == 13:
                self.score = self.score + 1
        models.B_Q5Res.objects.update_or_create(
            defaults={'score': self.score,'answer_string':ans_str},
            openid=self.openID)
        return self.score

class B_Q6_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if '交通工具' in patient_ans:
            self.score = 1
        models.B_Q6_1Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

class B_Q6_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if '乐器' in patient_ans:
            self.score = 1
        models.B_Q6_2Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

class B_Q6_3score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if '方向' in patient_ans:
            self.score = 1
        models.B_Q6_3Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

class B_Q7score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = ['梅花', '萝卜', '沙发', '蓝色', '筷子']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        for item in self.correct_ans:
            if item in patient_ans:
                self.score += 1
        models.B_Q7Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score

# 语音转文字的工具类

# if __name__ == '__main__':
#     print(Q2score('moca/png_resource/2_1607928274.png').getScore())
