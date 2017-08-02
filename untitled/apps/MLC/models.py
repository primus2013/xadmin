# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from BasicInfo.models import Rzxx
# Create your models here.


# leafposition测试
class LeafPosition(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    MaxValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最大值')
    MinValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最小值')
    AverageValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"平均值")

    class Meta:
        verbose_name = "leafposition测试"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')


# pickfence测试
class PickFence(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    MaxValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最大值')
    MinValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='最小值')
    AverageValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"平均值")

    class Meta:
        verbose_name = "pickfence测试"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')
