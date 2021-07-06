from django.urls import path
from .views import *


urlpatterns = [
    path('', list_typ_analyse, name='list_typ_analyse'),
    path('', list_exploitation_analyse, name='list_exploitation_analyse'),
    path('', list_exploration_analyse, name='list_exploration_analyse'),
]