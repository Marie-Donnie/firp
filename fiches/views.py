from django.shortcuts import get_object_or_404, render
from fiches.models import Fiche, UserProfile, Objet, Armure, Case, Inventaire, Equipement
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from fiches.forms import FicheForm, UserForm, UserProfileForm, MyRegistrationForm
from fiches.forms import ObjetForm, ArmureForm, CaseForm, InventaireForm, EquipementForm
from django.db.models import Count
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% GENERAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Displays the first name and last name of the Fiche model
def index(request):
    fiches = Fiche.objects.order_by('nom', 'prenom')
    context = {'latest_fiches': fiches}

    return render(request, 'fiches/index.html', context)


def login_authen(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseNotFound('<h1>User not found</h1>')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyRegistrationForm()

    return render(request, 'registration/register.html', {'userform': form})


def password_reset(request):
    pass


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
def edit_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyRegistrationForm(instance=request.user)

    return render(request, 'registration/register.html', {'userform': form})


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
            data = request.POST.dict()
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
    print(utilisateur.email)
    return render(request, 'fiches/utilisateur.html',
                  {'utilisateur': utilisateur})


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Enables the creation of a Fiche
@login_required
def creer_fiche(request):
    utilisateur = request.user
    if ((utilisateur.fiches.count() < 16) or
        (utilisateur.has_perm('fiches.plus_de_15_fiches'))):
        if request.method == 'POST':
            data = request.POST.dict()
            data['createur'] = User.objects.get(username=utilisateur).id
            if not(utilisateur.has_perm('fiches.equipement_ok') and
                   utilisateur.has_perm('fiches.inventaire_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
            else:
                data['inventaire'] = None
            form = FicheForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = FicheForm()

        equipements = Equipement.objects.all()
        inventaires = Inventaire.objects.all()
        context = {'form': form, 'equipements': equipements,
                   'inventaires': inventaires}
        return render(request, 'fiches/formulaire.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire plus de quinze fiches. Seuls les membres des Fils de Garithos le peuvent.")


# Display the request Fiche
def detail_fiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)

    if (fiche.inventaire_fdg.cases.count() < 25):
        nb = 25 - fiche.inventaire_fdg.cases.count()
    else:
        nb = 0
    context = {'fiche': fiche, 'range': range(nb)}
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
            data = request.POST.dict()
            data['createur'] = User.objects.get(username=utilisateur).id
            if not(utilisateur.has_perm('fiches.equipement_ok') and
                   utilisateur.has_perm('fiches.inventaire_ok')):
                data['equipement'] = None
                data['inventaire_fdg'] = None
            else:
                data['inventaire'] = None
            form = FicheForm(data, request.FILES, instance=fiche)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
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
                form.save()
                return HttpResponseRedirect('/')
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
                form.save()
                return HttpResponseRedirect('/')
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
            form = CaseForm(request.POST, request.FILES)
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

        cases = Case.objects.all()
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
                form.save()
                return HttpResponseRedirect('/')
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
                form.save()
                return HttpResponseRedirect('/')
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
            form = CaseForm(request.POST, instance=case)
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
        cases = Case.objects.all()
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
