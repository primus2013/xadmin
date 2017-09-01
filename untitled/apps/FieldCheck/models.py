# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from BasicInfo.models import Rzxx
from datetime import datetime
# Create your models here.


# 光射野重合性
# class RadiationFit(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
#     MU = models.IntegerField(verbose_name='跳数')
#     FieldSize = models.CharField(max_length=10, verbose_name='射野大小', default='10cm×10cm')
#     GTValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"头脚方向值", default="")
#     LRValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"左右方向值", default="")
#     Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "光射野重合性"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.FieldSize
#
#
# # 射野大小
# class FieldSize(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
#     FieldSize = models.CharField(max_length=10, verbose_name='射野大小', choices=(("2cm×2cm", '2cm×2cm'), ("6cm×6cm", "6cm×6cm"), ("10cm×10cm", "10cm×10cm")), default='2cm×2cm')
#     MU = models.IntegerField(verbose_name='跳数')
#     GTValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"头脚方向值", default="")
#     LRValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"左右方向值", default="")
#     Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "射野大小"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.FieldSize
#
#
# # 半影大小
# class Penumbra(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
#     FieldSize = models.CharField(max_length=10, verbose_name='射野大小', choices=(("2cm×2cm", "2cm×2cm"), ("6cm×6cm", "6cm×6cm"), ("10cm×10cm", "10cm×10cm")), default='2cm×2cm')
#     MU = models.IntegerField(verbose_name='跳数')
#     GTValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"头脚方向值", default="")
#     LRValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"左右方向值", default="")
#     Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "半影大小"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.FieldSize
#
#
# # 平坦度
# class Flatness(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
#     FieldSize = models.CharField(max_length=10, verbose_name='射野大小', default='10cm×10cm')
#     MU = models.IntegerField(verbose_name='跳数')
#     GTValue = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"头脚方向值", default="")
#     LRValue = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"左右方向值", default="")
#     # Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "平坦度"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.FieldSize
#
#
# # 对称性
# class Symmetry(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
#     FieldSize = models.CharField(max_length=10, verbose_name='射野大小', default='10cm×10cm')
#     MU = models.IntegerField(verbose_name='跳数')
#     GTValue = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"头脚方向值", default="")
#     LRValue = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"左右方向值", default="")
#     # Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "对称性"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.FieldSize
