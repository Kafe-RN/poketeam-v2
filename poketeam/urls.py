from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from poketeam import views
from rest_framework.authtoken import views as at

router = routers.DefaultRouter()
router.register(r'pokemons',views.PokemonViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('teams',views.create_team,name='create-team'),
    path('login/', at.obtain_auth_token)
]