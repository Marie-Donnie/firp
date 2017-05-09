from django.shortcuts import get_object_or_404, render
from fiches.models import Fiche, FicheForm, User, UserForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout


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


def inscription(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'fiches/inscription.html', {'form': form})
