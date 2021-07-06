from django.urls import path
from .views import *


urlpatterns = [
    path('', list_typ_sondage, name='list_typ_sondage'),
    path('', list_exploitation_sondage, name='list_exploitation_sondage'),
    path('', list_exploration_sondage, name='list_exploration_sondage'),
]