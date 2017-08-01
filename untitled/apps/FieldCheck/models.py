# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from BasicInfo.models import Rzxx

# Create your models here.


# 光射野重合性
class RadiationFit(object):
    sbbh = models.ForeignKey(Rzxx, verbose_name='设备编号')
    FieldSize = models.CharField(max_length=10, verbose_name='射野大小')
    GTValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"头脚方向值", default="")
    LRValue = models.DecimalField(max_digits=4, decimal_places=2,   verbose_name=u"左右方向值", default="")
    Estimate = models.BooleanField(verbose_name=u'达标判断', null=True, blank=True, default=''),

    class Meta:
        verbose_name = "光射野重合性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.FieldSize
