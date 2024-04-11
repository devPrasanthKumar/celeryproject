from django.db import models

# Create your models here.
# myapp/models.py
from django_celery_results.models import TaskResult

class MyTaskResult(TaskResult):
    class Meta:
        proxy = True
        app_label = 'django_celery_results'
