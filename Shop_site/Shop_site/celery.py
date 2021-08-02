import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Shop_site.settings')

app = Celery('Shop_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-1-minutes':{
        'task':'shop.tasks.cancel',
        'schedule':crontab(minute='*/1440'),
    },
}