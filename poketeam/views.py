
from os import stat
from unicodedata import name
from poketeam.models import Pokemon,Poketeam
from rest_framework import viewsets
from rest_framework import status
from poketeam.serializers import PokemonSerializer,PoketeamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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

        pokemons=new_team.pokemons.all()

        poke_list=[]
        for pokemon in pokemons:
            poke_list.append({
                'name':pokemon.name,
                'sprite':pokemon.sprite,
                'types':pokemon.types
            })

        serializer=PoketeamSerializer(new_team,many=False,context={'request':request})
        return Response(status =200,data={'name':pack['name'],'pokemons':poke_list})

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

@api_view(['POST'])
def register(request):
    """
        Custom Funtion to create user
    """

    body = json.loads(request.body)

    username=body["username"]
    password=body["password"]

    user = User(username=username,password=password)

    user.save()
    userResponse=User.objects.get(username=username)
    print(userResponse)
    token=Token.objects.get(user=userResponse)

    return Response({"token":token.key})
