from django.urls import path
from .views import *


urlpatterns = [
    path('', list_typ_rapport, name='list_typ_rapport'),
    path('', list_rapport, name='list_rapport'),
    path('', list_liste_rapport, name='list_liste_rapport'),
]