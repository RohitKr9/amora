from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        data = request.POST
        email = data["email"]
        password = data["password"]
        print(email, password)

        user = authenticate(request, username=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return HttpResponse("REDIRECT TO TEXT")
    
    return render(request, 'login.html')
        
def signupView(request):

    if request.method == 'POST':
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        print(user)
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, 'signup.html')