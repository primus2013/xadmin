# -*- coding:utf-8 -*-
import xadmin
# from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email']

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        ass = self.new_obj
        pass

    def save_models(self):
        ass=self.new_obj
        pass


# xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
