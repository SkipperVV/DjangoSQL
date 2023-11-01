import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projects.settings')#'mcdonalds.settings')
 
app = Celery('Mc_Donalds')#('mcdonalds')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()