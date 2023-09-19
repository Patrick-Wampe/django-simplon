from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def accueil(request):
    prenom = "Patou"
    return render(request,"accueil.html",
                  context={"prenom": prenom})
