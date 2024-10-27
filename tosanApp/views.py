from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request, 'registration/signup.html')

def login_view(request):
    return render(request, 'registration/login.html')

def receiver_dashboard(request):
    return render(request, 'dashboard/receiver.html')