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


class Q10_score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.num = 0
        self.QB = ['虎', '牛', '狼', '鼠', '兔', '鹿', '貂', '树懒', '斑马', '狗', '狐', '熊', '象', '豹子', '麋鹿', '狮子', '猪', '羊', '鸡',
                   '穿山甲', '熊猫', '猩猩', '海牛', '水獭', '灵猫', '海豚', '海象', '鸭嘴兽', '刺猬', '北极狐', '无尾熊', '北极熊', '蛇', '马',
                   '袋鼠', '犰狳', '河马', '海豹', '鲸鱼', '鼬', '龙鱼', '塘鳢', '鲶鱼', '鲨鱼', '章鱼', '刺鱼目', '鲱形目', '鲵鳅鱼', '猴',
                   '鳟鱼', '锦鲤', '鲤鱼', '金枪鱼', '神仙鱼', '鲈鱼', '鲑鱼', '孔雀鱼', '海鸥', '天鹅', '海狮', '企鹅', '龟', '蜥蜴', '蟾蜍',
                   '蝴蝶', '蜻蜓', '蝎子', '珊瑚', '海参', '海蜇', '海胆', '乌贼', '孔雀', '长颈鹿', '鹦鹉', '鸟', '蚂蚁']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text']
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        for item in self.QB:
            if item in patient_ans:
                self.num += 1
        if self.num > 10:
            self.score = 1
        models.Q10Res.objects.update_or_create(
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
        models.B_Q1Res.objects.update_or_create(defaults={'string_from_patient': self.anwstring, 'score': self.score},
                                                openid=self.openID)
        return self.score


class B_Q3score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.num = 0
        self.QB = ['苹果', '沙果', '海棠', '野樱莓', '枇杷', '欧楂', '山楂', '梨', '温柏', '蔷薇果', '花楸', '杏', '樱桃', '水蜜桃', '油桃', '蟠桃',
                   '李子',
                   '梅子', '西梅', '黑莓', '覆盆子', '云莓', '罗甘莓', '草莓', '菠萝', '甘蔗', '圣女果', '橘子', '砂糖桔', '橙子', '柠檬', '青柠', '柚子',
                   '金桔', '葡萄柚', '香橼', '佛手', '指橙', '黄皮果', '哈密瓜', '香瓜', '白兰瓜', '刺角瓜', '金铃子', '香蕉', '葡萄', '提子', '蓝莓',
                   '蔓越莓',
                   '越橘', '猕猴桃', '菠萝', '柿子', '黑枣', '黑柿', '桑葚', '无花果', '菠萝蜜']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        if self.response_json == '':
            models.B_Q3Res.objects.update_or_create(
                defaults={'score': self.score},
                openid=self.openID)
            return self.score
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        for item in self.QB:
            if item in patient_ans:
                self.num += 1
        if self.num > 7 and self.num < 13:
            self.score = 1
        elif self.num > 12:
            self.score = 2
        models.B_Q3Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
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
        ans_str = ""
        for item in thisSet:
            total = 0
            for i in range(len(item)):
                total += int(item[i])
                ans_str = ans_str + item[i]
            if total == 13:
                self.score = self.score + 1
        models.B_Q5Res.objects.update_or_create(
            defaults={'score': self.score, 'answer_string': ans_str},
            openid=self.openID)
        return self.score


class B_Q6_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        if self.response_json == '':
            models.B_Q6_1Res.objects.update_or_create(
                defaults={'score': self.score},
                openid=self.openID)
            return self.score
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]
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
        if self.response_json == '':
            models.B_Q6_2Res.objects.update_or_create(
                defaults={'score': self.score},
                openid=self.openID)
            return self.score
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]
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
        if self.response_json == '':
            models.B_Q6_3Res.objects.update_or_create(
                defaults={'score': self.score},
                openid=self.openID)
            return self.score
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]
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
        patient_ans = ans['text'][0:-1]
        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        for item in self.correct_ans:
            if item in patient_ans:
                self.score += 1
        models.B_Q7Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class B_Q8score(object):
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = ['剪刀', 'T恤', '香蕉', '台灯', '蜡烛', '手表', '杯子', '叶子', '钥匙', '勺子']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        res = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        count = 0
        for i in self.correct_ans:
            if i in res:
                count += 1
        if 4 <= count <= 5:
            self.score = 1
        elif 6 <= count <= 8:
            self.score = 2
        elif 9 <= count <= 10:
            self.score = 3
        models.B_Q8Res.objects.update_or_create(
            defaults={'audio_to_text': res, 'score': self.score},
            openid=self.openID)
        return self.score


