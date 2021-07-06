from django.urls import path
from .views import *


urlpatterns = [
    path('', list_pays, name='list_pays'),
    path('', list_region, name='list_region'),
    path('', list_departement, name='list_departement'),
    path('', list_commune, name='list_commune'),
]