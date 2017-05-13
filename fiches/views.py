from django.shortcuts import get_object_or_404, render
from fiches.models import Fiche, FicheForm, User, UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as UserA
from django.template import RequestContext


# Create your views here.
def index(request):
    fiches = Fiche.objects.order_by('nom', 'prenom')
    context = {'latest_fiches': fiches}
    return render(request, 'fiches/index.html', context)


def detailFiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)
    return render(request, 'fiches/detail.html', {'fiche': fiche})


def creerfiche(request):
    if request.method == 'POST':
        form = FicheForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FicheForm()

    return render(request, 'fiches/formulaire.html', {'form': form})


def authen(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # return render(request, 'fiches/index.html', {'form': form})
        return HttpResponseRedirect('/')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def edit_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, user=request.user)
        if form.is_valid():
            print(form.cleaned_data)
            # user = User.objects.create(user=form.user, image=form.image,
            #                            naissance=form.naissance)
            # user = UserA(username=form.username,
            #              first_name=form.first_name,
            #              last_name=form.last_name,
            #              password=form.password,
            #              email=form.email)
            # user.save()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm(user=request.user)

    return render(request, 'fiches/inscription.html', {'form': form})


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
        context = RequestContext(request)
    return render(request,
                  'registration/register.html',
                  dict(userform=uf,
                       userprofileform=upf))
