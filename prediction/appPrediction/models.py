from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Travailleur(models.Model):
    prenom = models.CharField(max_length=100, null=False)
    nom = models.CharField(max_length=100, null=False)
    competence = models.TextField(max_length=200, null=True, default="NON")
    metier = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=100, null=False)
    salaire = models.FloatField()
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])

class NombreDeLigne(models.model):
    nombre = models.IntegerField()