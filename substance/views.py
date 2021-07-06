from django.shortcuts import render
from .models import *

def list_substance(request):
    conv_substance = Substance.objects.all()
    nbr_substance = conv_substance.count()

    contexte = {'conv_substance': conv_substance, 'nbr_substance': nbr_substance}

    return render(request, 'list_substance.html', contexte)

def list_extraction(request):
    conv_extraction = Extraction.objects.all()
    nbr_extraction = conv_extraction.count()

    contexte = {'conv_extraction': conv_extraction, 'nbr_extraction': nbr_extraction}

    return render(request, 'list_extraction.html', contexte)

def list_extraction_brut(request):
    conv_extraction_brut = Extraction_brut.objects.all()
    nbr_extraction_brut = conv_extraction_brut.count()

    contexte = {'conv_extraction_brut': conv_extraction_brut, 'nbr_extraction_brut': nbr_extraction_brut}

    return render(request, 'list_extraction_brut.html', contexte)

def list_titre_substance_rel(request):
    conv_titre_substance_rel = Titre_substance_rel.objects.all()
    nbr_titre_substance_rel = conv_titre_substance_rel.count()

    contexte = {'conv_titre_substance_rel': conv_titre_substance_rel, 'nbr_titre_substance_rel': nbr_titre_substance_rel}

    return render(request, 'list_titre_substance_rel.html', contexte)

def list_benefic_typ(request):
    conv_benefic_typ = Benefic_typ.objects.all()
    nbr_benefic_typ = conv_benefic_typ.count()

    contexte = {'conv_benefic_typ': conv_benefic_typ, 'nbr_benefic_typ': nbr_benefic_typ}

    return render(request, 'list_benefic_typ.html', contexte)
