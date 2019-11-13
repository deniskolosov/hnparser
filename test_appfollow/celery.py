from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('test_appfollow')

app.autodiscover_tasks()
