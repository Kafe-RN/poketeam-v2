from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from animals import views 

router = routers.DefaultRouter()
router.register(r'animais',views.AnimalViewSet)
router.register(r'racas',views.RacaViewSet)
router.register(r'curiosidades',views.CuriosidadeViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]