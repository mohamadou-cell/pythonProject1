from django.shortcuts import render
from .models import *

def list_typ_rapport(request):
    conv_typ_rapport = Typ_rapport.objects.all()
    nbr_typ_rapport = conv_typ_rapport.count()

    contexte = {'conv_typ_rapport': conv_typ_rapport, 'nbr_typ_rapport': nbr_typ_rapport}

    return render(request, 'list_typ_rapport.html', contexte)

def list_rapport(request):
    conv_rapport = Rapport.objects.all()
    nbr_rapport = conv_rapport.count()

    contexte = {'conv_rapport': conv_rapport, 'nbr_rapport': nbr_rapport}

    return render(request, 'list_rapport.html', contexte)

def list_liste_rapport(request):
    conv_liste_rapport = Liste_rapport.objects.all()
    nbr_liste_rapport = conv_liste_rapport.count()

    contexte = {'conv_liste_rapport': conv_liste_rapport, 'nbr_liste_rapport': nbr_liste_rapport}

    return render(request, 'list_liste_rapport.html', contexte)
