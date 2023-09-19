from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect

def connexion(request):
    message = ""
    if request.method == "POST":
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        verification = authenticate(username = username,
                                    password = motDePasse)
        if verification != None:
            login(request, verification)
            pass # rediriger vers la page d'accueil
        else:
            message = "username ou/et mot de passe incorrect"
    
    return render(request,
                      "connexion.html", {"message" : message})

def deconnexion(request):
    logout(request)
    return redirect("connexion")
