# coding:utf-8
import os

'''
@summary: 用户自定义全局常量设置
'''

# 自定义APP
INSTALLED_APPS_CUSTOM = [
    # add your app here...

    'apps.order',
    'apps.product',
    'apps.user',
    'apps.finance',
    'apps.sln',
    'apps.transfer',
    'apps.import_export',
]

# ===============================================================================
# 日志级别
# ===============================================================================
# 本地开发环境日志级别
LOG_LEVEL_DEVELOP = 'DEBUG'
# 正式环境日志级别
LOG_LEVEL_PRODUCT = os.environ.get('LOG_LEVEL', 'INFO')
