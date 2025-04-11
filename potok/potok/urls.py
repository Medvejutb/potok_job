from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('mainpage', include('mainpage.urls')),
    # path('reserv', include('reserv.urls')),
    path('users', include('users.urls')),
]
