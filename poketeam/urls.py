from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from poketeam import views
from rest_framework.authtoken import views as at
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = routers.DefaultRouter()
router.register(r'pokemons',views.PokemonViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('teams',views.create_team,name='create-team'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',views.register)
]