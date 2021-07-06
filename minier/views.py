from django.shortcuts import render
from .models import *

def list_nature_titre_minier(request):
    conv_nature_titre_minier = Nature_titre_minier.objects.all()
    nbr_nature_titre_minier = conv_nature_titre_minier.count()

    contexte = {'conv_nature_titre_minier': conv_nature_titre_minier, 'nbr_nature_titre_minier': nbr_nature_titre_minier}

    return render(request, 'list_nature_titre_minier.html', contexte)

def list_titre_minier(request):
    conv_titre_minier = Titre_minier.objects.all()
    nbr_titre_minier = conv_titre_minier.count()

    contexte = {'conv_titre_minier': conv_titre_minier, 'nbr_titre_minier': nbr_titre_minier}

    return render(request, 'list_titre_minier.html', contexte)

def list_exploratn_details(request):
    conv_exploratn_details = Exploratn_details.objects.all()
    nbr_exploratn_details = conv_exploratn_details.count()

    contexte = {'conv_exploratn_details': conv_exploratn_details, 'nbr_exploratn_details': nbr_exploratn_details}

    return render(request, 'list_exploratn_details.html', contexte)

def list_tranchee(request):
    conv_tranchee = Tranchee.objects.all()
    nbr_tranchee = conv_tranchee.count()

    contexte = {'conv_tranchee': conv_tranchee, 'nbr_tranchee': nbr_tranchee}

    return render(request, 'list_tranchee.html', contexte)


def list_typ_geophysique(request):
    conv_typ_geophysique = Typ_geophysique.objects.all()
    nbr_typ_geophysique = conv_typ_geophysique.count()

    contexte = {'conv_typ_geophysique': conv_typ_geophysique, 'nbr_typ_geophysique': nbr_typ_geophysique}

    return render(request, 'list_typ_geophysique.html', contexte)

def list_geophysique(request):
    conv_geophysique = Geophysique.objects.all()
    nbr_geophysique = conv_geophysique.count()

    contexte = {'conv_geophysique': conv_geophysique, 'nbr_geophysique': nbr_geophysique}

    return render(request, 'list_geophysique.html', contexte)

def list_typ_geochimie(request):
    conv_typ_geochimie = Typ_geochimie.objects.all()
    nbr_typ_geochimie = conv_typ_geochimie.count()

    contexte = {'conv_typ_geochimie': conv_typ_geochimie, 'nbr_typ_geochimie': nbr_typ_geochimie}

    return render(request, 'list_typ_geochimie.html', contexte)

def list_typ_cartgrph(request):
    conv_typ_cartgrph = Typ_cartgrph.objects.all()
    nbr_typ_cartgrph = conv_typ_cartgrph.count()

    contexte = {'conv_typ_cartgrph': conv_typ_cartgrph, 'nbr_typ_cartgrph': nbr_typ_cartgrph}

    return render(request, 'list_typ_cartgrph.html', contexte)

def list_cartographie(request):
    conv_cartographie = Cartographie.objects.all()
    nbr_cartographie = conv_cartographie.count()

    contexte = {'conv_cartographie': conv_cartographie, 'nbr_cartographie': nbr_cartographie}

    return render(request, 'list_cartographie.html', contexte)
