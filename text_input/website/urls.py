from django.urls import path
from .views import home, display


app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('display/', display, name='display'),
]
