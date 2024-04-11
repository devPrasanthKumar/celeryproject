from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_task(subject, message, recipient_list):
    # Convert recipient_list to a list if it's a string
    if isinstance(recipient_list, str):
        recipient_list = [recipient_list]

    # Validate recipient_list
    if not isinstance(recipient_list, (list, tuple)):
        raise ValueError('recipient_list must be a list or tuple')

    # Ensure all elements in recipient_list are valid email addresses
    for recipient in recipient_list:
        if not isinstance(recipient, str) or '@' not in recipient:
            raise ValueError(f'Invalid recipient email: {recipient}')

    # Send email using send_mail
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
