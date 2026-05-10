from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from releves.models import Releve
from appareils.models import Appareil, Zone


@login_required
def home(request):
    total_appareils = Appareil.objects.count()
    total_zones = Zone.objects.count()
    total_releves = Releve.objects.count()
    derniers_releves = Releve.objects.select_related('appareil__zone').order_by('-date_heure_releve')[:5]
    
    
    from django.db.models import Sum, Max
    consommation_totale = Releve.objects.aggregate(Sum('valeur_kwh'))['valeur_kwh__sum'] or 0
    
  
    from collections import defaultdict
    from django.utils import timezone

    daily_totals = defaultdict(float)
    for r in Releve.objects.all():
        if r.date_heure_releve:
            dt = r.date_heure_releve
            if timezone.is_aware(dt):
                dt = timezone.localtime(dt)
            daily_totals[dt.date()] += r.valeur_kwh

    sorted_dates = sorted(daily_totals.keys())[-7:]
    
    chart_labels = [d.strftime('%d/%m') for d in sorted_dates]
    chart_values = [round(daily_totals[d], 2) for d in sorted_dates]
  
    puissance_max = Releve.objects.aggregate(Max('puissance_instantanee'))['puissance_instantanee__max'] or 0

    context = {
        'total_appareils': total_appareils,
        'total_zones': total_zones,
        'total_releves': total_releves,
        'derniers_releves': derniers_releves,
        'consommation_totale': round(consommation_totale, 2),
        'puissance_max': round(puissance_max, 1),
        'chart_labels': chart_labels,
        'chart_values': chart_values,
    }
    return render(request, 'home.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue, {username} !")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('login')
