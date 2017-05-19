from django.shortcuts import get_object_or_404, render
from fiches.models import Fiche, UserProfile
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from fiches.forms import FicheForm, UserForm, UserProfileForm, MyRegistrationForm


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
    print(users)
    context = {'latest_users': users}
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
def add_profile(request):
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

    return render(request, 'fiches/utilisateur.html',
                  {'utilisateur': utilisateur})


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# Enables the creation of a Fiche
@login_required
def creer_fiche(request):
    if request.method == 'POST':
        data = request.POST.dict()
        data['createur'] = User.objects.get(username=request.user).id
        form = FicheForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FicheForm()

    return render(request, 'fiches/formulaire.html', {'form': form})


# Display the request Fiche
def detail_fiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)

    return render(request, 'fiches/detail.html', {'fiche': fiche})


# Displays the first name and last name of the latests Fiche model instances
def personnages(request):
    fiches = Fiche.objects.order_by('nom', 'prenom')
    context = {'latest_fiches': fiches}

    return render(request, 'fiches/index.html', context)

@login_required
def edit_fiche(request, fiche_id):
    fiche = Fiche.objects.get(pk=fiche_id)
    if request.user == fiche.createur:
        if request.method == 'POST':
            form = FicheForm(request.POST, instance=fiche)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:

            form = FicheForm(instance=fiche)

        return render(request, 'fiches/formulaire.html', {'form': form})

    else:

        return HttpResponse("Vous ne pouvez pas editer cette fiche.")
