from django.shortcuts import render
from .models import *

def list_pays(request):
    conv_pays = Pays.objects.all()
    nbr_pays = conv_pays.count()

    contexte = {'conv_pays': conv_pays, 'nbr_pays': nbr_pays}

    return render(request, 'list_pays.html', contexte)

def list_region(request):
    conv_region = Region.objects.all()
    nbr_region = conv_region.count()

    contexte = {'conv_region': conv_region, 'nbr_region': nbr_region}

    return render(request, 'list_region.html', contexte)

def list_departement(request):
    conv_departement = Departement.objects.all()
    nbr_departement = conv_departement.count()

    contexte = {'conv_departement': conv_departement, 'nbr_departement': nbr_departement}

    return render(request, 'list_departement.html', contexte)

def list_commune(request):
    conv_commune = Commune.objects.all()
    nbr_commune = conv_commune.count()

    contexte = {'conv_commune': conv_commune, 'nbr_commune': nbr_commune}

    return render(request, 'list_commune.html', contexte)