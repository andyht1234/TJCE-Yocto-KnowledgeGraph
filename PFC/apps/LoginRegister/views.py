from django.shortcuts import render

# Create your views here.
def showlogin(request):
    return render(request,'LoginRegister/login.html')
