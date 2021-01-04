
from animals.models import Animal, Raca,Curiosidade
from rest_framework import viewsets
from rest_framework import permissions
from animals.serializers import AnimalSerializer, RacaSerializer,CuriosidadeSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    #permission_classes = [permissions.IsAuthenticated]


class RacaViewSet(viewsets.ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer
    #permission_classes = [permissions.IsAuthenticated]
class CuriosidadeViewSet(viewsets.ModelViewSet):
    queryset = Curiosidade.objects.all()
    serializer_class = CuriosidadeSerializer