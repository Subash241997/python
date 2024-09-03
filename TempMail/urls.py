from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_email_address, name="generate_email"),
    path('receive/', views.receive_email, name="receive"),
    path('inbox/<str:email_address>/', views.view_inbox, name='view_inbox'),
]