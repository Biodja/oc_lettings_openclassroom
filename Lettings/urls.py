from django.contrib import admin
from django.urls import include, path
from .views import lettings_index , letting



urlpatterns = [
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='lettings'),
    path('', admin.site.urls),
  
]