from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('inf1', views.inf1, name='inf1'),
    path('inf2', views.inf1, name='inf2'),
    path('inf3', views.inf1, name='inf3'),
    path('inf4', views.inf1, name='inf4'),
    path('inf5', views.inf1, name='inf5'),
]