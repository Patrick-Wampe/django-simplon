from django.contrib import admin
from appPrediction.models import Travailleur
# Register your models here.

class AffichageColonnes(admin.ModelAdmin):
    list_display = [field.name for field in Travailleur._meta.get_fields()]

admin.site.register(Travailleur, AffichageColonnes)
