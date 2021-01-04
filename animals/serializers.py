from animals.models import Raca, Animal,Curiosidade
from rest_framework import serializers


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ['nome','idade','raca']


class RacaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raca
        fields = ['nome', 'descricao']

class CuriosidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curiosidade
        fields =['animal','descricao']
    