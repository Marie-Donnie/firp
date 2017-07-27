from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fiches.models import *
from fiches.forms import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% GENERAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Displays the first name and last name of the Fiche model
def index(request):
    fiches = Fiche.objects.order_by('-creation')[:16]
    context = {'latest_fiches': fiches}

    return render(request, 'fiches/index.html', context)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def conseils(request):
    return render(request, 'fiches/conseils.html', {})


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
            form = UserProfileForm()

        return render(request, 'fiches/profil.html', {'form': form})


def aff_user(request, user_id):
    utilisateur = get_object_or_404(User, pk=user_id)
    return render(request, 'fiches/utilisateur.html',
                  {'utilisateur': utilisateur})


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Enables the creation of a Fiche
@login_required
def creer_fiche(request):
    utilisateur = request.user
    # Checks wether user can create another fiche or not
    if ((utilisateur.fiches.count() < 16) or
        (utilisateur.has_perm('fiches.plus_de_15_fiches'))):
        if request.method == 'POST':
            # request.POST is not editable, so we have to copy it to hard code a value
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            # not fdg users are not allowed to have an equipement and detailed inventaire
            if not(utilisateur.has_perm('fiches.equipement_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
            else:
                data['inventaire'] = None
                name = data['prenom']
                data['equipement'] = Equipement.objects.create(nom='Equipement de '+name).id
                data['inventaire_fdg'] = Inventaire.objects.create(nom='Inventaire de '+name).id
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

        context = {'form': form}
        return render(request, 'fiches/formulaire.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire plus de quinze fiches. Seuls les membres des Fils de Garithos le peuvent.")


# Display the request Fiche
def detail_fiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)

    if fiche.inventaire_fdg:
        if (fiche.inventaire_fdg.cases.count() < 30):
            nb = 30 - fiche.inventaire_fdg.cases.count()
        else:
            nb = 0
    else:
        nb = 0

    if fiche.equipement:
        mp = fiche.equipement.get_mp()
        am = fiche.equipement.get_am()
        aa = fiche.equipement.get_autre_arme()
        tete = fiche.equipement.get_tete()
        epaules = fiche.equipement.get_epaules()
        torse = fiche.equipement.get_torse()
        mains = fiche.equipement.get_mains()
        taille = fiche.equipement.get_taille()
        jambes = fiche.equipement.get_jambes()
        dos = fiche.equipement.get_dos()
        cou = fiche.equipement.get_cou()
        poignets = fiche.equipement.get_poignets()
        doigts = fiche.equipement.get_doigts()
        divers = fiche.equipement.get_divers()
        effets, effets_ig, force, intell, agi, armure = fiche.equipement.effets()
    else:
        mp, am, aa, tete, epaules, torse = None, None, None, None, None, None
        mains, taille, jambes, dos, cou = None, None, None, None, None
        poignets, doigts, divers = None, None, None
        effets, effets_ig, force = None, None, None
        intell, agi, armure = None, None, None
    context = {'fiche': fiche,
               'range': range(nb), 'effets': effets, 'effets_ig': effets_ig,
               'force': force, 'intell': intell, 'agi': agi,
               'armure': armure, 'mp': mp, 'am': am, 'aa': aa, 'tete': tete,
               'epaules': epaules, 'torse': torse, 'mains': mains,
               'taille': taille, 'jambes': jambes, 'dos': dos, 'cou': cou,
               'poignets': poignets, 'doigts': doigts, 'divers': divers}
    return render(request, 'fiches/detail.html', context)


# Displays the first name and last name of the latests Fiche model instances
def personnages(request):
    # fiches = Fiche.objects.order_by('nom', 'prenom')
    fiches_list = Fiche.objects.order_by('nom', 'prenom')

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
def edit_fiche(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    utilisateur = request.user
    if utilisateur == fiche.createur:
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            if not(utilisateur.has_perm('fiches.equipement_ok') and
                   utilisateur.has_perm('fiches.inventaire_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
            else:
                data['inventaire'] = None
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
                   'inventaires': inventaires}

        return render(request, 'fiches/formulaire.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer cette fiche.")


@login_required
def delete_fiche(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur:
        context = {'fiche': fiche}
        if request.method == 'POST':
            fiche.delete()
            return render(request, 'fiches/fiche_supprimee.html', context)
        else:
            return render(request, 'fiches/confirmation_suppression.html', context)
    else:
        return HttpResponse("Vous ne pouvez pas supprimer cette fiche.")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@login_required
def creer_objet(request):
    if request.user.has_perm('fiches.add_objet'):
        if request.method == 'POST':
            form = ObjetForm(request.POST, request.FILES)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_objet', objet_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ObjetForm()

        return render(request, 'fiches/objet.html', {'form': form})

    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent faire des objets.")


@login_required
def creer_armure(request):
    if request.user.has_perm('fiches.armure_ok'):
        if request.method == 'POST':
            form = ArmureForm(request.POST, request.FILES)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_armure', armure_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ArmureForm()

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/armure.html', context)

    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent faire des armures.")


@login_required
def creer_case(request):
    if request.user.has_perm('fiches.case_ok'):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            form = CaseForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = CaseForm()

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/case.html', context)

    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent faire des cases d'inventaire.")


@login_required
def creer_inventaire(request):
    if request.user.has_perm('fiches.inventaire_ok'):
        if request.method == 'POST':
            form = InventaireForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = InventaireForm()

        cases = Case.objects.filter(createur=request.user)
        context = {'form': form, 'cases': cases}

        return render(request, 'fiches/inventaire.html', context)

    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent gerer leur inventaire.")


@login_required
def creer_equipement(request):
    if request.user.has_perm('fiches.equipement_ok'):
        if request.method == 'POST':
            form = EquipementForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = EquipementForm()

        objets = Armure.objects.all()
        context = {'form': form, 'objets': objets}

        return render(request, 'fiches/equipement.html', context)

    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent gerer leur equipement.")


@login_required
def objets(request):
    if request.user.has_perm('fiches.objet_ok'):
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
    else:
        return HttpResponse("Seuls les membres des Fils de Garithos peuvent voir la liste des objets.")


def detail_objet(request, objet_id):
    objet = get_object_or_404(Objet, pk=objet_id)
    context = {'objet': objet}
    return render(request, 'fiches/aff_objet.html', context)


def detail_armure(request, armure_id):
    armure = get_object_or_404(Armure, pk=armure_id)
    objet = armure.objet
    context = {'armure': armure, 'objet': objet}
    return render(request, 'fiches/aff_armure.html', context)


@login_required
def edit_objet(request, objet_id):
    objet = Objet.objects.get(pk=objet_id)
    if request.user.has_perm('fiches.change_object'):
        if request.method == 'POST':
            form = ObjetForm(request.POST, request.FILES, instance=objet)
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

        return HttpResponse("Vous ne pouvez pas editer les objets.")


@login_required
def edit_armure(request, armure_id):
    armure = Armure.objects.get(pk=armure_id)
    if request.user.has_perm('fiches.change_armure'):
        if request.method == 'POST':
            form = ArmureForm(request.POST, instance=armure)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_armure', armure_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ArmureForm(instance=armure)

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/armure.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer les armures.")


@login_required
def edit_case(request, case_id):
    case = Case.objects.get(pk=case_id)
    if request.user.has_perm('fiches.change_case'):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=request.user).id
            form = CaseForm(data, instance=case)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = CaseForm(instance=case)

        objets = Objet.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/case.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer les cases.")


@login_required
def edit_inventaire(request, inventaire_id):
    inventaire = Inventaire.objects.get(pk=inventaire_id)
    if request.user.has_perm('fiches.change_inventaire'):
        if request.method == 'POST':
            form = InventaireForm(request.POST, instance=inventaire)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = InventaireForm(instance=inventaire)

        cases_perso = inventaire.cases.all()
        cases = Case.objects.filter(createur=request.user)
        context = {'form': form, 'cases': cases, 'cases_perso': cases_perso}
        return render(request, 'fiches/inventaire.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer les inventaires.")


@login_required
def edit_equipement(request, equipement_id):
    equipement = Equipement.objects.get(pk=equipement_id)
    if request.user.has_perm('fiches.change_equipement'):
        if request.method == 'POST':
            form = EquipementForm(request.POST, instance=equipement)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = EquipementForm(instance=equipement)

        objets = Armure.objects.all()
        context = {'form': form, 'objets': objets}
        return render(request, 'fiches/equipement.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer les equipements.")


def tooltip_objet(request, objet_id):
    objet = get_object_or_404(Objet, pk=objet_id)
    context = {'objet': objet}
    return render(request, 'fiches/tooltip_objet.html', context)


def tooltip_armure(request, armure_id):
    armure = get_object_or_404(Armure, pk=armure_id)
    objet = armure.objet
    context = {'armure': armure, 'objet': objet}
    return render(request, 'fiches/tooltip_armure.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUETES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


def quetes(request):
    quetes = Quete.objects.all().order_by('etat', 'creation', 'difficulte', 'nom')

    context = {'quetes': quetes}

    return render(request, 'site/quetes.html', context)


def quete(request, quete_id):
    quete = get_object_or_404(Quete, pk=quete_id)

    context = {'quete': quete}

    return render(request, 'site/quete.html', context)
