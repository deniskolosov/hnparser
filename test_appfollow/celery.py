from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    'test_appfollow',
    broker='amqp://',
    backend='amqp://',
    include=['hackernews_parser.tasks']
)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update({
    'result_persistent': True,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})
app.autodiscover_tasks()
