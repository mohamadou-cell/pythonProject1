from django.shortcuts import render
from .models import *

def list_produit(request):
    conv_produit = Produit.objects.all()
    nbr_produit = conv_produit.count()

    contexte = {'conv_produit': conv_produit, 'nbr_produit': nbr_produit}

    return render(request, 'list_produit.html', contexte)

def list_exportation(request):
    conv_exportation = Exportation.objects.all()
    nbr_exportation = conv_exportation.count()

    contexte = {'conv_exportation': conv_exportation, 'nbr_exportation': nbr_exportation}

    return render(request, 'list_exportation.html', contexte)

def list_exportation_brut(request):
    conv_exportation_brut = Exportation_brut.objects.all()
    nbr_exportation_brut = conv_exportation_brut.count()

    contexte = {'conv_exportation_brut': conv_exportation_brut, 'nbr_exportation_brut': nbr_exportation_brut}

    return render(request, 'list_exportation_brut.html', contexte)


