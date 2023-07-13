from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserCreationForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/dashboard')
        else:
            pass
            msg = 'Error login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form':form, 'msg':msg})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':form})

def signout(request):
    logout(request)
    return redirect("/login")
    


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        firstName = form.cleaned_data.get("first_name")
        lastName = form.cleaned_data.get("last_name")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        form.save()
        new_user = authenticate(first_name=firstName, last_name=lastName, username=username, email=email, password=password)
        if new_user is not None:
            auth_login(request, new_user)
            return redirect("/dashboard")
        
    else:
        form = SignUpForm()

    context = {
        "form":form
    }
    return render(request, 'signup.html', context)