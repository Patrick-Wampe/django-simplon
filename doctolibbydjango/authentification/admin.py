from django.contrib import admin
from authentification.models import Utilisateur

class colonnes(admin.ModelAdmin):
    list_display = ("username", "role", "email","is_superuser",)  #[field.name for field in Utilisateur._meta.get_fields()]
    #list_display = [field.name for field in Utilisateur._meta.get_fields()][1:-2]
    #search_fields = #['username','role']

admin.site.register(Utilisateur, colonnes)

"""
>>> from authentification.models import Utilisateur
>>> tuple([field.name for field in Utilisateur._meta.get_fields()])
('logentry', 'patientMedecin', 'medecinPatient', 'id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'role', 'groups', 'user_permissions')
"""
