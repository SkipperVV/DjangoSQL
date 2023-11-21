import os
from celery import Celery
from celery.schedules import  crontab

 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projects.settings')
 
app = Celery('Projects')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'Mc_Donalds.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}

app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'Mc_Donalds.tasks.clear_old',
        'schedule': crontab(),
    },
}