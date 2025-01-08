from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.seller_login, name='seller_login'),
    path('home/', views.seller_home, name='seller_home'),
]
