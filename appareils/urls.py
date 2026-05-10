from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_appareils, name='liste_appareils'),
    path('<int:appareil_id>/', views.detail_appareil, name='detail_appareil'),
    path('ajouter/', views.ajouter_appareil, name='ajouter_appareil'),
    path('modifier/<int:appareil_id>/', views.modifier_appareil, name='modifier_appareil'),
    path('supprimer/<int:appareil_id>/', views.supprimer_appareil, name='supprimer_appareil'),
    
    
    path('zones/', views.liste_zones, name='liste_zones'),
    path('zones/ajouter/', views.ajouter_zone, name='ajouter_zone'),
    path('zones/modifier/<int:zone_id>/', views.modifier_zone, name='modifier_zone'),
    path('zones/supprimer/<int:zone_id>/', views.supprimer_zone, name='supprimer_zone'),
]
