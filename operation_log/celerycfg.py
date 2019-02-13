#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fanghuaqing'
__mtime__ = '2018/10/9'
"""
import os

import djcelery
from kombu import Exchange, Queue

djcelery.setup_loader()

RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', '140.143.56.14:35672')

if RABBIT_HOSTNAME.startswith('tcp://'):
    RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]

BROKER_URL = os.environ.get('BROKER_URL', '')
if not BROKER_URL:
    BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
        user=os.environ.get('RABBIT_ENV_USER', 'robo'),
        password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'robo2025'),
        hostname=RABBIT_HOSTNAME,
        vhost=os.environ.get('RABBIT_ENV_VHOST', ''))

# BROKER_URL = 'amqp://robo:robo2025@192.168.2.167:5672/' #连接rabbitmq
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

# 定义一个test交换机
test_exchange = Exchange('test', type='direct')

# 定义一个proc交换机
proc_exchange = Exchange('proc', type='direct')

# 创建三个队列，一个是默认队列，一个是video、一个image
CELERY_QUEUES = (
    Queue('test', test_exchange, routing_key='test'),
    Queue('proc', proc_exchange, routing_key='proc')
)

CELERY_DEFAULT_QUEUE = 'test'
CELERY_DEFAULT_EXCHANGE = 'test_exchange'
CELERY_DEFAULT_ROUTING_KEY = 'test'
#
CELERY_ROUTES = ({'apps.proofing.views.test_post': {
                        'queue': 'test',
                        'routing_key': 'test'
                 }}, {'apps.proofing.views.proc_post': {
                        'queue': 'proc',
                        'routing_key': 'proc'
                 }}, {'apps.transfer.views.test_post': {
                        'queue': 'test',
                        'routing_key': 'test'
                 }}, {'apps.transfer.views.proc_post': {
                        'queue': 'proc',
                        'routing_key': 'proc'
                 }}, )


# redis
# Celery settings
# import djcelery
# djcelery.setup_loader()
#
# BROKER_URL = 'redis://192.168.2.200:6379'
# CELERY_RESULT_BACKEND = 'redis://192.168.2.200:6379'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# # CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_TIMEZONE = 'Asia/Shanghai'
