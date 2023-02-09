from django.contrib import admin
from appPrediction.models import Travailleur, NombreDeLigne, scoreModel
# Register your models here.

class AffichageColonnes(admin.ModelAdmin):
    list_display = [field.name for field in Travailleur._meta.get_fields()]

class NombreDeLigneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NombreDeLigne._meta.get_fields()]

class scoreModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in scoreModel._meta.get_fields()]

admin.site.register(Travailleur, AffichageColonnes)
admin.site.register(NombreDeLigne, NombreDeLigneAdmin)
admin.site.register(scoreModel, scoreModelAdmin)
