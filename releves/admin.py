from django.contrib import admin
from .models import Releve


class ReleveAdmin(admin.ModelAdmin):
    list_display = ('id', 'appareil', 'valeur_kwh', 'date_heure_releve')
    search_fields = ('appareil__nom',)
    list_filter = ('appareil__zone', 'date_heure_releve')
    date_hierarchy = 'date_heure_releve'


admin.site.register(Releve, ReleveAdmin)
