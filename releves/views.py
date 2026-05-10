from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Releve
from appareils.models import Appareil, Zone
from .forms import ReleveForm


@login_required
def liste_releves(request):
    query = request.GET.get('q', '')
    zone_id = request.GET.get('zone', '')
    date_debut = request.GET.get('date_debut', '')
    date_fin = request.GET.get('date_fin', '')

    releves = Releve.objects.select_related('appareil__zone').all()

    if query:
        releves = releves.filter(Q(appareil__nom__icontains=query))
    if zone_id:
        releves = releves.filter(appareil__zone__id=zone_id)
    if date_debut:
        releves = releves.filter(date_heure_releve__date__gte=date_debut)
    if date_fin:
        releves = releves.filter(date_heure_releve__date__lte=date_fin)

    zones = Zone.objects.all()
    context = {
        'releves': releves,
        'zones': zones,
        'query': query,
        'zone_id': zone_id,
        'date_debut': date_debut,
        'date_fin': date_fin,
    }
    return render(request, 'releves/liste.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff, login_url='home')
def ajouter_releve(request):
    form = ReleveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_releves')
    return render(request, 'releves/form.html', {'form': form, 'titre': 'Ajouter un relevé'})


@login_required
@user_passes_test(lambda u: u.is_staff, login_url='home')
def modifier_releve(request, releve_id):
    releve = get_object_or_404(Releve, id=releve_id)
    form = ReleveForm(request.POST or None, instance=releve)
    if form.is_valid():
        form.save()
        return redirect('liste_releves')
    return render(request, 'releves/form.html', {'form': form, 'titre': 'Modifier le relevé', 'releve': releve})


@login_required
@user_passes_test(lambda u: u.is_staff, login_url='home')
def supprimer_releve(request, releve_id):
    releve = get_object_or_404(Releve, id=releve_id)
    releve.delete()
    return redirect('liste_releves')
