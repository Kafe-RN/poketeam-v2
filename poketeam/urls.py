from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from poketeam import views 

router = routers.DefaultRouter()
router.register(r'pokemons',views.PokemonViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('teams',views.create_team,name='create-team')
]