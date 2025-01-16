from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('address')
        branch = request.POST.get('branch')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        SDO = StudentData(sname = name, spno =pno, email = email, add = add, branch = branch, username=un, password=pw)
        SDO.save()
        return HttpResponse('Registration Successfull....')
    return render(request, 'register.html')

# def search(request):
#     if request.method == 'POST':
#         un = request.POST.get('un')
#         all_objects = StudentData.objects.all()
#         for object in all_objects:
#             if object.username == un:
#                 uo = object
#                 print(uo.username, uo.password, uo.sname, uo.spno, sep='\n')
#                 break
#         else:
#             return HttpResponse('user not found')
#     return render(request, 'search.html')


def search(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        all_objects = StudentData.objects.all()
        for object in all_objects:
            if object.username == un:
                UO = object
                break
        else:
            return HttpResponse('User Not Found')
        d = {'UO': UO}
        return render(request, 'data.html', d)
    return render(request, 'search.html')