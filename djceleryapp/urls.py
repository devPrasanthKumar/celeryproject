from django.urls import path
from . import views
urlpatterns = [
    path('mail/',views.SendEmailView.as_view() ),
]
