from django.db import models


class Zone(models.Model):
    nom_zone = models.CharField(max_length=100)
    limite_puissance = models.FloatField(help_text="Limite de puissance en Watts")

    def __str__(self):
        return self.nom_zone

    class Meta:
        verbose_name = "Zone"
        verbose_name_plural = "Zones"


class Appareil(models.Model):
    TYPE_ALIMENTATION_CHOICES = [
        ('monophase', 'Monophasé'),
        ('triphase', 'Triphasé'),
        ('solaire', 'Solaire'),
        ('batterie', 'Batterie'),
    ]

    nom = models.CharField(max_length=200)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='appareils')
    type_alimentation = models.CharField(
        max_length=50,
        choices=TYPE_ALIMENTATION_CHOICES,
        default='monophase'
    )
    puissance_nominale = models.FloatField(help_text="Puissance nominale en Watts")
    date_installation = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.zone.nom_zone})"

    class Meta:
        verbose_name = "Appareil"
        verbose_name_plural = "Appareils"
