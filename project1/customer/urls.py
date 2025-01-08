from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.customer_login, name='customer_login'),
    path('home/', views.customer_home, name='customer_home'),
]
