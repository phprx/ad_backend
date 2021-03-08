import json
import time
from backend import questionUtils
import requests
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from backend.questiones import *
import os
import time

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
        q5 = request.GET.get('5')
        q5_score = questionUtils.B_Q5score(q5, 'get').getScore()
        print(q5_score)
    return HttpResponse()


def multifile(request):
    print('access successfully')
    # GET请求用于获取前端传值（非文件类型请求），并完成每道题的打分。
    # 通过questionUtils中针对每道题设计的打分类提供的getScore()方法给出分值。
    if request.method == 'GET':
        q1 = request.GET.get('1')
        q6_1 = request.GET.get('6.1')
        q6_2 = request.GET.get('6.2')
        q7 = request.GET.get('7')
        q8 = request.GET.get('8')
        q9_1 = request.GET.get('9.1')
        q9_2 = request.GET.get('9.2')
        q10 = request.GET.get('10')
        q11_1 = request.GET.get('11.1')
        q11_2 = request.GET.get('11.2')
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

        # 第6大题计算分数存入数据库
        q6_1_score = questionUtils.Q6_1score(q6_1, openId).getScore()
        print('第6_1得分：' + str(q6_1_score))

        q6_2_score = questionUtils.Q6_2score(q6_2, openId).getScore()
        print('第6_2得分：' + str(q6_2_score))

        # 第7题计算分数并将分数与答案存入数据库
        q7_score = questionUtils.Q7score.getScore(q7)
        print('第7题得分：' + str(q7_score))
        # 第8题计算分数并将分数与答案存入数据库
        q8_score = questionUtils.Q8score.getScore(q8)
        print('第8题得分：' + str(q8_score))

        # 第9大题计算分数存入数据库
        q9_1_score = questionUtils.Q9_1score(q9_1, openId).getScore()
        print('第9_1得分：' + str(q9_1_score))

        q9_2_score = questionUtils.Q9_2score(q9_2, openId).getScore()
        print('第9_2得分：' + str(q9_2_score))

        # 第10题计算分数存入数据库
        q10_score = questionUtils.Q10_score(q10, openId).getScore()
        print('第10题得分：' + str(q10_score))

        # 第11大题计算分数存入数据库
        q11_1_score = questionUtils.Q11_1score(q11_1, openId).getScore()
        print('第11_1得分：' + str(q11_1_score))

        q11_2_score = questionUtils.Q11_2score(q11_2, openId).getScore()
        print('第11_2得分：' + str(q11_2_score))

        # 第12题计算分数并将分数与答案存入数据库,Q13score存储结果到MySQL
        q12_score = questionUtils.Q12score(q12, openId).getScore()
        print('第12题得分：' + str(q12_score))

        # 第13题计算分数并将分数与答案存入数据库,Q13score存储结果到MySQL
        q13_score = questionUtils.Q13score(q13, openId).getScore()
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


