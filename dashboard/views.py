from django.shortcuts import render
from django.shortcuts import redirect
import yfinance as yf
# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'user':user})
    else:
        return redirect('/login')


