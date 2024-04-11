# djceleryapp/__init__.py

from djceleryproject.celery import app as celery_app

__all__ = ['celery_app']
