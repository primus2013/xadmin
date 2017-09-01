# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from BasicInfo.models import Rzxx, MLC
from datetime import datetime


# Create your models here.
# E2E测试
# class E2E(models.Model):
#     sbbh = models.ForeignKey(Rzxx, verbose_name=u'设备编号')
#     MLC_Model = models.ForeignKey(MLC, verbose_name=u'MLC型号')
#     MeasureValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u'测量值')
#     TPS_Value = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u'TPS计算值DT')
#     OffValue = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"偏差值")
#     PassRate = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=u"通过率")
#     MeasureTime = models.DateTimeField(default=datetime.now, verbose_name=u'测量时间')
#
#     class Meta:
#         verbose_name = "E2E测试"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return str('self.sbbh')