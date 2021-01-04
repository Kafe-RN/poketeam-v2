from django.db import models

# Create your models here.


class Raca(models.Model):
    nome=models.CharField(max_length=256)
    descrição= models.TextField()

class Animal(models.Model):
    nome = models.CharField(max_length=256)
    idade = models.FloatField(default=0)
    raca = models.ForeignKey(Raca,on_delete = models.CASCADE)

class Curiosidade(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    descricao = models.TextField()

