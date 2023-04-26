from django.contrib import admin
from django.urls import path , include
from .views import ping
from . import views

app_name = 'Profiles' 


urlpatterns = [
    path('', views.index, name='index'),

    path('lettings' ,include('Lettings.urls')),
    path('profiles' ,include('Profiles.urls')),
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),

]
