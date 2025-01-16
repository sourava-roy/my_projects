from django.shortcuts import render
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def handle_suffix(request):
    # Fetch suffixes from GET parameters
    primary_suffix = request.GET.get('primary_suffix', '').strip()
    secondary_suffix = request.GET.get('secondary_suffix', '').strip()

    if not primary_suffix and not secondary_suffix:
        return redirect('home')  # Redirect to home if both are empty
    elif not primary_suffix and secondary_suffix:
        return redirect('login')  # Redirect to login if only primary is empty
    
    return redirect('home')  # Default to home


# Create your views here.
