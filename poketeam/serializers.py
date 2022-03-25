from poketeam.models import Pokemon,Poketeam
from rest_framework import serializers


class  PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id','name','sprite','types']
class PoketeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Poketeam
        fields=['name','pokemons']