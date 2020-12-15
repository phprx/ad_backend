import json
import time
from backend import questionUtils
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.questiones import *
import os

'''获取openid
    目前的appid为温健的appid'''


def getOpenid(request):
    resp = None
    # print(request.session['test'])      # 测试sessionid是否正常使用
    # request.session['test'] = 'session正常使用'  # 测试sessionid是否正常使用
    if request.method == 'GET':
        # payload = {'appid': 'wx7955e3cc1d058951', 'secret': '1707aa88262e8dc354d91283869ea7a5',
        #            'js_code': request.GET['code'],
        #            'grant_type': 'authorization_code'}
        payload = {'appid': 'wx27a50c62773be8a2', 'secret': '2eab9b7a6e5c17e32d07efb8637770e4',  # 黄鹏测试appid和secret
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


# 自己测的13题,不用管
def test(request):
    if request.method == 'GET':
        q13 = request.GET.get('13')
        q13_score=questionUtils.Q13score(q13,'get').getScore()
        print(q13_score)
    return HttpResponse()


def multifile(request):
    print('access successfully')
    # GET请求用于获取前端传值（非文件类型请求），并完成每道题的打分。
    # 通过questionUtils中针对每道题设计的打分类提供的getScore()方法给出分值。
    if request.method == 'GET':
        q1 = request.GET.get('1')
        q7 = request.GET.get('7')
        q8 = request.GET.get('8')
        q12 = request.GET.get('12')
        q13 = request.GET.get('13')
        openId = request.GET.get('openId')

        # 第1题计算分数并将分数与答案存入数据库
        q1_score = questionUtils.Q1score().getScore(q1)
        print('第1题得分：' + str(q1_score))
        models.Q1Res.objects.update_or_create(defaults={'string_from_patient': q1, 'score': q1_score}, openid=openId)

        # 第2题计算分数存入数据库
        q2_score = questionUtils.Q2score(models.Q2Res.objects.get(openid=openId).filePath).getScore()
        print('第2题得分：' + str(q2_score))
        models.Q2Res.objects.filter(openid=openId).update(score=q2_score)

        # 第7题计算分数并将分数与答案存入数据库

        # 第8题计算分数并将分数与答案存入数据库

        # 第13题计算分数并将分数与答案存入数据库,Q13score存储结果到MySQL
        q13_score=questionUtils.Q13score(q13,openId).getScore()
        print('第13题得分：' + str(q13_score))



    # POST请求用于传输文件（前端首先使用POST方法上传所有文件数据到服务器）
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

        '''区分文件类型'''
        fileType = 'mp3'

        '''n为前端setStorage是的序号，index为每题对应的题号'''
        index = None
        if int(n) == 0:
            index = '3-1'
            fileType = 'png'
        elif int(n) == 1:
            index = '3-2'
            fileType = 'png'
        elif int(n) == 2:
            index = '3-3'
            fileType = 'png'
        elif int(n) == 3:
            index = '2'
            fileType = 'png'
        elif int(n) == 4:
            index = '6.1'
        elif int(n) == 5:
            index = '6.2'
        elif int(n) == 6:
            index = '12.1'
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

        if index == '2':
            print("question2:" + path + name)
            models.Q2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '4':
            print("question4:" + path + name)
            models.Q4Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '5':
            print("question5:" + path + name)
            models.Q5Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '6.1':
            print("question6-1:" + path + name)
            models.Q6Res.objects.update_or_create(defaults={'normal_audio_filePath': path + name}, openid=openid)
        elif index == '6.2':
            print("question6-2:" + path + name)
            models.Q6Res.objects.update_or_create(defaults={'reverse_audio_filePath': path + name}, openid=openid)
        elif index == '9.1':
            print("question9.1:" + path + name)
            models.Q9_1Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '9.2':
            print("question9.2:" + path + name)
            models.Q9_2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '10':
            print("question10:" + path + name)
            models.Q10Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '11.1':
            print("question11.1:" + path + name)
            models.Q11_1Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '11.2':
            print("question11.2:" + path + name)
            models.Q11_2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
        elif index == '12.1':
            print("question12.1:" + path + name)
            models.Q12Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
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
