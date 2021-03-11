from django.contrib import admin

# Register your models here.
#用户表ｕｓｅｒ负责查询　收藏表Novelrack（粗存小说number,名称（通过名称和作者like模糊查询）
# 收藏表Novelrac通过number去获取小说的名称储存在Novelrack　
from .models import Novel,User, NovelTag, NumToTag,Novelrack,NovelMessage


class NovelManage(admin.ModelAdmin):
    list_display = ['id', 'name', 'number']
    list_display_links = ['id', 'name', 'number']
    list_filter = ['number']


admin.site.register(Novel, NovelManage)


class NovelTagManage(admin.ModelAdmin):
    list_display = ['number_id', 'name','email']
    list_display_links = ['number_id', 'number_id','email']
    list_filter = ['number_id','number_id','email']

    # def number(self, obj):
    #     novel_num = obj.tag.number
    #     return novel_num


admin.site.register(Novelrack, NovelTagManage)


class UserManage(admin.ModelAdmin):
     list_display = ['mail']


admin.site.register(User, UserManage)


class NovelMessageManage(admin.ModelAdmin):
    list_display = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
    list_display_links = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
    list_filter = ['author', 'up', 'vip_type', 'novel_num']
    search_fields = ['author', 'vip_type']
    list_ordering = ['id']


admin.site.register(NovelMessage, NovelMessageManage)