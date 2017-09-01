# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 用户表扩展
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="", verbose_name=u"地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, default="", verbose_name=u"电话")
    image = models.ImageField(upload_to="image/%y%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # 不定义就不能打印字符串
        return self.username


# 邮箱验证码
# class EmailVerifyRecord(models.Model):
#     code = models.CharField(max_length=20, verbose_name=u"验证码")
#     email = models.EmailField(max_length=50, verbose_name=u"邮箱")
#     send_type = models.CharField(verbose_name=u"验证码类型", max_length=50, choices=(("register", u"注册"), ("forget", u"找回密码")))
#     send_time = models.DateTimeField(verbose_name=u"验证时间", default=datetime.now)
#
#     class Meta:
#         verbose_name = u"邮箱验证码"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return '{0}({1})'.format(self.code, self.email)


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager,
#                      self).get_queryset().filter(status='published')


# class Post(models.Model):
#     # ...
#     objects = models.Manager()  # The default manager.
#     published = PublishedManager()  # Our custom manager.
#
# Post.published.filter(title__startswith='Who')
