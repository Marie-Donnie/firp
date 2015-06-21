from django.shortcuts import get_object_or_404, render
from fiches.models import Fiche, FicheForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    fiches = Fiche.objects.order_by('nom')[:5]
    context = {'latest_fiches': fiches}
    return render(request, 'fiches/index.html', context)


def detailFiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, pk=fiche_id)
    return render(request, 'fiches/detail.html', {'fiche': fiche})

def creerfiche(request):
    if request.method == 'POST':
        form = FicheForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FicheForm()

    return render(request, 'fiches/formulaire.html', {'form': form})
