from django import forms

from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class TravailleurForm(forms.Form):
    prenom = forms.CharField(max_length=100)
    nom = forms.CharField(max_length=100)
    competence = forms.CharField(max_length=200)
    metier = forms.CharField(max_length=100)
    ville = forms.CharField(max_length=100)
    salaire = forms.FloatField()
    age = forms.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    experience = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])

