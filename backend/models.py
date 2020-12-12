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
    id = models.IntegerField(primary_key=True)
    sas_score = models.IntegerField(null=True)
    sds_score = models.IntegerField(null=True)
