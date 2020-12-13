# @Time    : 2020/12/12 17:06
# @Author  : Cosmos
# @Site    : 
# @File    : questionUtils.py
# @Software: PyCharm

import speech_recognition as sr

class Q1score:
    def __init__(self):
        self.score = 0
        self.string = '1甲2乙3丙4丁5戊'

    def string_cmp(self, anwstring):
        if anwstring == self.string:
            self.score = 1
        return self.score

# 语音转文字的工具类

