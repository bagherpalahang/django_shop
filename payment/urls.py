from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('request/', views.OrderPayView.as_view(), name='request'),
]