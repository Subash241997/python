from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def loginPage(request):
    context = {
        'title' : 'Login Page',
    }
    return render(request, 'login.html', context)

def signupPage(request):
    context = {
        'title' : 'Signup Page'
    }
    return render(request, 'signup.html', context)

def homePage(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'home.html', context)

def forgetPasswordPage(request):
    context = {
        'title': 'forget password',
    }

    return render(request, 'forgetPassword.html', context)