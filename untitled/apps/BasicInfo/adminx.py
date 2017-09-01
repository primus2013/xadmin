# -*- coding:utf-8 -*-
from BasicInfo.models import *
import xadmin
from xadmin import views


# 在導航欄添加主題更換標簽
class BaseSetting(object):
    enable_themes = True   # 表示需要使用主题功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)


# 修改頁面的題頭和頁脚
class GlobalSettings(object):
    site_title="醫用加速器物理質控項目"
    site_footer="武漢協和腫瘤醫院放療中心"
    menu_style= "accordion"  # 左邊欄樣式

xadmin.site.register(views.CommAdminView, GlobalSettings)

class YyxxAdmin(object):
    list_display = ['yymc', 'chengshi', 'dengj']


# class GlobalSetting(object):
#     # 菜单设置
#     def get_site_menu(self):
#         return (
#             {'title': '投票管理', 'perm': self.get_model_perm(Poll, 'change'), 'menus': (
#                 {'title': '投票', 'url': self.get_model_url(Poll, 'changelist')},
#                 {'title': '选票', 'url': self.get_model_url(Choice, 'changelist')}
#             )},
#         )
#
# xadmin.site.register(views.CommAdminView, GlobalSetting)


xadmin.site.register(Yyxx, YyxxAdmin)
xadmin.site.register(Sbcj)
xadmin.site.register(Sbxx)
xadmin.site.register(Rzxx)
xadmin.site.register(Formula)
xadmin.site.register(MLC)
xadmin.site.register(TPS)


