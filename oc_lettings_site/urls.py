from django.contrib import admin
from django.urls import path , include
from .views import ping
from . import views
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

app_name = 'Profiles' 


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', trigger_error),

    path('lettings' ,include('Lettings.urls')),
    path('profiles' ,include('Profiles.urls')),
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    
]
