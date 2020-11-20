from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.questiones import *


# 测试接口
def index(request):
    q = Question6().getRandomQuestionfromDb()
    print(str(q.description) + ' ' + str(q.score) + ' ' + str(q.id1) + ' ' + str(q.num_series1) + ' ' + str(q.id2) + ' ' + str(q.num_series2))
    return HttpResponse("hello world")
