from django import forms
from .models import Appareil, Zone


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['nom_zone', 'limite_puissance']
        widgets = {
            'nom_zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cuisine, Atelier...'}),
            'limite_puissance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Watts'}),
        }
        labels = {
            'nom_zone': 'Nom de la zone',
            'limite_puissance': 'Limite de puissance (W)',
        }


class AppareilForm(forms.ModelForm):
    class Meta:
        model = Appareil
        fields = ['nom', 'zone', 'type_alimentation', 'puissance_nominale']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'appareil'}),
            'zone': forms.Select(attrs={'class': 'form-select'}),
            'type_alimentation': forms.Select(attrs={'class': 'form-select'}),
            'puissance_nominale': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Puissance en Watts'}),
        }
        labels = {
            'nom': 'Nom de l\'appareil',
            'zone': 'Zone',
            'type_alimentation': 'Type d\'alimentation',
            'puissance_nominale': 'Puissance nominale (W)',
        }
