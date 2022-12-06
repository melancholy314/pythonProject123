from django.urls import path
from . import views

app_name = 'proj'

urlpatterns = [
    path('', views.proj_view, name='projview'),
    path('plswork', views.plswork, name='plswork'),
]