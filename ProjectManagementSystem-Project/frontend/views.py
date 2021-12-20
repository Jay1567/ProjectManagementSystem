from django.shortcuts import render


def index(request):
    return render(request, 'frontend/auth-signin.html')
def signup(request):
    return render(request, 'frontend/auth-signup.html')
def dashboard(request):
    return render(request, 'frontend/dashboard.html')

