# -*- coding:utf-8 -*-
from django import forms


# 需要验证的字段（不能为空和密码长度等）
class LoginForm(forms.Form):
    username = forms.CharField(required=True)     # 名字一定要与前台html的name一致，下同
    password = forms.CharField(required=True, min_length=5)
