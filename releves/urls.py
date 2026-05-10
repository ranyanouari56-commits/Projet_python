from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_releves, name='liste_releves'),
    path('ajouter/', views.ajouter_releve, name='ajouter_releve'),
    path('modifier/<int:releve_id>/', views.modifier_releve, name='modifier_releve'),
    path('supprimer/<int:releve_id>/', views.supprimer_releve, name='supprimer_releve'),
]
