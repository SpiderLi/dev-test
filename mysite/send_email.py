# _*_coding:utf-8_*_
"""
# @Author  : Guangqiang Li
# @Time    : 2021/7/12 14:52
# @Description:
"""
import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自骚强的邮箱测试',
        '欢迎访问',
        'guangqiangli001@sina.com',
        ['zengyisi@netseekgaming.com'],

