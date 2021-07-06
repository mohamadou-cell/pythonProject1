from django.shortcuts import render
from .models import *


def list_typ_alteration(request):
    conv_typ_alteration = Typ_alteration.objects.all()
    nbr_typ_alteration = conv_typ_alteration.count()

    contexte = {'conv_typ_alteration': conv_typ_alteration, 'nbr_typ_alteration': nbr_typ_alteration}

    return render(request, 'list_typ_alteration.html', contexte)

def list_alteration(request):
    conv_alteration = Alteration.objects.all()
    nbr_alteration = conv_alteration.count()

    contexte = {'conv_alteration': conv_alteration, 'nbr_alteration': nbr_alteration}

    return render(request, 'list_alteration.html', contexte)

def list_alteration_mineral_rel(request):
    conv_alteration_mineral_rel = Alteration_mineral_rel.objects.all()
    nbr_alteration_mineral_rel = conv_alteration_mineral_rel.count()

    contexte = {'conv_alteration_mineral_rel': conv_alteration_mineral_rel, 'nbr_alteration_mineral_rel': nbr_alteration_mineral_rel}

    return render(request, 'list_alteration_mineral_rel.html', contexte)

def list_mineral(request):
    conv_mineral = Mineral.objects.all()
    nbr_mineral = conv_mineral.count()

    contexte = {'conv_alteration': conv_mineral, 'nbr_alteration': nbr_mineral}

    return render(request, 'list_mineral', contexte)