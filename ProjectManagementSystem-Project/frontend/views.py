from django.shortcuts import render


def index(request):
    return render(request, 'frontend/auth-signin.html')

def newProject(request):
    return render(request, 'frontend/create-project.html')

def myProjects(request):
    return render(request, 'frontend/myprojects.html')

def signup(request):
    return render(request, 'frontend/auth-signup.html')
    
def dashboard(request):
    return render(request, 'frontend/dashboard.html')

