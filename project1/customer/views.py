from django.shortcuts import render

def customer_login(request):
    return render(request, 'customer_login.html')

def customer_home(request):
    return render(request, 'customer_home.html')