def multifile2(request):
    print('access successfully')
    # GET请求用于获取前端传值（非文件类型请求），并完成每道题的打分。
    # 通过questionUtils中针对每道题设计的打分类提供的getScore()方法给出分值。
    if request.method == 'GET':
        q1 = request.GET.get('1')
        q3 = request.GET.get('3')
        q4 = request.GET.get('4')
        q5 = request.GET.get('5')
        q6_1 = request.GET.get('6.1')
        q6_2 = request.GET.get('6.2')
        q6_3 = request.GET.get('6.3')
        q7 = request.GET.get('7')
        q8 = request.GET.get('8')
        q9_1 = request.GET.get('9.1')
        q9_2 = request.GET.get('9.2')
        q9_3 = request.GET.get('9.3')
        q9_4 = request.GET.get('9.4')
        q10_1 = request.GET.get('10.1')
        q10_2 = request.GET.get('10.2')
        openId = request.GET.get('openId')
        log_info = request.GET.get('loginfo')

        # 测试字段
        print("-------------------------------测试-------------------------------")
        test_f = request.GET.get('test')
        print("测试字段" + test_f)
        print("q3:" + q3)
        print("q5:" + q5)
        print("q6_1:" + q6_1)
        print("q6_2:" + q6_2)
        print("q7:" + q7)
        print("q8:" + q8)
        print("q9_1:" + q9_1)
        print("q9_2:" + q9_2)
        print("q9_3:" + q9_3)
        print("q9_4:" + q9_4)
        print("q10_1:" + q10_1)
        print("q10_2:" + q10_2)
        print("-------------------------------测试-------------------------------")


        # 提取用户信息
        log_info_dict = json.loads(log_info)
        name = log_info_dict['name']
        age = int(log_info_dict['age'])
        education = int(log_info_dict['education'])
        sex_flag1 = log_info_dict['1']
        sex_flag2 = log_info_dict['2']
        sex = '男'
        if sex_flag1 == '2' and sex_flag2 == '2':
            sex = '女'

        # 第1题计算分数并将分数与答案存入数据库
        q1_score = questionUtils.B_Q1score(q1, openId).getScore()
        print('第1题得分：' + str(q1_score))

        # 第3题计算分数并将分数与答案存入数据库
        q3_score = questionUtils.B_Q3score(q3, openId).getScore()
        print('第3题得分：' + str(q3_score))

        # 第4题计算分数存入数据库
        q4_score = questionUtils.B_Q4score(q4, openId).getScore()
        print('第4题得分：' + str(q4_score))

        # 第5题计算分数并将分数与答案存入数据库
        q5_score = questionUtils.B_Q5score(q5, openId).getScore()
        print('第5题得分：' + str(q5_score))

        # 第6大题计算分数并将分数存入数据库
        q6_1_score = questionUtils.B_Q6_1score(q6_1, openId).getScore()
        print('第6.1题得分：' + str(q6_1_score))

        q6_2_score = questionUtils.B_Q6_2score(q6_2, openId).getScore()
        print('第6.2题得分：' + str(q6_2_score))

        q6_3_score = questionUtils.B_Q6_3score(q6_3, openId).getScore()
        print('第6.3题得分：' + str(q6_3_score))

        # 第7题计算分数并将分数与答案存入数据库
        q7_score = questionUtils.B_Q7score(q7, openId).getScore()
        print('第7题得分：' + str(q7_score))

        # 第8题计算分数并将分数与答案存入数据库
        q8_score = questionUtils.B_Q8score(q8, openId).getScore()
        print('第8题得分：' + str(q8_score))

        # 第9题计算分数并将分数与答案存入数据库
        q9_1_score = questionUtils.B_Q9_1score(q9_1, openId).getScore()
        print('第9.1题得分：' + str(q9_1_score))

        q9_2_score = questionUtils.B_Q9_2score(q9_2, openId).getScore()
        print('第9.2题得分：' + str(q9_2_score))

        q9_3_score = questionUtils.B_Q9_3score(q9_3, openId).getScore()
        print('第9.3题得分：' + str(q9_3_score))

        q9_4_score = questionUtils.B_Q9_4score(q9_4, openId).getScore()
        print('第9.4题得分：' + str(q9_4_score))

        # 第10题计算分数并将分数与答案存入数据库
        q10_1_score = questionUtils.B_Q10_1score(q10_1, openId).getScore()
        print('第10.1题得分：' + str(q10_1_score))

        q10_2_score = questionUtils.B_Q10_2score(q10_2, openId).getScore()
        print('第10.2题得分：' + str(q10_2_score))

        # 将所有题目存入历史记录表
        db_dict = {
            'name': name, 'sex': sex, 'age': age, 'education': education
            , 'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            , 'Q1_score': q1_score, 'Q3_score': q3_score, 'Q4_score': q4_score, 'Q5_score': q5_score
            , 'Q6_score': q6_1_score + q6_2_score + q6_3_score, 'Q7_score': q7_score
            , 'Q8_score': q8_score, 'Q9_score': q9_1_score + q9_2_score + q9_3_score + q9_4_score
            , 'Q10_score': q10_1_score + q10_2_score
            , 'total_score': q1_score + q3_score + q4_score + q5_score + q6_1_score + q6_2_score + q6_3_score + q7_score + q8_score + q9_1_score + q9_2_score + q9_3_score + q9_4_score + q10_1_score + q10_2_score}
        models.B_MOCA_History.objects.update_or_create(openid=openId, defaults=db_dict)

        return HttpResponse(json.dumps(db_dict), content_type="application/json")

    # POST请求用于传输文件（前端首先使用POST方法上传所有文件数据到服务器）
    else:
        n = str(request.POST.get('NUMBER'))
        openid = request.POST.get('openid')
        print("openid" + " " + str(openid))
        print('第' + n + '个文件上传成功')
        if not os.path.exists('moca_b/' + 'png_resource' + '/'):
            os.makedirs('moca_b/' + 'png_resource' + '/')
        if not os.path.exists('moca_b/' + 'mp3_resource' + '/'):
            os.makedirs('moca_b/' + 'mp3_resource' + '/')
        report_file = request.FILES.get('file')
        timestamp = str(round(time.time()))

        '''B卷上传的全是录音'''
        fileType = 'mp3'

        '''n为前端setStorage时的序号，index为每题对应的题号'''
        index = None
        if int(n) == 0:
            index = '2'
        elif int(n) == 1:
            index = '3'
        elif int(n) == 2:
            index = '6.1'
        elif int(n) == 3:
            index = '6.2'
        elif int(n) == 4:
            index = '6.3'
        elif int(n) == 5:
            index = '7'
        elif int(n) == 6:
            index = '8'
        elif int(n) == 7:
            index = '9.1'
        elif int(n) == 8:
            index = '9.2'
        elif int(n) == 9:
            index = '9.3'
        elif int(n) == 10:
            index = '9.4'
        elif int(n) == 11:
            index = '10.1'
        elif int(n) == 12:
            index = '10.2'
        name = index + '_' + timestamp + '.' + fileType
        path = 'moca_b/' + fileType + '_resource' + '/'
        fw = open(path + name, 'wb+')
        for chunk in report_file.chunks():
            fw.write(chunk)
        fw.close()
        print("finished writing file")
        print(index, type(index))
        print("\n")

        if index == '3':
            print("question3:" + path + name)
            models.B_Q3Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q3_file_path': path + name})
        elif index == '6.1':
            print("question6.1:" + path + name)
            models.B_Q6_1Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q6_file_path1': path + name})
        elif index == '6.2':
            print("question6.2:" + path + name)
            models.B_Q6_2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q6_file_path2': path + name})
        elif index == '6.3':
            print("question6.3:" + path + name)
            models.B_Q6_3Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q6_file_path3': path + name})
        elif index == '7':
            print("question7:" + path + name)
            models.B_Q7Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q7_file_path': path + name})
        elif index == '8':
            print("question8:" + path + name)
            models.B_Q8Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q8_file_path': path + name})
        elif index == '9.1':
            print("question9:" + path + name)
            models.B_Q9Res.objects.update_or_create(defaults={'filePath1': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q9_file_path1': path + name})
        elif index == '9.2':
            print("question9:" + path + name)
            models.B_Q9Res.objects.update_or_create(defaults={'filePath2': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q9_file_path2': path + name})
        elif index == '9.3':
            print("question9:" + path + name)
            models.B_Q9Res.objects.update_or_create(defaults={'filePath3': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q9_file_path3': path + name})
        elif index == '9.4':
            print("question9:" + path + name)
            models.B_Q9Res.objects.update_or_create(defaults={'filePath4': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q9_file_path4': path + name})
        elif index == '10.1':
            print("question10.1:" + path + name)
            models.B_Q10_1Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q10_file_path1': path + name})
        elif index == '10.2':
            print("question10.2:" + path + name)
            models.B_Q10_2Res.objects.update_or_create(defaults={'filePath': path + name}, openid=openid)
            models.B_MOCA_History.objects.update_or_create(openid=openid, defaults={'Q10_file_path2': path + name})
        return HttpResponse()
