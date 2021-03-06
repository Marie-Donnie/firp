# coding=utf-8

import os
import uuid
import datetime

from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core import serializers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from fiches.models import *
from fiches.forms import *
from fiches.functions import Shops


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% GENERAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Displays the first name and last name of the Fiche model
def index(request):
    fiches = Fiche.objects.order_by('-creation')[:16]
    today = datetime.now()
    month = today.month
    birthdays = Fiche.objects.filter(mois_de_naissance__exact=month)
    context = {'latest_fiches': fiches, 'birthdays': birthdays}

    return render(request, 'fiches/index.html', context)


def handler404(request, exception):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler403(request, exception):
    error = 403
    error_text = "Vous n'avez pas accès à cette page."
    context = {'error': error, 'error_text': error_text}
    response = render(request, 'error.html', context)
    response.status_code = 403
    return response

def handler500(request):
    error = 500
    error_text = "Oopsie, il y a un bug sur le site. Merci de le reporter."
    context = {'error': error, 'error_text': error_text}
    response = render(request, 'error.html', context)
    response.status_code = 500
    return response


def conseils(request):
    return render(request, 'fiches/conseils.html', {})

def plus(request):
    return render(request, 'fiches/plus.html', {})


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Displays the username of the users
def users(request):
    users = User.objects.all().order_by('username')
    paginator = Paginator(users, 20)
    page = request.GET.get('page')
    try:
        users_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        users_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        users_list = paginator.page(paginator.num_pages)

    context = {'users_list': users_list}

    return render(request, 'fiches/utilisateurs.html', context)


@login_required
def profile(request):
    if hasattr(request.user, 'infos'):
        profil = User.objects.get(username=request.user).infos
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=profil)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = UserProfileForm(instance=profil)

        return render(request, 'fiches/profil.html', {'form': form})

    else:
        if request.method == 'POST':
            data = request.POST.copy()
            data['user'] = User.objects.get(username=request.user).id
            form = UserProfileForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = UserProfileForm()

        return render(request, 'fiches/profil.html', {'form': form})


