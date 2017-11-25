#coding:utf-8
from django.db import models
# Create your models here.
from django.contrib import admin
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(verbose_name=u'文章分类', max_length=64)

    def __str__(self):
        return self.name


class article(models.Model):
    title = models.CharField(u'标题', max_length=60)
    category = models.ForeignKey(Category,verbose_name=u'标签',blank=True,null=True,on_delete=models.SET_NULL)
    createtime = models.DateTimeField(u'createtime', default=timezone.now)
    content = models.TextField(u'内容', blank=True, null=True)

    def __str__(self):
        return self.title

    class Mete:
        ordering = ['-createtime']


class aboutme(models.Model):
    aboutme = models.TextField(u'关于我', max_length=10000)

    def __str__(self):
        return u'关于我'


# 创建BlogPostAdmin类，继承admin.ModelAdmin(后台)父类，以列表的形式显示BlogPost的标题和时间

# 事实上是增加了一条ModelAdamin类中的表的字段
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'createtime', 'category')
