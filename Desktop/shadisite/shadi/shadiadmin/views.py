from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userstable(request):
    return render(request, 'userstable.html')

def useradd(request):
    return render(request, 'useradd.html')

def useredit(request):
    return render(request, 'useredit.html')

def religion(request):
    return render(request, 'religion.html')

def religionadd(request):
    return render(request, 'religionadd.html')

def religionedit(request):
    return render(request, 'religionedit.html')

def religioncategory(request):
    return render(request, 'religioncategory.html')

def religioncategoryadd(request):
    return render(request, 'religioncategoryadd.html')

def religioncategoryedit(request):
    return render(request, 'religioncategoryedit.html')

def state(request):
    return render(request, 'state.html')

def stateadd(request):
    return render(request, 'stateadd.html')

def stateedit(request):
    return render(request, 'stateedit.html')

def education(request):
    return render(request, 'education.html')

def educationadd(request):
    return render(request, 'educationadd.html')

def educationedit(request):
    return render(request, 'educationedit.html')

def occupation(request):
    return render(request, 'occupation.html')

def occupationadd(request):
    return render(request, 'occupationadd.html')

def occupationedit(request):
    return render(request, 'occupationedit.html')

def mothertongue(request):
    return render(request, 'mothertongue.html')

def mothertongueadd(request):
    return render(request, 'mothertongueadd.html')

def mothertongueedit(request):
    return render(request, 'mothertongueedit.html')