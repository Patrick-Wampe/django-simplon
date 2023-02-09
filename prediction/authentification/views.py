from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate # import des fonctions login et authenticate
from django.shortcuts import redirect

def connexion(request):
    message = ""
    if request.method == "POST": #Est-ce que le formulaire est renseigné ?
        # Vérification des infos de connexion
        user = authenticate(
                username=request.POST["username"],
                password=request.POST["password"])
        # user vaut None si la vérification échoue
        if user is not None:
            # On lance la connexion
            login(request, user)
            return redirect("index")
        else:
            message = 'Identifiants invalides.'
    return render(request, 'connexion.html', context={'message': message})


def deconnexion(request):
    logout(request)
    return redirect('connexion')
