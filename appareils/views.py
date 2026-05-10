from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appareil, Zone
from .forms import AppareilForm, ZoneForm
from releves.models import Releve
from django.db.models import Q, Sum, Avg


@login_required
def liste_appareils(request):
    query = request.GET.get('q', '')
    zone_id = request.GET.get('zone', '')
    type_alim = request.GET.get('type_alimentation', '')

    appareils = Appareil.objects.select_related('zone').all()

    if query:
        appareils = appareils.filter(Q(nom__icontains=query))
    if zone_id:
        appareils = appareils.filter(zone__id=zone_id)
    if type_alim:
        appareils = appareils.filter(type_alimentation=type_alim)

    zones = Zone.objects.all()
    context = {
        'appareils': appareils,
        'zones': zones,
        'query': query,
        'zone_id': zone_id,
        'type_alim': type_alim,
        'type_choices': Appareil.TYPE_ALIMENTATION_CHOICES,
    }
    return render(request, 'appareils/liste.html', context)


@login_required
def detail_appareil(request, appareil_id):
    appareil = get_object_or_404(Appareil, id=appareil_id)
    releves = appareil.releves.order_by('-date_heure_releve')[:20]
    stats = appareil.releves.aggregate(
        total_kwh=Sum('valeur_kwh'),
        moyenne_kwh=Avg('valeur_kwh'),
        moyenne_puissance=Avg('puissance_instantanee'),
    )

  
    chart_releves = appareil.releves.order_by('date_heure_releve')[:15]
    chart_labels = [r.date_heure_releve.strftime('%d/%m %H:%M') for r in chart_releves]
    chart_data_kwh = [r.valeur_kwh for r in chart_releves]
    chart_data_watts = [r.puissance_instantanee for r in chart_releves]

    context = {
        'appareil': appareil,
        'releves': releves,
        'stats': stats,
        'chart_labels': chart_labels,
        'chart_data_kwh': chart_data_kwh,
        'chart_data_watts': chart_data_watts,
    }
    return render(request, 'appareils/detail.html', context)


@login_required
def ajouter_appareil(request):
    if not request.user.is_staff:
        return redirect('home')
    form = AppareilForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_appareils')
    return render(request, 'appareils/form.html', {'form': form, 'titre': 'Ajouter un appareil'})


@login_required
def modifier_appareil(request, appareil_id):
    if not request.user.is_staff:
        return redirect('home')
    appareil = get_object_or_404(Appareil, id=appareil_id)
    form = AppareilForm(request.POST or None, instance=appareil)
    if form.is_valid():
        form.save()
        return redirect('liste_appareils')
    return render(request, 'appareils/form.html', {'form': form, 'titre': 'Modifier l\'appareil', 'appareil': appareil})


@login_required
def supprimer_appareil(request, appareil_id):
    if not request.user.is_staff:
        return redirect('home')
    appareil = get_object_or_404(Appareil, id=appareil_id)
    appareil.delete()
    return redirect('liste_appareils')




@login_required
def liste_zones(request):
    zones = Zone.objects.all()
    return render(request, 'appareils/liste_zones.html', {'zones': zones})


@login_required
def ajouter_zone(request):
    if not request.user.is_staff:
        return redirect('home')
    form = ZoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_zones')
    return render(request, 'appareils/form.html', {'form': form, 'titre': 'Ajouter une zone'})


@login_required
def modifier_zone(request, zone_id):
    if not request.user.is_staff:
        return redirect('home')
    zone = get_object_or_404(Zone, id=zone_id)
    form = ZoneForm(request.POST or None, instance=zone)
    if form.is_valid():
        form.save()
        return redirect('liste_zones')
    return render(request, 'appareils/form.html', {'form': form, 'titre': 'Modifier la zone', 'zone': zone})


@login_required
def supprimer_zone(request, zone_id):
    if not request.user.is_staff:
        return redirect('home')
    zone = get_object_or_404(Zone, id=zone_id)
    zone.delete()
    return redirect('liste_zones')
