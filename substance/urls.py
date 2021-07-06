from django.urls import path
from .views import *


urlpatterns = [
    path('', list_benefic_typ, name='list_benefic_typ'),
    path('', list_extraction, name='list_extraction'),
    path('', list_extraction_brut, name='list_extraction_brut'),
    path('', list_substance, name='list_substance'),
    path('', list_titre_substance_rel, name='list_titre_substance_rel'),
]