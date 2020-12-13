import json
import time
from backend import questionUtils
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.questiones import *
import os

# 测试接口
# def index(request):
#     q = Question6().getRandomQuestionfromDb()
#     print(str(q.description) + ' ' + str(q.score) + ' ' + str(q.id1) + ' ' + str(q.num_series1) + ' ' + str(q.id2) + ' ' + str(q.num_series2))
#     return HttpResponse("hello world")

'''获取openid
    目前的appid为温健的appid'''


def getOpenid(request):
    resp = None
    # print(request.session['test'])      # 测试sessionid是否正常使用
    # request.session['test'] = 'session正常使用'  # 测试sessionid是否正常使用
    if request.method == 'GET':
        payload = {'appid': 'wx7955e3cc1d058951', 'secret': '1707aa88262e8dc354d91283869ea7a5',
                   'js_code': request.GET['code'],
                   'grant_type': 'authorization_code'}
        ip = 'https://api.weixin.qq.com/sns/jscode2session'
        url = ip + "?appid=" + payload['appid'] + "&secret=" + payload['secret'] + "&js_code=" + payload[
            'js_code'] + "&grant_type=authorization_code"
        resp = requests.post(url)

        print("wenjianshuaige" + resp.text)
        openid = resp.json()['openid']
        print(openid)
        # print('请求的url：' + resp.url)
        # print('请求结果：' + resp.text)
        # print('openid：' + resp.json().get('openid'))
    return HttpResponse(json.dumps(resp.json()), content_type="application/json")


def login(request):
    resp = {}
    if request.method == 'GET':
        openId = request.GET.get('openId')
        request.session['openId'] = openId  # 登录时将用户的openId存入session
        print(request.session['openId'])
    return HttpResponse()


# 目前存储2 13.1音频文件
# 1 7 8 13 14 非文件数据
def multifile(request):
    print('access successfully')
    if request.method == 'GET':
        q1 = request.GET.get('1')
        # q7 = request.GET.get('7')
        # q8 = request.GET.get('8')
        # q12 = request.GET.get('12')
        # q13 = request.GET.get('13')
        openId = request.GET.get('openId')


        score = questionUtils.Q1score().string_cmp(q1)
        # 除第一题有评分之外，其他题目评分还未处理
        models.Q1Res.objects.update_or_create(defaults={'string_from_patient': q1, 'score':score}, openid=openId)
        # models.Q7Res.objects.update_or_create(defaults={'result_sequence': str(q7)}, openid=openId)
        # models.Q8Res.objects.update_or_create(defaults={'result': str(q8), }, openid=openId)
        print(str(q1))

    else:
        n = str(request.POST.get('NUMBER'))
        openid = request.POST.get('openid')
        print("openid" + " " + str(openid))
        print('第' + n + '个文件上传成功')
        if not os.path.exists('moca/' + 'png_resource' + '/'):
            os.makedirs('moca/' + 'png_resource' + '/')
        if not os.path.exists('moca/' + 'mp3_resource' + '/'):
            os.makedirs('moca/' + 'mp3_resource' + '/')
        report_file = request.FILES.get('file')
        timestamp = str(round(time.time()))

        '''只有第一个是图片文件，剩余的都是音频文件'''
        fileType = 'png'
        if int(n) >= 1:
            fileType = 'mp3'

        '''n为前端setStorage是的序号，index为每题对应的题号'''
        index = '1'
        if int(n) == 0:
            index = '3-1'
        elif int(n) == 1:
            index = '3-2'
        elif int(n) == 2:
            index = '3-3'
        elif int(n) == 3:
            index = '2'
        elif int(n) == 4:
            index = '6.1'
        elif int(n) == 5:
            index = '6.2'
        elif int(n) == 6:
            index = '12-1'
        elif int(n) == 7:
            index = '9.1'
        elif int(n) == 8:
            index = '9.2'
        elif int(n) == 9:
            index = '10'
        elif int(n) == 10:
            index = '11.1'
        elif int(n) == 11:
            index = '11.2'
        elif int(n) == 12:
            index = '4'
        elif int(n) == 13:
            index = '5'
        name = index + '_' + timestamp + '.' + fileType
        path = 'moca/' + fileType + '_resource' + '/'
        fw = open(path + name, 'wb+')
        for chunk in report_file.chunks():
            fw.write(chunk)
        fw.close()
        print("finished writing file")
        print(index, type(index))
        print("\n")

        '''目前可以穿2、4、5号文件，剩余的需要存数据库的自行添加'''
        if index == '2':
            print("question2:" + path + name)
            models.Q2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '4':
            print("question4:" + path + name)
            models.Q4Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '5':
            print("question5:" + path + name)
            models.Q5Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
    return HttpResponse()


# 接收量表传过来的分数
def sdsResolve(request):
    if request.method == 'GET':
        openId = request.GET.get('openId')
        print(openId)
        '''取出量表的代号和相应的分值'''
        score = request.GET.get("sc")
        type_id = request.GET.get("id")
        print(score + " " + type_id)
        # sas(焦虑症)：102    sds(抑郁症)：104
        if type_id == '102':
            models.Scale.objects.update_or_create(defaults={'sas_score': score}, id=openId)
        elif type_id == '104':
            models.Scale.objects.update_or_create(defaults={'sds_score': score}, id=openId)
    return HttpResponse()
