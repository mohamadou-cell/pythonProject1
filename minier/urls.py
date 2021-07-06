from django.urls import path
from .views import *


urlpatterns = [
    path('', list_cartographie, name='list_cartographie'),
    path('', list_exploratn_details, name='list_exploratn_details'),
    path('', list_geophysique, name='list_geophysique'),
    path('', list_nature_titre_minier, name='list_nature_titre_minier'),
    path('', list_titre_minier, name='list_titre_minier'),
    path('', list_tranchee, name='list_tranchee'),
    path('', list_typ_cartgrph, name='list_typ_cartgrph'),
    path('', list_typ_geochimie, name='list_typ_geochimie'),
    path('', list_typ_geophysique, name='list_typ_geophysique'),
]