# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from BasicInfo.models import Rzxx
from datetime import datetime
# Create your models here.


# 输出刻度表
class OutputScale(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=((100, '100'), (200, '200')), default=100)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "输出刻度"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue


# 输出稳定性（短期）
class OutputStability(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=((100, '100'), (200, '200')), default=100)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "输出稳定性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue


# 输出线性
class OutputLinear(models.Model):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=((50, '50'), (100, '100'), (200, '200'), (300, '300'), (500, '500'), (800, '800'), (1000, '1000')), default=50)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),
    MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')

    class Meta:
        verbose_name = "输出线性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue
