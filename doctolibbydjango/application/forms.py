from django import forms
from application.models import FormulaireSante

class FormulaireSanteForm(forms.ModelForm):
    class Meta:
        model = FormulaireSante
        fields = "__all__"
"""
class InfoGeneraleForm(forms.ModelForm):
    class Meta:
        model = FormulaireSante
        fields = ("patient", 
                  'date_remplissage', 
                  'periodicite_jours',
                  'is_late',
                  "poids",
                  "tour_de_taille_cm",)
    
class EtatDeSanteForm(forms.ModelForm):
    class Meta:
        model = FormulaireSante
        fields = ("frequence_cardiaque_min", 
                  'tension_arterielle_systolique_matin', 
                  'tension_arterielle_systolique_soir',
                  'tension_arterielle_diastolique_matin',
                  "tension_arterielle_diastolique_soir",
                  "symptomes_cardiovasculaires",
                  "nb_medicaments_jour",)
"""
