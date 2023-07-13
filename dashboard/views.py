from django.shortcuts import render
import yfinance as yf
# Create your views here.

def dashboard(request):
    user = request.user
    teslaData = yf.Ticker('TSLA').history()
    teslaPrice = teslaData['Close'].iloc[-1]
    return render(request, 'dashboard.html', {'user':user})

