from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=NewUserForm()
    return render(request, 'signup.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        usr=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request, username=usr, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username and password aren't correct. Try Again!")
    return render(request, 'login.html')
