from django.db import models


# Create your models here.


# 测试表，不用管
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


# 数字连线
class Question1(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=20)


# 画几何体
class Question2(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=200)
    image_path = models.CharField(max_length=20)


# 画钟表
class Question3(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=200)


# 动物命名
class Question4(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=20)
    image_path = models.CharField(max_length=20)


# 重复单词
class Question5(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=20)
    audio_path = models.CharField(max_length=20)


# 读数字序列
class Question6(models.Model):
    id = models.IntegerField(primary_key=True)
    sequence = models.CharField(max_length=20)
    positive_sequence = models.IntegerField()
    audio_path = models.CharField(max_length=20)


# 遇到1记录
class Question7(models.Model):
    id = models.IntegerField(primary_key=True)
    sequence = models.CharField(max_length=50)
    audio_path = models.CharField(max_length=20)


# 语言复述
class Question9(models.Model):
    id = models.IntegerField(primary_key=True)
    statement = models.CharField(max_length=50)
    audio_path = models.CharField(max_length=20)


class Question11(models.Model):
    id = models.IntegerField(primary_key=True)
    par_word = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)


# SAS、SDS量表
class Scale(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    sas_score = models.IntegerField(null=True)
    sds_score = models.IntegerField(null=True)


'''接收各题目答案的数据表设计，每一题都有得分的字段，
   主键id为openid'''


# 题目1：连线题，前端传过来的字符串，后端判断后存分数
class Q1Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    score = models.IntegerField(null=True)
    string_from_patient = models.CharField(max_length=20)


# 题目2：画图，前端传图片，后端判定
class Q2Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    score = models.IntegerField(null=True)
    filePath = models.TextField(null=True)


# 题目3：画钟


# 题目4：猜动物，前端传语音，后端转文字，保存语音路径和转换后的文字
class Q4Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    score = models.IntegerField(null=True)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)


# 题目5：读取词语，前端传语音，后端转文字，保存语音路径和转换后的文字
class Q5Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    score = models.IntegerField(null=True)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)


# 题目6：读数字，正序读5个，
# 倒叙读三个，前端传语音，后端转文字，保存语音路径和转换后的文字
class Q6Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    normal_audio_filePath = models.TextField(null=True)
    reverse_audio_filePath = models.TextField(null=True)
    normal_text = models.TextField(null=True)
    reverse_text = models.TextField(null=True)
    normal_score = models.IntegerField(null=True)
    reverse_score = models.IntegerField(null=True)
    total_score = models.IntegerField(null=True)


# 题目7：听1按键，传随机序列和病人点击的序列到后端，判分并存储到数据库
class Q7Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    result_sequence = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目8：随机减数，传每道题得分的数据到后端，判分并存储到数据库
class Q8Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    score = models.IntegerField(null=True)
    result = models.TextField(null=True)


# 题目9.1：重复句子，前端传语音，后端转文字，后端转文本，保存文本和录音；
class Q9_1Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目9.2：重复句子，前端传语音，后端转文字，后端转文本，保存文本和录音；
class Q9_2Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目10：一分钟说动物名，前端传语音，后端转文本，保存文本和录音
class Q10Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目11.1：求同存异，前端传语音，后端转文字，后端转文本，保存文本和录音
class Q11_1Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目11.2：求同存异，前端传语音，后端转文字，后端转文本，保存文本和录音
class Q11_2Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目12：回忆第五题所提到的5个词，前端传语音，后端转文本，保存文本和录音
class Q12Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    filePath = models.TextField(null=True)
    audio_to_text = models.TextField(null=True)
    score = models.IntegerField(null=True)


# 题目13：写年月日、星期几、地点、城市
class Q13Res(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    answer_string = models.CharField(null=True, max_length=50)
    realAnswer_string = models.CharField(null=True, max_length=50)
    score = models.IntegerField(null=True)
