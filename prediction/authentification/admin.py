from django.contrib import admin
from authentification.models import User

class UserAffichage(admin.ModelAdmin):
    #list_display = [field.name for field in User._meta.get_fields()]
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAffichage)
