# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 新建一个数据处理方法，将数据内容按日期归档
# class RzxxManager(models.Manager):
#     def distinct_date(self):
#         distinct_date_list = []     # 存放处理结果
#         date_list = self.values('rzsj')
#         for date in date_list:
#             # date = date['rzsj'].strftime('%Y{y}%m{m}').format(y='年', m='月')
#             date = date['rzsj'].strftime('%Y/%m')
#             # date = date['rzsj'].strftime('%Y/%m文件存档')  # 用于改变获得的数据格式
#             if date not in distinct_date_list:
#                 distinct_date_list.append(date)
#         return distinct_date_list


# 医院字典
class Yyxx(object):
    yymc = models.CharField(max_length=50, verbose_name='医院名称')
    chengshi = models.CharField(max_length=50, verbose_name='所在城市')
    dengj = models.CharField(max_length=50, verbose_name='医院等级')

    class Meta:
        verbose_name = '医院字典'
        verbose_name_plural = verbose_name
        ordering = ['-yymc', 'dengj']

    def __unicode__(self):
        return self.yymc


# 厂家字典
class Sbcj(object):
    cjmc = models.CharField(max_length=50, verbose_name='厂家名称')
    szdq = models.CharField(max_length=50, verbose_name='所在国家')

    class Meta:
        verbose_name = '厂家字典'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.cjmc


# 设备字典
class Sbxh(object):
    sbxh = models.CharField(max_length=50, verbose_name='设备型号')
    leix = models.CharField(max_length=50, verbose_name='设备类型')
    sscj = models.ForeignKey(Sbcj, default='', verbose_name='所属厂家')
    sbdj = models.CharField(max_length=50, default='', null=True, verbose_name='设备等级')

    class Meta:
        verbose_name = '设备字典'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.sbxh


# 医院入组情况表
class Rzxx(object):
    sbbh=models.CharField(max_lengh=10, verbose_name=u'设备编号')
    yymc=models.ForeignKey(Yyxx, verbose_name='医院名称')
    sbcj=models.ForeignKey(Sbcj, verbose_name='设备厂家')
    sbxh=models.ForeignKey(Sbxh, max_length=50, verbose_name='设备型号')
    rzsj = models.DateField(verbose_name='入组时间')
    bz=models.TextField(max_length=500, null=True, verbose_name='备注')

    # 将在models.py里定义的类关联进来
    # objects = RzxxManager()

    class Meta:
        verbose_name='入组信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.sbbh
        # return str('self.yymc')

# 所需公式存放表
class Formula(object):
    label_name = models.CharField(max_length=20, verbose_name=u"表名称", default="")
    Formula = models.DateField(max_length=20, verbose_name=u"公式", null=True, blank=True)
    DeviationValue = models.DecimalField(max_digits=3, decimal_places=2, verbose_name=u"偏差值", null=True, blank=True)

    class Meta:
        verbose_name = "公式与偏差表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.label_name


# MLC参数表
class MLC(object):
    MLC_Model = models.CharField(max_length=20, verbose_name=u"MLC型号", default="")
    VaneNumb = models.IntegerField(verbose_name=u"叶片对数", null=True, blank=True)
    Manufacturer = models.CharField(max_length=20, verbose_name=u"生产厂家", null=True, blank=True)
    VaneWidth = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=u'等中心叶片宽度')

    class Meta:
        verbose_name = "MLC参数表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.MLC_Model

