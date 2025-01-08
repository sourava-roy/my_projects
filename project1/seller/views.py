from django.shortcuts import render

from django.shortcuts import render

def seller_login(request):
    return render(request, 'seller_login.html')

def seller_home(request):
    return render(request, 'seller_home.html')