class B_Q9_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = '斑马'
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        res = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if self.correct_ans == res:
            self.score = 1
        else:
            self.score = 0
        origin_score = models.B_Q9Res.objects.get(openid=self.openID).score
        if origin_score is None:
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text1': res, 'score': self.score},
                openid=self.openID)
        else:
            current_score = origin_score + self.score
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text1': res, 'score': current_score},
                openid=self.openID)
        return self.score


class B_Q9_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = '孔雀'
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        res = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if self.correct_ans == res:
            self.score = 1
        else:
            self.score = 0
        origin_score = models.B_Q9Res.objects.get(openid=self.openID).score
        if origin_score is None:
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text2': res, 'score': self.score},
                openid=self.openID)
        else:
            current_score = origin_score + self.score
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text2': res, 'score': current_score},
                openid=self.openID)
        return self.score


class B_Q9_3score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = '老虎'
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        res = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if self.correct_ans == res:
            self.score = 1
        else:
            self.score = 0
        origin_score = models.B_Q9Res.objects.get(openid=self.openID).score
        if origin_score is None:
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text3': res, 'score': self.score},
                openid=self.openID)
        else:
            current_score = origin_score + self.score
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text3': res, 'score': current_score},
                openid=self.openID)
        return self.score


class B_Q9_4score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = '蝴蝶'
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        res = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        if self.correct_ans == res:
            self.score = 1
        else:
            self.score = 0
        origin_score = models.B_Q9Res.objects.get(openid=self.openID).score
        if origin_score is None:
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text4': res, 'score': self.score},
                openid=self.openID)
        else:
            current_score = origin_score + self.score
            models.B_Q9Res.objects.update_or_create(
                defaults={'audio_to_text4': res, 'score': current_score},
                openid=self.openID)
        return self.score


class B_Q10_1score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = ['1', '8', '2', '3', '9', '4', '6', '7', '5']
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        count = 0
        for item in self.correct_ans:
            if item not in patient_ans:
                count = count + 1\

        if count <= 2:
            self.score = 2
        elif count == 3:
            self.score = 1
        else:
            self.score = 0
        models.B_Q10_1Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score


class B_Q10_2score:
    def __init__(self, response_json, openID):
        self.score = 0
        self.correct_ans = {0: 1, 1: 3, 2: 2, 3: 1, 4: 3, 5: 2, 7: 1, 8: 3, 9: 4}
        self.response_json = response_json
        self.openID = openID

    def getScore(self):
        # 第一步：先将response_json反序列化为对象
        ans = json.loads(self.response_json)
        patient_ans = ans['text'][0:-1]

        # 第二步：按每道题的判分逻辑进行判分，把结果分数赋值给score
        count = 0
        # 将字符串转换为整型数组
        patient_ans = list(map(int, patient_ans))
        patient_ans.sort()
        # 查询遗漏数字的个数
        count = 0
        for elem in patient_ans:
            if count >= 4:
                break
            if elem not in self.correct_ans:
                count = count + 1
            else:
                self.correct_ans[elem] = self.correct_ans[elem] - 1

        for num in self.correct_ans:
            count += self.correct_ans[num]

        if count <= 2:
            self.score = 2
        elif count == 3:
            self.score = 1
        else:
            self.score = 0
        models.B_Q10_2Res.objects.update_or_create(
            defaults={'audio_to_text': patient_ans, 'score': self.score},
            openid=self.openID)
        return self.score
