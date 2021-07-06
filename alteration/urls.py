from django.urls import path
from .views import *


urlpatterns = [
    path('', list_typ_alteration, name='list_typ_alteration'),
    path('', list_alteration, name='list_alteration'),
    path('', list_alteration_mineral_rel, name='list_alteration_mineral_rel'),
    path('', list_mineral, name='list_mineral'),
]