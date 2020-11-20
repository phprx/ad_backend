from backend import models
import random

"""
逻辑处理层，负责从数据库中保存的题库中随机抽取题目
"""


# 数字连线
class Question1:

    def __init__(self):
        self.id = None
        self.imagePath = None
        self.description = None
        self.score = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question1.objects.all()
        count = len(all_question)
        random_num = random.randint(0, count - 1)
        db_question = all_question[random_num]
        self.id = db_question.id
        self.description = '第一题题目描述'
        self.score = 1
        self.imagePath = db_question.image_path
        return self


# 画几何体
class Question2:

    def __init__(self):
        self.id = None
        self.imagePath = None
        self.description = None
        self.score = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question2.objects.all()
        count = len(all_question)
        random_num = random.randint(0, count - 1)
        db_question = all_question[random_num]
        self.id = db_question.id
        self.description = db_question.description
        self.score = 1
        self.imagePath = db_question.image_path
        return self


# 画钟表
class Question3:

    def __init__(self):
        self.id = None
        self.description = None
        self.score = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question3.objects.all()
        count = len(all_question)
        random_num = random.randint(0, count - 1)
        db_question = all_question[random_num]
        self.id = db_question.id
        self.description = db_question.description
        self.score = 1
        return self


# 动物命名
class Question4:

    def __init__(self):
        self.id1 = None
        self.answer1 = None
        self.image1Path = None
        self.id2 = None
        self.answer2 = None
        self.image2Path = None
        self.id3 = None
        self.answer3 = None
        self.image3Path = None
        self.description = None
        self.score = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question4.objects.all()
        count = len(all_question)
        record = []
        while len(record) < 3:
            random_num = random.randint(0, count - 1)
            if random_num not in record:
                record.append(random_num)
        self.description = '第四题题目描述'
        self.score = 3
        self.id1 = all_question[record[0]].id
        self.answer1 = all_question[record[0]].answer
        self.image1Path = all_question[record[0]].image_path
        self.id2 = all_question[record[1]].id
        self.answer2 = all_question[record[1]].answer
        self.image2Path = all_question[record[1]].image_path
        self.id3 = all_question[record[2]].id
        self.answer3 = all_question[record[2]].answer
        self.image3Path = all_question[record[2]].image_path
        return self


# 重复单词
class Question5:

    def __init__(self):
        self.id1 = None
        self.word1 = None
        self.audio_path1 = None
        self.id2 = None
        self.word2 = None
        self.audio_path2 = None
        self.id3 = None
        self.word3 = None
        self.audio_path3 = None
        self.id4 = None
        self.word4 = None
        self.audio_path4 = None
        self.id5 = None
        self.word5 = None
        self.audio_path5 = None
        self.description = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question5.objects.all()
        count = len(all_question)
        record = []
        while len(record) < 5:
            random_num = random.randint(0, count - 1)
            if random_num not in record:
                record.append(random_num)
        self.description = '第五题题目描述'
        self.id1 = all_question[record[0]].id
        self.word1 = all_question[record[0]].word
        self.audio_path1 = all_question[record[0]].audio_path
        self.id2 = all_question[record[1]].id
        self.word2 = all_question[record[1]].word
        self.audio_path2 = all_question[record[1]].audio_path
        self.id3 = all_question[record[2]].id
        self.word3 = all_question[record[2]].word
        self.audio_path3 = all_question[record[2]].audio_path
        self.id4 = all_question[record[3]].id
        self.word4 = all_question[record[3]].word
        self.audio_path4 = all_question[record[3]].audio_path
        self.id5 = all_question[record[4]].id
        self.word5 = all_question[record[4]].word
        self.audio_path5 = all_question[record[4]].audio_path
        return self


