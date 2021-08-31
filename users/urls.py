from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    
    path('sitesdata', sitesdata, name='sitesdata'),
    path('gen_data', gen_data, name='gen_data'),
    
]
