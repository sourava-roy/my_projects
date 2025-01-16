from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_suffix, name='handle_suffix'),
    path('home/', views.home, name='home'),
    path('login/', views.login_page, name='login'),
]
