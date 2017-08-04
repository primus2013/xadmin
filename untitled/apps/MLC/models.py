# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from BasicInfo.models import Rzxx, MLC, TPS
from datetime import datetime
# Create your models here.


# leafposition测试
class LeafPosition(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name=u'设备编号')
    MLC_Model = models.ForeignKey(MLC, verbose_name=u'MLC型号')
    DoseRate = models.IntegerField(verbose_name=u'剂量率')
    Dose = models.IntegerField(verbose_name=u'输出剂量')
    MaxValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最大值')
    MinValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最小值')
    AverageValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"平均值")
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "leafposition测试"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')


# pickfence测试
class PickFence(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    MLC_Model = models.ForeignKey(MLC, verbose_name=u'MLC型号')
    DoseRate = models.IntegerField(verbose_name=u'剂量率')
    Dose = models.IntegerField(verbose_name=u'输出剂量')
    MaxValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最大值')
    MinValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最小值')
    AverageValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"平均值")
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "pickfence测试"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')


# 叶片漏射
class LeafLeak(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name=u'设备编号')
    MLC_Model = models.ForeignKey(MLC, verbose_name=u'MLC型号')
    DoseRate = models.IntegerField(verbose_name=u'剂量率')
    Dose = models.IntegerField(verbose_name=u'输出剂量')
    D1 = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u'无遮挡值')
    D2 = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u'有遮挡位置2值')
    D3 = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"有遮挡位置3值")
    D4 = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"有遮挡位置4值")
    Calculate = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"计算值")
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "叶片漏射"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')