# 读数字序列
class Question6:

    def __init__(self):
        # 正序
        self.id1 = None
        self.num_series1 = None
        self.audio_path1 = None
        # 逆序
        self.id2 = None
        self.num_series2 = None
        self.audio_path2 = None
        self.description = None
        self.score = None

    def getRandomQuestionfromDb(self):
        all_positive_sequence = models.Question6.objects.filter(positive_sequence=1)
        positive_count = len(all_positive_sequence)
        random_num = random.randint(0, positive_count - 1)
        positive_sequence = all_positive_sequence[random_num]
        self.id1 = positive_sequence.id
        self.num_series1 = positive_sequence.sequence
        self.audio_path1 = positive_sequence.audio_path
        all_negative_sequence = models.Question6.objects.filter(positive_sequence=0)
        negative_count = len(all_negative_sequence)
        random_num = random.randint(0, negative_count - 1)
        negative_sequence = all_negative_sequence[random_num]
        self.id2 = negative_sequence.id
        self.num_series2 = negative_sequence.sequence
        self.audio_path2 = negative_sequence.audio_path
        self.description = '第六题题目描述'
        self.score = 2
        return self


# 遇到1记录
class Question7:

    def __init__(self):
        self.id = None
        self.description = None
        self.score = None
        self.series = None
        self.audioPath = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question7.objects.all()
        count = len(all_question)
        random_num = random.randint(0, count - 1)
        db_question = all_question[random_num]
        self.id = db_question.id
        self.description = '第七题题目'
        self.score = 1
        self.series = db_question.sequence
        self.audioPath = db_question.audio_path
        return self


# 100开始连续减7
class Question8:

    def __init__(self):
        self.description = '第八题题目'
        self.score = 3


# 语言复述
class Question9:

    def __init__(self):
        self.description = None
        self.score = None
        self.id1 = None
        self.statement1 = None
        self.audioPath1 = None
        self.id2 = None
        self.statement2 = None
        self.audioPath2 = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question9.objects.all()
        count = len(all_question)
        record = []
        while len(record) < 2:
            random_num = random.randint(0, count - 1)
            if random_num not in record:
                record.append(random_num)
        self.id1 = all_question[record[0]].id
        self.statement1 = all_question[record[0]].statement
        self.audioPath1 = all_question[record[0]].audio_path
        self.id2 = all_question[record[1]].id
        self.statement2 = all_question[record[1]].statement
        self.audioPath2 = all_question[record[1]].audio_path
        self.description = '第九题题目'
        self.score = 2

        return self


# 语言流畅性
class Question10:

    def __init__(self):
        self.description = '第十题题目描述'
        self.score = 1


# 词语共性
class Question11:

    def __init__(self):
        self.description = None
        self.score = None
        self.id1 = None
        self.parWord1 = None
        self.answer1 = None
        self.id2 = None
        self.parWord2 = None
        self.answer2 = None

    def getRandomQuestionfromDb(self):
        all_question = models.Question11.objects.all()
        count = len(all_question)
        record = []
        while len(record) < 2:
            random_num = random.randint(0, count - 1)
            if random_num not in record:
                record.append(random_num)
        self.id1 = all_question[record[0]].id
        self.parWord1 = all_question[record[0]].par_word
        self.answer1 = all_question[record[0]].answer
        self.id2 = all_question[record[1]].id
        self.parWord2 = all_question[record[1]].par_word
        self.answer2 = all_question[record[1]].answer
        self.description = '第十一题题目描述'
        self.score = 2
        return self


# 延迟回忆
class Question12:

    def __init__(self, q5):
        self.id1 = q5.id1
        self.word1 = q5.word1
        self.id2 = q5.id2
        self.word2 = q5.word2
        self.id3 = q5.id3
        self.word3 = q5.word3
        self.id4 = q5.id4
        self.word4 = q5.word4
        self.id5 = q5.id5
        self.word5 = q5.word5
        self.description = '第十二题题目描述'
        self.score = 5


# 定向
class Question13:

    def __init__(self):
        self.description = '第十三题题目描述'
        self.score = 6
