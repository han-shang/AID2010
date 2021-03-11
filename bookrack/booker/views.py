import hashlib
import random

from django.http import JsonResponse
from django.shortcuts import render
# from books.models import User_info
from tools.login import login_check
from django. db import models
from .models import *
from django.http import HttpResponse



# Create your views here.

def test_books(request,mail,number):
    print(number)
    # return HttpResponse('HG')
    # print('ggggg>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',mail,number)
    # return HttpResponse('FFFD')
    book = Novel.objects.filter(number=number).values('id')
    #获得书名类字典
    book_name = Novel.objects.filter(number=number).values('name')
    print('book_name>>>>>>>>>>>>>>>>>>>>>>>',book_name)
    book_names = book_name[0]['name']

    print('>>>>>>>>>>>',book)
    #获得书名
    messge_id = book[0]['id']
    print('messge＞＞＞＞＞＞＞＞＞＞',messge_id)
    try:
        author = NovelMessage.objects.filter(id=messge_id).values('author')[0]['author']
        introduce = NovelMessage.objects.filter(id=messge_id).values('introduce')[0]['introduce']
        up = NovelMessage.objects.filter(id=messge_id).values('up')[0]['up']
        serialize = NovelMessage.objects.filter(id=messge_id).values('serialize')[0]['serialize']
        vip_type = NovelMessage.objects.filter(id=messge_id).values('vip_type')[0]['vip_type']
    except:
        result = {'code':1001,'erro':'数据库中无此数据'}
        return JsonResponse(result)

    print('>>>>>>>>>>>>>>>>',author)
    print('>>>>>>>>>>>>>>>>', introduce)
    print('>>>>>>>>>>>>>>>>',up)
    print('>>>>>>>>>>>>>>>>',serialize)
    print('>>>>>>>>>>>>>>>>',vip_type)
    if serialize == True:
        serialize = '有更新'
    else:
        serialize = '暂无更新'
    if vip_type == True:
        vip_type = 'VIP'
    else:
        vip_type = '免费阅读'
    print('>>>>>>>>>>>>>>>>>',serialize,vip_type)

    email_id = Novelrack.objects.filter(number_id=number)
    if not email_id:
        book_rack = Novelrack()
        book_rack.number_id = number
        # print('dgggggg>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',book_names)
        book_rack.name = book_names
        book_rack.email = mail
        # print('>>>>>>>>>>>>>>>>>加入书架成功>>>>>>>>>>>>>>>>>',ema)
        book_rack.save()
        ema = '加入书架成功'
        result = {'code':200,'msg':ema}
        return JsonResponse(result)
    else:
        em = '已经加入书架,请勿重复加入'
        result = {'code':100,'error':em}
        return JsonResponse(result)



def test_input(request,email):
    # return HttpResponse(email)
    print(('>>>>>>>>>>>>>>>>>>>>>>', email))
    # 判断是不是有用户ｉｄ存放
    book_name = Novelrack.objects.filter(email=email)
    print(book_name)
    #如果没有用户就返回无书籍
    if not book_name:
        result = {'code':1003,'error':'暂无书籍加入'}
        return JsonResponse(result)
    else:
        messge_id = Novelrack.objects.filter(email=email).values_list('number_id')
        print('messsge_id>>>>>>>>>>>>>三季度经济上电视看>>>>>>>>>>>>>.',messge_id)

        rack_info = []
        for book_id in messge_id:
            item = {}
            #邮箱－－＞获得小说编号－－－＞获取小说ｉｄ－－＞获取小说详情
            rack_id = (book_id[0])
            print('rasl_list>>>>>>>>>>>>>>>>>>>>>',rack_id)
            nvel_id = Novel.objects.filter(number = rack_id).values('id')[0]['id']
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print(nvel_id)
            try:
                author = NovelMessage.objects.filter(id = nvel_id).values('author')[0]['author']
                print(author)
                introduce = NovelMessage.objects.filter(id = nvel_id).values('introduce')[0]['introduce']
                up = NovelMessage.objects.filter(id=nvel_id).values('up')[0]['up']
                serialize = NovelMessage.objects.filter(id=nvel_id).values('serialize')[0]['serialize']
                vip_type = NovelMessage.objects.filter(id=nvel_id).values('vip_type')[0]['vip_type']
            except:
                result = {'code': 1005, 'erro': '无此数据'}
                return JsonResponse(result)

            print('>>>>>>>>>>>>>>>>', author)
            print('>>>>>>>>>>>>>>>>', introduce)
            print('>>>>>>>>>>>>>>>>', up)
            print('>>>>>>>>>>>>>>>>', serialize)
            print('>>>>>>>>>>>>>>>>', vip_type)
            if serialize == True :
                serialize = '有更新'
                vip_type = 'VIP'
            else:
                serialize = '暂无更新'
                vip_type = '免费阅读'
            str1 = str(introduce)
            if len(str1)>5:
                st = str1[:5] + '....'
                print('>>>>>>>>>>>>>>>>>', serialize, vip_type)
                item['author'] = author
                item['introduce'] = st
                item['up'] = up
                item['serialize'] = serialize
                item['vip_type'] = vip_type
                rack_info.append(item)

        result = {'code':200,'data':rack_info,'msg':'成功'}
        return JsonResponse(result)













