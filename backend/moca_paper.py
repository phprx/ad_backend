from backend.questiones import *

"""
MOCA试卷类,每次开始测试时获取一个该对象
"""


class MocaPaper:

    def __init__(self):
        self.q1 = Question1().getRandomQuestionfromDb()
        self.q2 = Question2().getRandomQuestionfromDb()
        self.q3 = Question3().getRandomQuestionfromDb()
        self.q4 = Question4().getRandomQuestionfromDb()
        self.q5 = Question5().getRandomQuestionfromDb()
        self.q6 = Question6().getRandomQuestionfromDb()
        self.q7 = Question7().getRandomQuestionfromDb()
        self.q8 = Question8()
        self.q9 = Question9().getRandomQuestionfromDb()
        self.q10 = Question10()
        self.q11 = Question11().getRandomQuestionfromDb()
        self.q12 = Question12(q5=self.q5)
        self.q13 = Question13()
