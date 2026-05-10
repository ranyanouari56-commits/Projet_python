from django import forms
from .models import Releve


class ReleveForm(forms.ModelForm):
    class Meta:
        model = Releve
        fields = ['appareil', 'valeur_kwh', 'puissance_instantanee', 'date_heure_releve']
        widgets = {
            'appareil': forms.Select(attrs={'class': 'form-select'}),
            'valeur_kwh': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'kWh', 'step': '0.01'}),
            'puissance_instantanee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Watts', 'step': '0.1'}),
            'date_heure_releve': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'appareil': 'Appareil',
            'valeur_kwh': 'Consommation (kWh)',
            'puissance_instantanee': 'Puissance (Watts)',
            'date_heure_releve': 'Date et heure du relevé',
        }
