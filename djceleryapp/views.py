from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from djceleryapp.tasks import send_email_task






class SendEmailView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        # Extract data from request body
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list')

        if not subject or not message or not recipient_list:
            # Validate required fields
            return Response({'error': 'Missing required fields'}, status=400)

        try:
            # Send email asynchronously using Celery task
            send_email_task.delay(subject, message, recipient_list)
        except Exception as e:
            # Handle task execution errors
            return Response({'error': str(e)}, status=500)

        # Return success response
        return Response({'message': 'Email sent successfully'}, status=200)