from django.contrib import admin
from .models import Appareil, Zone


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_zone', 'limite_puissance')
    search_fields = ('nom_zone',)


class AppareilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'zone', 'type_alimentation', 'puissance_nominale')
    search_fields = ('nom',)
    list_filter = ('zone', 'type_alimentation')


admin.site.register(Zone, ZoneAdmin)
admin.site.register(Appareil, AppareilAdmin)
