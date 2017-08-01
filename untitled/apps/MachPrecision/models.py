# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from BasicInfo.models import Rzxx

# Create your models here.


# 激光灯精度
class LaserPrecision(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    LaserLamp = models.CharField(max_length=10, verbose_name='激光灯位置')
    MeasuredValue = models.CharField(max_length=10,  verbose_name=u"测量偏差", default="")

    class Meta:
        verbose_name = "激光灯精度"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.LaserLamp


# 机械等中心精度
class IsocenterPrecision(object):
    sbbh=models.ForeignKey(Rzxx, verbose_name='设备编号')
    collimator = models.CharField(max_length=10, verbose_name=u'准直器')
    couch = models.CharField(max_length=10, verbose_name=u'治疗床')
    gantry = models.CharField(max_length=10, verbose_name=u'旋转机架')

    class Meta:
        verbose_name = "机械等中心精度"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')


# 机械等中心精度（胶片法）
class IsocenterPrecisionFilm(object):
    sbbh=models.ForeignKey(Rzxx, verbose_name='设备编号')
    collimator = models.CharField(max_length=10, verbose_name=u'准直器')
    couch = models.CharField(max_length=10, verbose_name=u'治疗床')
    gantry = models.CharField(max_length=10, verbose_name=u'旋转机架')

    class Meta:
        verbose_name = "机械等中心精度（胶片法）"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.sbbh')
