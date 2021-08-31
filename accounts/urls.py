from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', signIn, name='login'),
    path('signup/', signup, name='signup'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
