
from os import stat
from unicodedata import name
from poketeam.models import Pokemon,Poketeam
from rest_framework import viewsets
from rest_framework import status
from poketeam.serializers import PokemonSerializer,PoketeamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions

import json

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST','GET'])
def create_team(request):
    """
        Custom Function to create a poketeam
    """
    if request.method =='POST':
        print(request.body)
        pack = (json.loads(request.body))
        #pokemons_ids=json.loads(pack['pokemons'])
        pokemons_ids=pack['pokemons']
        new_team = Poketeam(name=pack['name'])
        new_team.owner=request.user
        new_team.save()
        for p_id in pokemons_ids:
            pokemon= Pokemon.objects.get(id=p_id)
            new_team.pokemons.add(pokemon)
        new_team.save()
        return Response(status =200)

    elif request.method == 'GET':
        poketeams = Poketeam.objects.filter(owner=request.user)

        serializer = PoketeamSerializer(poketeams,many=True,context={'request':request})
        teams =[]
        for team in poketeams:
            pokemons=team.pokemons.all()
            poke_list=[]
            for pokemon in pokemons:
                poke_list.append({
                    'name':pokemon.name,
                    'sprite':pokemon.sprite,
                    'types':pokemon.types
                })
            teams.append({
                'name':team.name,
                'pokemons':poke_list
                }
            )
        return Response(teams)