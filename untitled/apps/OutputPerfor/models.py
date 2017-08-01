# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from BasicInfo.models import Rzxx
# Create your models here.


# 输出刻度表
class OutputScale(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=(100, 200), default=100)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),

    class Meta:
        verbose_name = "输出刻度"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue


# 输出稳定性（短期）
class OutputStability(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=(100, 200), default=100)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),

    class Meta:
        verbose_name = "输出稳定性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue


# 输出线性
class OutputLinear(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    ReferenceValue = models.IntegerField(verbose_name=u"参考值", choices=(50, 100, 200, 300, 500, 800, 1000), default=50)
    MeasuredValue = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u"测量值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),

    class Meta:
        verbose_name = "输出线性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MeasuredValue
