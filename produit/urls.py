from django.urls import path
from .views import *


urlpatterns = [
    path('', list_produit, name='list_produit'),
    path('', list_exportation, name='list_exportation'),
    path('', list_exportation_brut, name='list_exportation_brut'),
]