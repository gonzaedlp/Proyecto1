from django.contrib import admin
from django.urls import path
from familyApp.views import create_people, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-people/',create_people,name="create_people"),
    path('list-family/',list_family,name="list_familiares"),
]
