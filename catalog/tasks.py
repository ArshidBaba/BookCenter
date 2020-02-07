from celery import shared_task
from django.core.mail import send_mail

from time import sleep

@shared_task
def send_email_task(email):
    sleep(10)
    subject = 'Celery Task Working!'
    message = 'You are a subscriber now'
    sender = 'arshidbaba93@gmail.com',
    
    # print(email)
    # print(type(email))
    # to = str(email)
    # print(type(to))
    # print(to)
    send_mail('Celery Task Working!', 
        'You are a subscriber now', 
        'arshidbaba93@gmail.com', 
        [email])

    return None

# @shared_task
# def send_email_task():
#     sleep(10)
#     send_mail('Celery Task Working!',
#     'This is proof that Celery task worked',
#     'arshidbaba93@gmail.com',
#     ['arshid@hashlearn.com'])

#     return None