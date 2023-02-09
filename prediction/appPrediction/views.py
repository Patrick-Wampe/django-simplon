from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from appPrediction.models import Travailleur, NombreDeLigne, scoreModel
from appPrediction.forms import TravailleurForm
from appPrediction.modelisation import prediction
from authentification.models import User
from django.contrib.auth.decorators import login_required

from plotly.offline import plot
import plotly.express as px

# Create your views here.
# ETAPES DEVELOPPEMENT DJANGO
# Création d'un environnement virtuel
# Installatio de django > pip install django
# Création d'un projet django > django-admin startproject nomDuProjet
# Création de l'application > django-admin startapp nomDeLApplication
# Lancement du serveur > python manage.py runserver
# Lancement des migrations > python manage.py migrate
# Création d'une vue en affichant un fichier html du dossier templates

# Sauvegarder le modèle > OK
# Ajouter des visualisations dans le template > OK
# Entrainer le modèle si et seulement si on a un nombre X de nouvelles données 
# > pipeline > Comparer le nombre de ligne de la table > count()

# Sauvegarder le nouveau modèle ⇔ le score de ce dernier est meilleur que l'ancien

# url > views > model > template

# Si la table NombreDeLigne est vide on ajoute un nombre de ligne égale à 0
try:
    if len(NombreDeLigne.objects.all()) == 0:
        # On crée un enregistrement dans la table NombreDeLigne
        tableNDL = NombreDeLigne(nombre = 0) 
        tableNDL.save()
    else:
        pass

    if len(scoreModel.objects.all()) == 0:
        # On crée un enregistrement dans la table scoreModel
        scoreModelPrecedant = scoreModel(scorePrecedant = 0) 
        scoreModelPrecedant.save()
    else:
        pass
except:
    pass

#print("VALEURs de la colonne salaire", [ligne.salaire for ligne in Travailleur.objects.all()])

print("RESULTAT",User)




@login_required
def index(request):
    prix = int()
    form = TravailleurForm()

    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
    
    graphique = plot(fig, output_type="div")
    
    if request.method == "POST": # Si des données on été renseignées
        """
        tableTravailleur = Travailleur(nom = request.POST["Nom"],
        prenom = request.POST["Prenom"],
        ville = request.POST["Ville"],
        metier = request.POST["Metier"],
        competence = request.POST["Competences"],
        salaire = request.POST["Salaire"],
        age = request.POST["Age"],
        experience= request.POST["Experience"])
        tableTravailleur.save()
        return redirect('index')
        """

        #print(request.POST["taille"], type(request.POST["taille"]))
        #print("L'information envoyé par le navigateur est :", request.POST["taille"])
        try:
            ligneDansTableTravailleur = Travailleur.objects.get(id = int(request.POST["IDUser"]))
            #print(ligneDansTableTravailleur.prenom)
            #prix = regressionLineaire.predict([[int(request.POST["taille"])]])[0][0]
            #prix = regressionLineaire.predict([[ligneDansTableTravailleur.salaire]])[0][0]

            prix = prediction(ligneDansTableTravailleur.salaire)
            return render(request, "index.html", {"prix" : prix, "graphique" : graphique})
        #return redirect('burger')
        except:
            ligneDansTableTravailleur = "La ligne n'existe pas"
            prix = "La valeur n'existe pas"
            return render(request, "index.html", {"prix" : prix, "graphique" : graphique})

    else: # Je viens d'arriver sur la page
        #return HttpResponse("Bonjour tout le monde !")
        prenom = "ChatGPT"
        datas = Travailleur.objects.all() # On récupère toutes les lignes

        print("NOMBRE DE LIGNES :",len(datas))

        return render(request, "index.html", 
        context={"a" : prenom, 'd' : datas, 'form' : form,
        "graphique" : graphique})

@login_required
def maj(request, id):
    ligneDansDatabase = Travailleur.objects.get(id = id)
    if request.method == "POST": # Quelqu'un a appuyé sur le bouton submit
        ligneDansDatabase.nom = request.POST["Nom"]
        ligneDansDatabase.prenom = request.POST["Prenom"]
        ligneDansDatabase.ville = request.POST["Ville"]
        ligneDansDatabase.metier = request.POST["Metier"]
        ligneDansDatabase.competence = request.POST["Competences"]
        ligneDansDatabase.salaire = request.POST["Salaire"]
        ligneDansDatabase.age = request.POST["Age"]
        ligneDansDatabase.experience= request.POST["Experience"]
        
        ligneDansDatabase.save()
        return redirect('index')
    else: # Je viens d'atterir sur la page
        return render(request, "maj.html", 
        {"ligneDansDatabase" : ligneDansDatabase})

@login_required
def sup(request, id):
    ligneDansDatabase = Travailleur.objects.get(id = id)
    ligneDansDatabase.delete()
    return redirect('index')

@login_required
def burger(request):
    return render(request, "burger.html")