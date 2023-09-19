from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from authentification.models import Utilisateur
import random 
import string

def connexion(request):
    message = ""
    # A t'on reçu des datas d'un formulaire ? Si oui la condition est True
    if request.method == "POST": 
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        verification = authenticate(username = username,
                                    password = motDePasse)
        if verification != None:
            login(request, verification)
            return redirect("accueil")
        else:
            message = "username ou/et mot de passe incorrect"
    
    return render(request,
                      "connexion.html", {"message" : message})

def deconnexion(request):
    logout(request)
    return redirect("connexion")


def inscription(request):
    ideeMDP = "".join([random.choice(string.printable) for _ in range(12)]).replace(" ", "")
    if request.method == "POST": 
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        nouveauCompte = Utilisateur.objects.create_user(username = username,
                                    password = motDePasse)
        
        return redirect("connexion")
    
    return render(request,
                      "inscription.html", {"ideeMDP" : ideeMDP.replace(" ", "")})
