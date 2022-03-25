from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=256)
    sprite = models.TextField()
    types = models.TextField()


class Poketeam(models.Model):
    name = models.CharField(max_length=256)
    pokemons = models.ManyToManyField(Pokemon)
