from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Task

@shared_task
def send_due_date_reminders():
    today = now().date()
    tasks = Task.objects.filter(due_date=today, is_completed=False)

    for task in tasks:
        send_mail(
            'Lembrete de Tarefa',
            f'Olá, {task.user.username}, sua tarefa "{task.title}" está prevista para hoje!',
            'no-reply@taskmanager.com',
            [task.user.email],
            fail_silently=False,
        )
