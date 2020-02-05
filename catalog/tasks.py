from celery import shared_task
from django.core.mail import send_mail

from time import sleep

@shared_task
def send_email_task(query_text):
    sleep(10)
    send_mail('Celery Task Working!',
    query_text,
    'arshidbaba93@gmail.com',
    ['arshid@hashlearn.com'])

    return None