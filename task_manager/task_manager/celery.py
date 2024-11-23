from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configurações padrão do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

app = Celery('task_manager')

# Lê as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente as tarefas em apps instalados
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
