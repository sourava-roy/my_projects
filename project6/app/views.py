from django.shortcuts import render
from .models import StudentData
from django.http import HttpResponse
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        spno = request.POST.get('spno')
        email = request.POST.get('email')
        branch = request.POST.get('branch')
        address = request.POST.get('address')
        # use rname = request.POST.get('username')
        un = request.POST.get('un')
        password = request.POST.get('password')
        SDO=StudentData.objects.create(sname=sname, spno=spno, branch=branch, username=username, password=password)
        SDO.save()
        return HttpResponse("student data saved")
        # return render(request, "")

        # print(sname, spno, branch, username, password)
    return render(request, "register.html")
def search(request):
    if request.method =='POST':
        un = request.POST.get('un')
        all_objects = StudentData.objects.all()
        for i in all_objects:
            if i.username == un:
                uo = i
                print(uo.sname, uo.spno, uo.username, uo.password)
                break
        else:
            return HttpResponse("user not found")

    return render(request, "search.html")
# Create your views here.
