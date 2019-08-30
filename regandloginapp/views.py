from django.shortcuts import render
from django.http import HttpResponse
from .models import reg
from .forms import LoginForm
from .forms import RegForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("register successfully")
    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})
def login(request):
    if request.method == 'POST':
        MyLoginForm=login(request.POST)
        if MyLoginForm.is_valid():
            un = MyLoginForm.cleaned_data['user']
            pw = MyLoginForm.cleaned_data['pwd']
            dbuser = reg.objects.filter(user=un , pwd=pw)
            if not dbuser:
                return HttpResponse("login failed")
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
