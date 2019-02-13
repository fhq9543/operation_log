#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fanghuaqing'
__mtime__ = '2018/9/28'
"""
from __future__ import absolute_import

import os
import django

from django.conf import settings
from celery import Celery, platforms

platforms.C_FORCE_ROOT = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'operation_log.settings')
django.setup()

app = Celery('operation_log')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
