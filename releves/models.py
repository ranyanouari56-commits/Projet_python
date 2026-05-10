from django.db import models
from django.utils import timezone
from appareils.models import Appareil


class Releve(models.Model):
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE, related_name='releves')
    valeur_kwh = models.FloatField(help_text="Consommation en kWh")
    puissance_instantanee = models.FloatField(help_text="Puissance en Watts au moment du relevé", default=0)
    date_heure_releve = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        
        if not self.puissance_instantanee or self.puissance_instantanee == 0:
            if self.appareil and self.appareil.puissance_nominale:
                self.puissance_instantanee = self.appareil.puissance_nominale
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.appareil.nom} - {self.valeur_kwh} kWh ({self.date_heure_releve.strftime('%d/%m/%Y %H:%M')})"

    @property
    def intensite_badge(self):
        """Retourne la classe Bootstrap selon l'intensité"""
        if self.valeur_kwh < 1:
            return 'success'
        elif self.valeur_kwh < 5:
            return 'warning'
        else:
            return 'danger'

    @property
    def pourcentage_limite(self):
        """Calcule le pourcentage de la limite de zone utilisé"""
        if self.appareil.zone.limite_puissance > 0:
            return round((self.puissance_instantanee / self.appareil.zone.limite_puissance) * 100, 1)
        return 0

    class Meta:
        verbose_name = "Relevé"
        verbose_name_plural = "Relevés"
        ordering = ['-date_heure_releve']
