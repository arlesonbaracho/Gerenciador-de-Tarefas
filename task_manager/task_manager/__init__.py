from __future__ import absolute_import, unicode_literals

# Importa o app do Celery
from .celery import app as celery_app

__all__ = ('celery_app',)