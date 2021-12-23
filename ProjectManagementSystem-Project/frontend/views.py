from django.shortcuts import render


def index(request):
    return render(request, 'frontend/auth-signin.html')

def reset_password(request):
    return render(request, 'frontend/forget_password.html')

def newProject(request):
    return render(request, 'frontend/create-project.html')

def myProjects(request):
    return render(request, 'frontend/myprojects.html')

def newTask(request):
    return render(request, 'frontend/create-task.html')

def myTasks(request):
    return render(request, 'frontend/mytasks.html')


def calendar(request):
    return render(request, 'frontend/calendar.html')

def signup(request):
    return render(request, 'frontend/auth-signup.html')
    
def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def member(request):
    return render(request, 'frontend/member.html')

def updateProfile(request):
    return render(request, 'frontend/userProfile.html')

def bugreport(request):
    return render(request, 'frontend/invoices.html')

def bugdetail(request):
    return render(request, 'frontend/bugreports.html')
