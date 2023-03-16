from django.contrib import admin
from django.urls import path , include

from . import views
from Profiles.views import profiles_index , profile
from Lettings.views import lettings_index, letting

app_name = 'Profiles' 


urlpatterns = [
    path('', views.index, name='index'),

    path('lettings' ,include('Lettings.urls')),
    path('profiles' ,include('Profiles.urls')),
    path('admin/', admin.site.urls),

]
