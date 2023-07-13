from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
] 