def aff_user(request, user_id):
    utilisateur = get_object_or_404(User, pk=user_id)
    user = request.user
    context = {'utilisateur': utilisateur, 'user': user}
    return render(request, 'fiches/utilisateur.html',
                  context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Enables the creation of a Fiche
@login_required
def creer_fiche(request):
    utilisateur = request.user
    # Checks wether user can create another fiche or not
    if ((utilisateur.fiches.count() < 7) or
        (utilisateur.has_perm('fiches.plus_de_15_fiches'))):
        if request.method == 'POST':
            # request.POST is not editable, so we have to copy it to hard code a value
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            # not fdg users are not allowed to have an equipement and detailed inventaire
            if not(utilisateur.has_perm('fiches.equipement_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
                data['gallerie'] = None
            else:
                data['inventaire'] = None
                name = data['prenom']
                data['equipement'] = Equipement.objects.create(nom='Equipement de '+name).id
                data['inventaire_fdg'] = Inventaire.objects.create(nom='Inventaire de '+name).id
                path = "%s/" % (settings.MEDIA_ROOT)
                noms = '%s_%s' % (name, data['nom'])
                data['gallerie'] = GalleriePerso.objects.create(nom_perso=noms).id
            # get the completed form
            form = FicheForm(data, request.FILES)
            if form.is_valid():
                # get the saved form to redirect to the created fiche
                save_it = form.save()
                return redirect('detail_fiche', fiche_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = FicheForm()

        context = {'form': form, 'is_new_fiche': True, 'title_verb': 'Créer'}
        return render(request, 'fiches/formulaire.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire plus de six fiches. Seuls les membres des Fils de Garithos le peuvent.")


# Display the request Fiche
def detail_fiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)
    utilisateur = request.user
    if fiche.inventaire_fdg:
        if (fiche.inventaire_fdg.cases.count() < 30):
            nb = 30 - fiche.inventaire_fdg.cases.count()
        else:
            nb = 0
    else:
        nb = 0

    if fiche.equipement:
        mp, emp = fiche.equipement.get_mp()
        am, eam = fiche.equipement.get_am()
        aa, eaa = fiche.equipement.get_autre_arme()
        tete, etete = fiche.equipement.get_tete()
        epaules, eepaules = fiche.equipement.get_epaules()
        torse, etorse = fiche.equipement.get_torse()
        mains, emains = fiche.equipement.get_mains()
        taille, etaille = fiche.equipement.get_taille()
        jambes, ejambes = fiche.equipement.get_jambes()
        dos, edos = fiche.equipement.get_dos()
        cou, ecou = fiche.equipement.get_cou()
        poignets, epoignets = fiche.equipement.get_poignets()
        pieds, epieds = fiche.equipement.get_pieds()
        doigts = fiche.equipement.get_doigts()
        divers = fiche.equipement.get_divers()
        effets, effets_ig, force, intell, agi, armure, runique, terradiance, resist = fiche.equipement.effets()
    else:
        mp, am, aa, tete, epaules, torse = None, None, None, None, None, None
        mains, taille, jambes, dos, cou = None, None, None, None, None
        poignets, doigts, divers = None, None, None
        effets, effets_ig, force = None, None, None
        intell, agi, armure = None, None, None
        pieds, runique, terradiance, resist = None, None, None, 0
        emp, eam, eaa, etete, eepaules = None, None, None, None, None
        etorse, emains, etaille, ejambes = None, None, None, None
        edos, ecou, epoignets, epieds = None, None, None, None
    if fiche.gallerie:
        images = fiche.gallerie.image.all()
    else:
        images = None
    context = {'fiche': fiche,
               'range': range(nb), 'effets': effets, 'effets_ig': effets_ig,
               'force': force, 'intell': intell, 'agi': agi,
               'armure': armure, 'mp': mp, 'am': am, 'aa': aa, 'tete': tete,
               'epaules': epaules, 'torse': torse, 'mains': mains,
               'taille': taille, 'jambes': jambes, 'dos': dos, 'cou': cou,
               'poignets': poignets, 'doigts': doigts, 'divers': divers,
               'pieds': pieds, 'runique': runique, 'terradiance': terradiance,
               'emp': emp, 'eam': eam, 'eaa': eaa, 'etete': etete, 'eepaules': eepaules,
               'etorse': etorse, 'emains': emains, 'etaille': etaille, 'ejambes': ejambes,
               'edos': edos, 'ecou': ecou, 'epoignets': epoignets, 'epieds': epieds,
               'utilisateur': utilisateur, 'images': images, 'resist': resist,
               'pretty_relations': pretty_print_relations(fiche.id)}
    return render(request, 'fiches/detail.html', context)


@login_required
def edit_fiche(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    utilisateur = request.user
    if utilisateur == fiche.createur:
        if request.method == 'POST':
            data = request.POST.copy()
            # Adds creator directly because the field is hidden
            data['createur'] = User.objects.get(username=utilisateur).id
            if (fiche.bourse):
                data['bourse'] = fiche.bourse.id
            """
            Disables useless fields and creates the required ones depending
            on the authorization of the user
            """
            if not(utilisateur.has_perm('fiches.equipement_ok') and
                   utilisateur.has_perm('fiches.inventaire_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
            else:
                data['inventaire'] = None
                name = data['prenom']
                if fiche.equipement and fiche.inventaire_fdg :
                    data['equipement'] = fiche.equipement.id
                    data['inventaire_fdg'] = fiche.inventaire_fdg.id
                else:
                    if not fiche.equipement:
                        data['equipement'] = Equipement.objects.create(nom='Equipement de '+name).id
                    if not fiche.inventaire_fdg:
                        data['inventaire_fdg'] = Inventaire.objects.create(nom='Inventaire de '+name).id
                if fiche.gallerie :
                    data['gallerie'] = fiche.gallerie.id
                else:
                    noms = '%s_%s' % (name, data['nom'])
                    data['gallerie'] = GalleriePerso.objects.create(nom_perso=noms).id
            # Remove the previous image if a new one is uploaded
            if 'image' in request.FILES:
                path = "%s/" % (settings.MEDIA_ROOT)
                fichier = os.path.join(path, fiche.image.name)
                if fiche.image.name != "images/site/no-image.png":
                    os.remove(fichier)
            form = FicheForm(data, request.FILES, instance=fiche)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_fiche', fiche_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = FicheForm(instance=fiche)

        equipements = Equipement.objects.all()
        inventaires = Inventaire.objects.all()
        context = {'form': form, 'equipements': equipements,
                   'inventaires': inventaires,
                   'is_new_fiche': False,
                   'title_verb': 'Éditer' }

        return render(request, 'fiches/formulaire.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer cette fiche.")


# Helper for live edit of Fiche textareas
def edit_fiche_field(field, request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user.id != fiche.createur.id and not request.user.has_perm('fiches.admin'):
        return HttpResponse(status=403)

    if request.method != 'POST':
        return HttpResponse(status=405)

    # Update the text
    setattr(fiche, field, request.POST['content'])
    fiche.save(update_fields=[field])
    return HttpResponse(status=200)

# API point to edit a fiche 'description'
@permission_required('fiches.fdg', raise_exception=True)
def edit_fiche_description(request, fiche_id):
    return edit_fiche_field('description', request, fiche_id)

# API point to edit a fiche 'historique'
@permission_required('fiches.fdg', raise_exception=True)
def edit_fiche_historique(request, fiche_id):
    return edit_fiche_field('historique', request, fiche_id)

# API point to edit a fiche 'relations'
@permission_required('fiches.fdg', raise_exception=True)
def edit_fiche_relations(request, fiche_id):
    edit_fiche_field('relations', request, fiche_id)
    context = { 'pretty_relations': pretty_print_relations(fiche_id) }
    return render(request, 'fiches/relation_pretty.html', context)

# API point to edit a fiche 'competences'
@permission_required('fiches.fdg', raise_exception=True)
def edit_fiche_competences(request, fiche_id):
    return edit_fiche_field('competences', request, fiche_id)

# API point to edit a fiche 'medailles'
@permission_required('fiches.fdg', raise_exception=True)
def edit_fiche_medailles(medailles, fiche_id):
    return edit_fiche_field('medailles', request, fiche_id)


def pretty_print_relations(fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    relations_finale = []
    if fiche.relations:
        relations_split = [str.strip() for str in fiche.relations.splitlines()]
        for relation in relations_split:
            exists = False
            relation_name = relation
            relation_link = None
            if relation.startswith('#'):
                number, name = relation[1:].split(' ', maxsplit=1)
                #number = relation[1:].split(' ', maxsplit=1)[0]
                #leftovers = relation[1:].split(' ', maxsplit=1)[1]
                if number.isdecimal():
                    try:
                        relation_link = Fiche.objects.get(pk=number)
                        relation_name = name
                        exists = True
                    except ObjectDoesNotExist:
                        pass
            relations_finale.append({'exists': exists,
                                     'name': relation_name,
                                     'link': relation_link})
    return relations_finale


def pretty_print_membres(famille_id):
    famille = Famille.objects.get(pk=fiche_id)
    membres_finale = []
    if famille.membres:
        membres_split = [str.strip() for str in famille.membres.splitlines()]
        for membre in membres_split:
            exists = False
            membre_name = membre
            membre_link = None
            if relation.startswith('#'):
                number, name = relation[1:].split(' ', maxsplit=1)
                #number = relation[1:].split(' ', maxsplit=1)[0]
                #leftovers = relation[1:].split(' ', maxsplit=1)[1]
                if number.isdecimal():
                    try:
                        membre_link = Fiche.objects.get(pk=number)
                        relation_name = name
                        exists = True
                    except ObjectDoesNotExist:
                        pass
            membres_finale.append({'exists': exists,
                                   'name': membre_name,
                                   'link': membre_link})
    return membres_finale


@login_required
def delete_fiche(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur:
        context = {'fiche': fiche}
        if request.method == 'POST':
            # remove profile image
            path = "%s/" % (settings.MEDIA_ROOT)
            fichier = os.path.join(path, fiche.image.name)
            if fiche.image.name != "images/site/no-image.png":
                os.remove(fichier)
            if fiche.inventaire_fdg:
                fiche.inventaire_fdg.delete()
            if fiche.bourse:
                fiche.bourse.delete()
            if fiche.equipement:
                fiche.equipement.delete()
            fiche.delete()
            return render(request, 'fiches/fiche_supprimee.html', context)
        else:
            return render(request, 'fiches/confirmation_suppression.html', context)
    else:
        return HttpResponse("Vous ne pouvez pas supprimer cette fiche.")


# Displays the list of all characters
def personnages(request):
    # fiches = Fiche.objects.order_by('nom', 'prenom')
    context = {}
    if request.method == 'GET' and 'valeur' in request.GET and 'recherche' in request.GET:
        if 'recherche' is not None and 'recherche' != '':
            valeur = request.GET.get('valeur')
            recherche = request.GET.get('recherche')
            Qr = None
            q = Q(**({"%s__icontains" % recherche: valeur }))
            if Qr:
                Qr = Qr | q # or & for filtering
            else:
                Qr = q
            # this you can now combine with other filters, exclude etc.
            fiches_list = Fiche.objects.filter(Qr)
            context['recherche'] = recherche
            context['valeur'] = valeur
        else:
            recherche = None
            fiches_list = Fiche.objects.order_by('-pj', 'nom', 'prenom')

    else:
        recherche = None
        fiches_list = Fiche.objects.order_by('-pj', 'nom', 'prenom')

    paginator = Paginator(fiches_list, 12)
    page = request.GET.get('page')
    try:
        fiches = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        fiches = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        fiches = paginator.page(paginator.num_pages)

    context = {'fiches': fiches, 'recherche': recherche}

    return render(request, 'fiches/personnages.html', context)

# unused
@login_required
def fiche_search(request):
    valeur = request.GET.get('valeur')
    recherche = request.GET.get('recherche')
    Qr = None
    q = Q(**({"%s__icontains" % recherche: valeur }))
    if Qr:
          Qr = Qr | q # or & for filtering
    else:
          Qr = q
    # this you can now combine with other filters, exclude etc.
    fiches_list = Fiche.objects.filter(Qr)

    paginator = Paginator(fiches_list, 20)
    page = request.GET.get('page')
    try:
        fiches = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        fiches = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        fiches = paginator.page(paginator.num_pages)

    context = {'fiches': fiches}

    return render(request, 'fiches/personnages.html', context)


@login_required
def mes_persos(request):
    utilisateur = get_object_or_404(User, pk=request.user.id)
    user = request.user
    context = {'utilisateur': utilisateur, 'user': user}
    return render(request, 'fiches/mes_personnages.html',
                  context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_gallerie(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur and not fiche.gallerie:
        path = "%s/" % (settings.MEDIA_ROOT)
        noms = '%s_%s' % (fiche.prenom, fiche.nom)
        gallerie_creee = GalleriePerso.objects.create(nom_perso=noms)
        fiche.gallerie = gallerie_creee
        fiche.save()
        return redirect('detail_fiche', fiche_id=fiche_id)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def image_perso(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur:
        if request.method == 'POST':
            data = request.POST.copy()
            noms = '%s_%s' % (fiche.prenom, fiche.nom)
            data['nom_perso'] = ''.join(e for e in noms if e.isalnum())
            data['gallerie'] = fiche.gallerie.id
            form = ImagePersoForm(data, request.FILES)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_fiche', fiche_id=fiche_id)
            else:
                print(form.errors)
        else:
            form = ImagePersoForm()
        context = {'form': form, 'fiche': fiche}
        return render(request, 'fiches/image.html', context)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def upload_gallery_perso(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur:
        context = {'fiche': fiche}
        images = fiche.gallerie.image.all()
        context = {'images_list': images, 'fiche': fiche}
        return render(request, 'fiches/up_gallery.html', context)
    else:
        return HttpResponse(status=403)


@login_required
def creer_famille(request):
    utilisateur = request.user
    # Checks wether user can create another fiche or not
    if utilisateur.has_perm('fiches.plus_de_15_fiches'):
        if request.method == 'POST':
            # request.POST is not editable, so we have to copy it to hard code a value
            data = request.POST.copy()
            # get the completed form
            form = FamilleForm(data, request.FILES)
            if form.is_valid():
                # get the saved form to redirect to the created fiche
                save_it = form.save()
                return redirect('famille', famille_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = FamilleForm()

        context = {'form': form}
        return render(request, 'fiches/famille.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire de famille. Seuls les membres des Fils de Garithos le peuvent.")


# Displays the families
def familles(request):
    context = {}
    familles = Familles.objects.order_by('nom')

    context = {'familles': familles}

    return render(request, 'fiches/familles.html', context)

# Display the request Fiche
def famille(request, famille_id):
    famille = get_object_or_404(Famille, pk=famille_id)

    context = {'famille': famille,
               'pretty_membres': pretty_print_membres(famille.id)}
    return render(request, 'familles/detail.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


@permission_required('fiches.fdg', raise_exception=True)
def creer_objet(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['createur'] = User.objects.get(username=request.user).id
        url = data['image_url']
        if url.endswith('.PNG'):
            url = url[:-4]
            data['image_url'] = url
        form = ObjetForm(data, request.FILES)
        if form.is_valid():
            save_it = form.save()
            return redirect('detail_objet', objet_id=save_it.id)
        else:
            print(form.errors)
    else:
        form = ObjetForm()

    return render(request, 'fiches/objet.html', {'form': form})



@permission_required('fiches.fdg', raise_exception=True)
def creer_armure(request):
    if request.method == 'POST':
        form = ArmureForm(request.POST, request.FILES)
        if form.is_valid():
            save_it = form.save()
            return redirect('detail_armure', armure_id=save_it.id)
        else:
            print(form.errors)
    else:
        form = ArmureForm()

    objets = Objet.objects.filter(createur=request.user)
    enchantements = Enchantement.objects.all()
    context = {'form': form, 'objets': objets,
               'enchantements': enchantements}
    return render(request, 'fiches/armure.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def copier_armure(request, armure_id):
    armure = Armure.objects.get(pk=armure_id)
    objet = armure.objet
    objet.pk = None
    objet.save()
    armure.pk = None
    armure.objet = objet
    armure.save()
    return redirect('detail_armure', armure_id=armure.id)


@permission_required('fiches.fdg', raise_exception=True)
def creer_case(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['createur'] = User.objects.get(username=request.user).id
        form = CaseForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = CaseForm()

    objets = Objet.objects.all()
    context = {'form': form, 'objets': objets}
    return render(request, 'fiches/case.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_case_perso(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user.id == fiche.createur.id:
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            form = CaseForm(data)
            if form.is_valid():
                save_it = form.save()
                #case = Case.objects.get(pk=save_it)
                fiche.inventaire_fdg.cases.add(save_it)
                return redirect('detail_fiche', fiche_id=fiche_id)
            else:
                print(form.errors)
        else:
            form = CaseForm()

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/case.html', context)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def creer_inventaire(request):
    if request.method == 'POST':
        form = InventaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = InventaireForm()

    cases = Case.objects.filter(createur=request.user)
    context = {'form': form, 'cases': cases}

    return render(request, 'fiches/inventaire.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_equipement(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = EquipementForm()

    objets = Armure.objects.all()
    context = {'form': form, 'objets': objets}

    return render(request, 'fiches/equipement.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def objets(request):
    objets_list = Objet.objects.order_by('nom')

    paginator = Paginator(objets_list, 20)
    page = request.GET.get('page')
    try:
        objets = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        objets = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        objets = paginator.page(paginator.num_pages)

    context = {'objets': objets}

    return render(request, 'fiches/objets.html', context)


def detail_objet(request, objet_id):
    objet = get_object_or_404(Objet, pk=objet_id)
    context = {'objet': objet}
    return render(request, 'fiches/aff_objet.html', context)


def detail_armure(request, armure_id):
    armure = get_object_or_404(Armure, pk=armure_id)
    objet = armure.objet
    context = {'armure': armure, 'objet': objet}
    return render(request, 'fiches/aff_armure.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def edit_objet(request, objet_id):
    objet = Objet.objects.get(pk=objet_id)
    if request.user.id == objet.createur.id :
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            url = data['image_url']
            if url.endswith('.PNG'):
                url = url[:-4]
                data['image_url'] = url
            form = ObjetForm(data, request.FILES, instance=objet)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_objet', objet_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ObjetForm(instance=objet)

        context = {'form': form}

        return render(request, 'fiches/objet.html', context)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def delete_objet(request, objet_id):
    objet = Objet.objects.get(pk=objet_id)
    if request.user == objet.createur:
        # check if an object is associated with an armor
        a_armure =  objet.has_equipement()
        proprietaires_equipements = []
        proprietaires_inventaires = []
        # if there is an armor, we want to return every character
        # that has this particular armor in their equipement
        if a_armure and objet.armure.equipement:
            # we first list all equipements that have this armor
            # object and armor are linked by a one to one relationship,
            # so we can get the armor directly from the object
            # armor and equipement are linked by a many to many relationship,
            # so we have to get a query set of equipements for a particular armor
            equipements = list(objet.armure.equipement.all())
            # then we get the owner of these equipements
            for e in equipements:
            # equipement and characters are linked by a one to one relationship,
            # so for each equipement we can find the corresponding character (fiche)
                proprietaires_equipements += list(Fiche.objects.filter(equipement=e))
        # same for the inventory, as an object can also be in an inventory as it is
        cases = list(Case.objects.filter(objet=objet))
        inventaires = []
        if len(cases) > 0:
            for c in cases:
                inventaires += list(c.inventaire.all())
            for i in inventaires:
                proprietaires_inventaires += list(Fiche.objects.filter(inventaire_fdg=i))
        context = {'objet': objet,
                   'proprietaires_equipements': proprietaires_equipements,
                   'proprietaires_inventaires': proprietaires_inventaires}
        if request.method == 'POST':
            if a_armure:
                objet.armure.delete()
            objet.delete()
            return render(request, 'fiches/objet_supprime.html', context)
        else:
            return render(request, 'fiches/confirmation_suppression_objet.html', context)
    else:
        return HttpResponse("Vous ne pouvez pas supprimer cet objet.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_armure(request, armure_id):
    armure = Armure.objects.get(pk=armure_id)
    if request.user.id == armure.objet.createur.id :
        if request.method == 'POST':
            form = ArmureForm(request.POST, instance=armure)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_armure', armure_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ArmureForm(instance=armure)

        objets = Objet.objects.filter(createur=request.user)
        enchantements = Enchantement.objects.all()
        context = {'form': form, 'objets': objets,
                   'enchantements': enchantements}
        return render(request, 'fiches/armure.html', context)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def edit_case(request, case_id):
    case = Case.objects.get(pk=case_id)
    if request.user.id == case.createur.id :
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            form = CaseForm(data, instance=case)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                print(form.errors)
        else:
            form = CaseForm(instance=case)

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/case.html', context)
    else:
        return HttpResponse(status=403)


# API point to edit the cardinality of an object in a cell
@permission_required('fiches.fdg', raise_exception=True)
def edit_case_number(request, case_id, valeur):
    case = Case.objects.get(pk=case_id)
    if request.user.id == case.createur.id or request.user.has_perm('fiches.admin'):
        if request.method == 'POST':
            # update the values of the cell number
            if int(valeur) < 1:
                return HttpResponse(status=406)
            case.nombre = valeur
            case.save(update_fields=['nombre'])
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def delete_case(request, case_id):
    try:
        case = Case.objects.get(pk=case_id)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    if request.user.id == case.createur.id or request.user.has_perm('fiches.admin'):
        if request.method == 'DELETE':
            case.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=403)

@permission_required('fiches.fdg', raise_exception=True)
def edit_inventaire(request, inventaire_id):
    inventaire = Inventaire.objects.get(pk=inventaire_id)
    if request.method == 'POST':
        form = InventaireForm(request.POST, instance=inventaire)
        if form.is_valid():
            save_it = form.save()
            fiche = Fiche.objects.get(inventaire_fdg=save_it.id)
            return redirect('detail_fiche', fiche_id=fiche.id)
        else:
            print(form.errors)
    else:
        form = InventaireForm(instance=inventaire)

    cases_perso = inventaire.cases.all()
    cases = Case.objects.filter(createur=request.user)
    context = {'form': form, 'cases': cases, 'cases_perso': cases_perso}
    return render(request, 'fiches/inventaire.html', context)


@login_required
def edit_equipement(request, equipement_id):
    equipement = Equipement.objects.get(pk=equipement_id)
    if request.user.has_perm('fiches.change_equipement'):
        if request.method == 'POST':
            form = EquipementForm(request.POST, instance=equipement)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                print(form.errors)
        else:
            form = EquipementForm(instance=equipement)

        objets = Armure.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/equipement.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer les equipements.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_equip(request, equipement_id):
    equipement = Equipement.objects.get(pk=equipement_id)
    if request.method == 'POST':
        re = request.POST.copy()
        re.pop('objets')
        re.pop('enchantements')
        if re.__contains__('mp') and re.__getitem__('mp') != '':
            re.appendlist('objets', re.__getitem__('mp'))
        if re.__contains__('am') and re.__getitem__('am') != '':
            re.appendlist('objets', re.__getitem__('am'))
        if re.__contains__('aa') and re.__getitem__('aa') != '':
            re.appendlist('objets', re.__getitem__('aa'))
        if re.__contains__('tete') and re.__getitem__('tete') != '':
            re.appendlist('objets', re.__getitem__('tete'))
        if re.__contains__('epaule') and re.__getitem__('epaule') != '':
            re.appendlist('objets', re.__getitem__('epaule'))
        if re.__contains__('torse') and re.__getitem__('torse') != '':
            re.appendlist('objets', re.__getitem__('torse'))
        if re.__contains__('main') and re.__getitem__('main') != '':
            re.appendlist('objets', re.__getitem__('main'))
        if re.__contains__('taille') and re.__getitem__('taille') != '':
            re.appendlist('objets', re.__getitem__('taille'))
        if re.__contains__('jambe') and re.__getitem__('jambe') != '':
            re.appendlist('objets', re.__getitem__('jambe'))
        if re.__contains__('do') and re.__getitem__('do') != '':
            re.appendlist('objets', re.__getitem__('do'))
        if re.__contains__('cou') and re.__getitem__('cou') != '':
            re.appendlist('objets', re.__getitem__('cou'))
        if re.__contains__('poignet') and re.__getitem__('poignet') != '':
            re.appendlist('objets', re.__getitem__('poignet'))
        if re.__contains__('pied') and re.__getitem__('pied') != '':
            re.appendlist('objets', re.__getitem__('pied'))
        if re.__contains__('doigt') and re.__getitem__('doigt') != '':
            doigts = re.getlist('doigt')
            for doigt in doigts:
                re.appendlist('objets', doigt)
        if re.__contains__('diver') and re.__getitem__('diver') != '':
            divers = re.getlist('diver')
            for diver in divers:
                re.appendlist('objets', diver)
        if re.__contains__('emp') and re.__getitem__('emp') != '':
            re.appendlist('enchantements', re.__getitem__('emp'))
        if re.__contains__('eam') and re.__getitem__('eam') != '':
            re.appendlist('enchantements', re.__getitem__('eam'))
        if re.__contains__('eaa') and re.__getitem__('eaa') != '':
            re.appendlist('enchantements', re.__getitem__('eaa'))
        if re.__contains__('etete') and re.__getitem__('etete') != '':
            re.appendlist('enchantements', re.__getitem__('etete'))
        if re.__contains__('eepaule') and re.__getitem__('eepaule') != '':
            re.appendlist('enchantements', re.__getitem__('eepaule'))
        if re.__contains__('etorse') and re.__getitem__('etorse') != '':
            re.appendlist('enchantements', re.__getitem__('etorse'))
        if re.__contains__('emain') and re.__getitem__('emain') != '':
            re.appendlist('enchantements', re.__getitem__('emain'))
        if re.__contains__('etaille') and re.__getitem__('etaille') != '':
            re.appendlist('enchantements', re.__getitem__('etaille'))
        if re.__contains__('ejambe') and re.__getitem__('ejambe') != '':
            re.appendlist('enchantements', re.__getitem__('ejambe'))
        if re.__contains__('edo') and re.__getitem__('edo') != '':
            re.appendlist('enchantements', re.__getitem__('edo'))
        if re.__contains__('ecou') and re.__getitem__('ecou') != '':
            re.appendlist('enchantements', re.__getitem__('ecou'))
        if re.__contains__('epoignet') and re.__getitem__('epoignet') != '':
            re.appendlist('enchantements', re.__getitem__('epoignet'))
        if re.__contains__('epied') and re.__getitem__('epied') != '':
            re.appendlist('enchantements', re.__getitem__('epied'))
        form = EquipementForm(re, instance=equipement)
        if form.is_valid():
            save_it = form.save()
            fiche = Fiche.objects.get(equipement=save_it.id)
            return redirect('detail_fiche', fiche_id=fiche.id)
        else:
            print(form.errors)
    else:
        form = EquipementForm(instance=equipement)

    objets = Armure.objects.all()
    mps = Armure.objects.filter(membre=1)
    emps = Enchantement.objects.filter(membre=1)
    ams = Armure.objects.filter(membre=2)
    eams = Enchantement.objects.filter(membre=2)
    aas = Armure.objects.filter(membre=15)
    eaas = Enchantement.objects.filter(membre=15)
    tetes = Armure.objects.filter(membre=3)
    etetes = Enchantement.objects.filter(membre=3)
    epaules = Armure.objects.filter(membre=4)
    eepaules = Enchantement.objects.filter(membre=4)
    torses = Armure.objects.filter(membre=5)
    etorses = Enchantement.objects.filter(membre=5)
    mains = Armure.objects.filter(membre=6)
    emains = Enchantement.objects.filter(membre=6)
    tailles = Armure.objects.filter(membre=7)
    etailles = Enchantement.objects.filter(membre=7)
    jambes = Armure.objects.filter(membre=8)
    ejambes = Enchantement.objects.filter(membre=8)
    dos = Armure.objects.filter(membre=10)
    edos = Enchantement.objects.filter(membre=10)
    cous = Armure.objects.filter(membre=11)
    ecous = Enchantement.objects.filter(membre=11)
    poignets = Armure.objects.filter(membre=13)
    epoignets = Enchantement.objects.filter(membre=13)
    pieds = Armure.objects.filter(membre=9)
    epieds = Enchantement.objects.filter(membre=9)
    doigts = Armure.objects.filter(membre=12)
    edoigts = Enchantement.objects.filter(membre=12)
    divers = Armure.objects.filter(membre=14)
    edivers = Enchantement.objects.filter(membre=14)
    context = {'form': form, 'objets': objets, 'mps': mps,
               'ams': ams, 'aas': aas, 'tetes': tetes,
               'epaules': epaules, 'torses': torses, 'mains': mains,
               'tailles': tailles, 'jambes': jambes, 'dos': dos,
               'cous': cous, 'poignets': poignets, 'pieds': pieds,
               'doigts': doigts, 'divers': divers,
               'eams': eams, 'eaas': eaas, 'etetes': etetes, 'emps': emps,
               'eepaules': eepaules, 'etorses': etorses, 'emains': emains,
               'etailles': etailles, 'ejambes': ejambes, 'edos': edos,
               'ecous': ecous, 'epoignets': epoignets, 'epieds': epieds,
               'edoigts': edoigts, 'edivers': edivers}
    return render(request, 'fiches/equip_edit.html', context)


def tooltip_objet(request, objet_id):
    objet = get_object_or_404(Objet, pk=objet_id)
    context = {'objet': objet}
    return render(request, 'fiches/tooltip_objet.html', context)


def tooltip_armure(request, armure_id, enchant_id=None):
    armure = get_object_or_404(Armure, pk=armure_id)
    objet = armure.objet
    if enchant_id:
        enchant= get_object_or_404(Enchantement, pk=enchant_id)
    else:
        enchant = None
    context = {'armure': armure, 'objet': objet, 'enchant': enchant}
    return render(request, 'fiches/tooltip_armure.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_enchantement(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['createur'] = User.objects.get(username=request.user).id
        form = EnchantementForm(data, request.FILES)
        if form.is_valid():
            save_it = form.save()
            return redirect('detail_enchantement', enchantement_id=save_it.id)
        else:
            print(form.errors)
    else:
        form = EnchantementForm()

    context = {'form': form,}

    return render(request, 'fiches/enchantement.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def edit_enchantement(request, enchantement_id):
    enchantement = Enchantement.objects.get(pk=enchantement_id)
    if request.user.id == enchantement.createur.id :
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            form = EnchantementForm(data, instance=enchantement)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_enchantement', enchantement_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = EnchantementForm(instance=enchantement)

        context = {'form': form}
        return render(request, 'fiches/enchantement.html', context)
    else:
        return HttpResponse(status=403)


@permission_required('fiches.fdg', raise_exception=True)
def objets_enchantements(request):
    utilisateur = get_object_or_404(User, pk=request.user.id)
    user = request.user
    context = {'utilisateur': utilisateur, 'user': user}
    return render(request, 'fiches/objets_enchants.html',
                  context)


def detail_enchantement(request, enchantement_id):
    enchantement = get_object_or_404(Enchantement, pk=enchantement_id)
    context = {'enchantement': enchantement}
    return render(request, 'fiches/aff_enchantement.html', context)




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUETES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

# Display list of quests
def quetes(request):
    quetes = Quete.objects.all().order_by('etat', 'creation', 'difficulte', 'nom')
    paginator = Paginator(quetes, 8)
    page = request.GET.get('page')
    try:
        quetes_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        quetes_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        quetes_list = paginator.page(paginator.num_pages)

    context = {'quetes': quetes, 'quetes_list': quetes_list}

    return render(request, 'site/quetes.html', context)


# Display quest
def quete(request, quete_id):
    quete = get_object_or_404(Quete, pk=quete_id)

    context = {'quete': quete}

    return render(request, 'site/quete.html', context)


# Enables the reservation of a quest by players
@permission_required('fiches.fdg', raise_exception=True)
def res_quete(request, quete_id):
    quete = get_object_or_404(Quete, pk=quete_id)

    if request.method == 'POST':
        data = request.POST.copy()
        # Puts the quest to the "reserved" state (2)
        data['etat'] = 2
        form = PrendreQueteForm(data, instance=quete)
        if form.is_valid():
            save_it = form.save()
            return redirect('quete', quete_id=save_it.id)
        else:
            print(form.errors)
    else:
        form = PrendreQueteForm(instance=quete)

    personnages = request.user.fiches.all()
    context = {'form': form, 'quete': quete, 'personnages': personnages}
    return render(request, 'site/prendre_quete.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% GALLERIE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# Display icon gallery
from os import listdir
from os import walk
@permission_required('fiches.allie', raise_exception=True)
def gallery(request):
    images_url = "%s/images/ICONS" % (settings.MEDIA_ROOT)
    images = listdir(images_url)
    # Sorts images independently of case
    images_sorted = sorted(images, key=str.lower)
    paginator = Paginator(images_sorted, 100)
    page = request.GET.get('page')
    try:
        images_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        images_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        images_list = paginator.page(paginator.num_pages)
    recherche = None
    context = {'images_list': images_list, 'recherche': recherche}
    return render(request, 'site/gallery.html', context)


# Enables the search of an icon
@permission_required('fiches.allie', raise_exception=True)
def gallery_search(request):
    recherche = request.GET.get('recherche')
    images_url = "%s/images/ICONS" % (settings.MEDIA_ROOT)
    images = []
    """
    Adds every files matching the name given to the returned list,
    checking everything in lower case
    """
    for root, dirs, files in walk(images_url):
        for name in files:
            if recherche.lower() in name.lower():
                images += [name]
    images_sorted = sorted(images, key=str.lower)
    paginator = Paginator(images_sorted, 100)
    page = request.GET.get('page')
    try:
        images_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        images_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        images_list = paginator.page(paginator.num_pages)

    context = {'images_list': images_list, 'recherche': recherche}
    return render(request, 'site/gallery.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CAMPAGNES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# Displays campaigns
def campagnes(request):
    campagnes = Operation.objects.all().order_by('-id')
    paginator = Paginator(campagnes, 8)
    page = request.GET.get('page')
    try:
        campagnes_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        campagnes_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        campagnes_list = paginator.page(paginator.num_pages)

    context = {'campagnes': campagnes, 'campagnes_list': campagnes_list}

    return render(request, 'site/campagnes.html', context)


# Display requested campaign
def campagne(request, campagne_id):
    campagne = get_object_or_404(Operation, pk=campagne_id)
    missions = Mission.objects.filter(operation=campagne).order_by('numero')
    paginator = Paginator(missions, 8)
    page = request.GET.get('page')
    try:
        missions_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        missions_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        missions_list = paginator.page(paginator.num_pages)
    context = {'campagne': campagne, 'missions_list': missions_list}

    return render(request, 'site/campagne.html', context)


# Displays report of the requested mission
def mission(request, campagne_id, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    image = None
    sign = mission.signature_url
    if sign.startswith( 'i: ' ):
        sign = sign[3:]
        image = get_object_or_404(Image, nom=sign)
    count = len(mission.deroulement)
    # Finds all missions of the campaign
    missions = Mission.objects.select_related().filter(operation = campagne_id)
    mission_pre = None
    mission_sui = None
    # Next and previous missions
    for mis in missions:
        if mis.numero == (mission.numero - 1):
            mission_pre = mis
        if mis.numero == (mission.numero + 1):
            mission_sui = mis
    # Finds the user requesting the mission to have a nice display of date
    utilisateur = request.user
    context = {'mission': mission, 'mission_pre': mission_pre,
               'mission_sui': mission_sui, 'image': image,
               'count': count, 'utilisateur': utilisateur}

    return render(request, 'site/rapport_mission.html', context)

def form_groups(form, groups):
    return [[form[k] for k in g] for g in groups]

# Enables the creation of missions for players
@permission_required('fiches.fdg', raise_exception=True)
def creer_mission(request, campagne_id):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            save_it = form.save()
            return redirect('mission', campagne_id=save_it.operation.id,
                            mission_id=save_it.id )
        else:
            print(form.errors)
    else:
        form = MissionForm(initial={'operation': campagne_id})
    context = {'form': form,
               'formgroups': form_groups(form, [['operation', 'numero', 'type_mis'],
                                                ['dirigeant', 'autre_dirigeant'],
                                                ['lieu', 'jour', 'mois', 'annee'],
                                                ['objectif', 'participants', 'deroulement',],
                                                ['signature_url',]])}
    return render(request, 'site/mission_edit.html', context)


# Enables the edition of missions for players
@permission_required('fiches.veteran', raise_exception=True)
def edit_mission(request, mission_id):
    mission = Mission.objects.get(pk=mission_id)

    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            save_it = form.save()
            return redirect('mission', campagne_id=mission.operation.id,
                            mission_id=mission.id )
        else:
            print(form.errors)
    else:
        form = MissionForm(instance=mission, initial={'operation': mission.operation})
    context = {'form': form,
               'formgroups': form_groups(form, [['operation', 'numero', 'type_mis'],
                                                ['dirigeant', 'autre_dirigeant'],
                                                ['lieu', 'jour', 'mois', 'annee'],
                                                ['objectif', 'participants', 'deroulement',],
                                                ['signature_url',]])}
    return render(request, 'site/mission_edit.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

# Display classes
@login_required
def classes(request):
    classes = Classe.objects.all().order_by('nom')
    paginator = Paginator(classes, 8)
    page = request.GET.get('page')
    try:
        classes_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        classes_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        classes_list = paginator.page(paginator.num_pages)

    context = {'classes': classes, 'classes_list': classes_list}

    return render(request, 'site/classes.html', context)

# Display list of spells for the required class
@permission_required('fiches.allie', raise_exception=True)
def sorts(request, classe_id):
    voyelles = ["a","e","i","o","u", "é", "è", "ë", "y"]
    classe = get_object_or_404(Classe, pk=classe_id)
    classe_consonne = True
    if classe.nom[0].lower() in voyelles:
        classe_consonne = False
    sorts = Sort.objects.filter(classe=classe_id).order_by('nom')
    paginator = Paginator(sorts, 12)
    page = request.GET.get('page')
    try:
        sorts_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        sorts_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        sorts_list = paginator.page(paginator.num_pages)

    context = {'sorts': sorts, 'sorts_list': sorts_list,
               'classe': classe, 'classe_c': classe_consonne}

    return render(request, 'site/sorts.html', context)


def tooltip_sort(request, sort_id):
    sort = get_object_or_404(Sort, pk=sort_id)
    context = {'sort': sort}
    return render(request, 'site/tooltip_sort.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            save_it = form.save()
            return redirect('upload_gallery')
        else:
            print(form.errors)
    else:
        form = ImageForm()

    return render(request, 'fiches/image.html', {'form': form})


@permission_required('fiches.fdg', raise_exception=True)
def upload_gallery(request):
    images = Image.objects.all()
    paginator = Paginator(images, 20)
    page = request.GET.get('page')
    try:
        images_list = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        images_list = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        images_list = paginator.page(paginator.num_pages)

    context = {'images_list': images_list}
    return render(request, 'site/up_gallery.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CARTES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def cartes(request):
    return render(request, 'site/maps.html', {})


def json_carte(request):
    quests = serializers.serialize('json', Quete.objects.filter(etat__lt=3),
                                   fields=('nom','zone', 'x', 'y', 'etat'))
    return JsonResponse(quests, safe=False)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMERCES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def gerer_bourse(request, fiche_id, bourse_id):
    bourse = Bourse.objects.get(pk=bourse_id)
    fiche = Fiche.objects.get(pk=fiche_id)
    utilisateur = request.user
    if utilisateur == fiche.createur:
        if request.method == 'POST':
            re = request.POST.copy()
            re['argent'] = int(re['argent'])* 100 + int(re['cuivre']) + int(re['or'])*10000
            form = BourseForm(re, instance=bourse)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_fiche', fiche_id=fiche_id)
            else:
                print(form.errors)
        else:
            form = BourseForm(instance=bourse)
    else:
        return HttpResponse("Vous ne pouvez pas editer cette bourse.")

    context = {'form': form, 'bourse': bourse}
    return render(request, 'fiches/bourse.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_bourse(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    utilisateur = request.user
    if utilisateur == fiche.createur and not fiche.bourse:
        bourse_creee = Bourse.objects.create(nom='Bourse de '+fiche.nom+' '+fiche.prenom)
        fiche.bourse=bourse_creee
        fiche.save()
        return redirect('detail_fiche', fiche_id=fiche_id)
    else:
        return HttpResponse("Vous ne pouvez pas créer cette bourse.")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% HABITATIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def creer_piece(request):
    utilisateur = request.user
    if request.method == 'POST':
        data = request.POST.copy()
        data['createur'] = User.objects.get(username=request.user).id
        form = PieceForm(data)
        if form.is_valid():
            save_it = form.save()
            return redirect('piece', piece_id=save_it.id )
        else:
            print(form.errors)
    else:
        form = PieceForm()
    context = {'form': form}
    return render(request, 'site/piece.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_etage(request):
    utilisateur = request.user
    pieces = Piece.objects.filter(createur=utilisateur)
    if request.method == 'POST':
        data = request.POST.copy()
        data['createur'] = User.objects.get(username=request.user).id
        form = EtageForm(data)
        if form.is_valid():
            save_it = form.save()
            return redirect('etage', etage_id=save_it.id )
        else:
            print(form.errors)
    else:
        form = EtageForm()
    context = {'form': form}
    return render(request, 'site/etage.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def creer_maison(request, proprietaire_id, type_maison):
    proprietaire = Fiche.objects.get(pk=proprietaire_id)
    utilisateur = request.user
    type_maison = int(type_maison)
    if proprietaire.createur == utilisateur :
        etages = Etage.objects.filter(createur=utilisateur)
        if request.method == 'POST':
            form = MaisonForm(request.POST)
            if form.is_valid():
                save_it = form.save()
                return redirect('maison', maison_id=save_it.id )
            else:
                print(form.errors)
        else:
            form = MaisonForm()

        context = {'form': form, 'proprietaire': proprietaire,
                   'etages': etages }
        if type_maison == 1:
            return render(request, 'site/maisons/taudis.html', context)
        elif type_maison == 2:
            return render(request, 'site/maison.html', context)
        else:
            return render(request, 'site/maison.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas créer une maison pour ce personnage.")


def habitations(request):
    context = {}
    if request.method == 'GET' and 'valeur' in request.GET and 'recherche' in request.GET:
        if 'recherche' is not None and 'recherche' != '':
            valeur = request.GET.get('valeur')
            recherche = request.GET.get('recherche')
            Qr = None
            q = Q(**({"%s__icontains" % recherche: valeur }))
            if Qr:
                Qr = Qr | q # or & for filtering
            else:
                Qr = q
            # this you can now combine with other filters, exclude etc.
            maisons_list = Maison.objects.filter(Qr)
            context['recherche'] = recherche
            context['valeur'] = valeur
        else:
            maisons_list = Maison.objects.order_by('nom')

    else:
        maisons_list = Maison.objects.order_by('nom')

    paginator = Paginator(maisons_list, 12)
    page = request.GET.get('page')
    try:
        maisons = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        maisons = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        maisons = paginator.page(paginator.num_pages)

    context['maisons'] = maisons

    return render(request, 'site/habitations.html', context)


# Display the requested house
def detail_maison(request, maison_id):
    maison = get_object_or_404(Maison, pk=maison_id)
    utilisateur = request.user

    context = {'maison': maison}
    return render(request, 'site/detail_maison.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSEIL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


def conseil(request):
    a_legende = False
    if request.user and request.user.is_authenticated:
        utilisateur = User.objects.get(username=request.user)
        if utilisateur.has_perm('fiches.chef'):
            legende_utilisateur = Legende.objects.all().filter(createur=utilisateur.id)
            if legende_utilisateur:
                a_legende = True
        else:
            a_legende = False

    legende_noirebois = Legende.objects.all().filter(nom__icontains='Noirebois')
    legendes_allies = Legende.objects.all().exclude(nom__icontains='Noirebois').exclude(nom__icontains='Horde')
    legende_horde = Legende.objects.all().filter(nom__icontains='Horde')

    all_layers = os.listdir('%s/site/council/layers' % (settings.STATICFILES_DIRS))

    context = {'legende_noirebois': legende_noirebois,
               'legendes_allies': legendes_allies,
               'legende_horde': legende_horde,
               'a_legende': a_legende,
               'all_layers': all_layers}

    return render(request, 'site/conseil.html', context)


@permission_required('fiches.chef', raise_exception=True)
def conseil_en_cours(request):
    # first delete associated tokens
    user = User.objects.get(username=request.user)
    user_tokens = Token.objects.all().filter(createur=user.id)
    user_tokens.delete()
    # then create new token and save it
    token = uuid.uuid4().hex
    token_object = Token.objects.create(token=token, createur=user)
    token_object.save()

    context = {'token': token}
    return render(request, 'site/conseil_en_cours.html', context)

@permission_required('fiches.chef', raise_exception=True)
def edit_legende(request):
    chef = User.objects.get(username=request.user).id
    legende_filter = Legende.objects.all().filter(createur=chef)
    # if there is already a legend
    if legende_filter:
        legende = legende_filter[0]
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = chef
            form = LegendeForm(data, request.FILES, instance=legende)
            if form.is_valid():
                save_it = form.save()
                return redirect('conseil')
            else:
                print(form.errors)
        else:
            form = LegendeForm(instance=legende)
    else:
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = chef
            form = LegendeForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('conseil')
            else:
                print(form.errors)
        else:
            form = LegendeForm()

    context = {'form': form}

    return render(request, 'site/legende_edit.html', context)


def get_id(request, token):
    try:
        found_token = Token.objects.get(token=token)
        return HttpResponse(found_token.createur.id)
    except ObjectDoesNotExist:
        return HttpResponse(status=403)


def delete_token(request, token):
    if request.method == 'DELETE':
        try:
            found_token = Token.objects.get(token=token)
            found_token.delete()
        except ObjectDoesNotExist:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=404)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% UTILS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def get_weather():
    date = datetime.datetime.now()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% UTILS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def compter_boutiques(request):
    citoyens = int(request.GET.get('citoyens', '1'))

    shops = Shops()

    context = shops.count_shops(citoyens)
    context['citoyens'] = citoyens
    return render(request, 'site/compter_boutiques.html', context)
