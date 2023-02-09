# ML
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump, load
import os
from appPrediction.models import NombreDeLigne, Travailleur, scoreModel

try:
    if "rl.joblib" in os.listdir():
        if (NombreDeLigne.objects.get(id = 1).nombre + 10) == len(Travailleur.objects.all()):
            # Je récupère la ligne avec l'ID que je souhaite (ici 1)
            ancienneValeurNombreDeLigne = NombreDeLigne.objects.get(id = 1)  
            
            # J'écrase la valeur de la colonne nombre pour mettre celle de la taille
            # du nombre de ligne dans la table Travailleur
            ancienneValeurNombreDeLigne.nombre = len(Travailleur.objects.all())
            
            # Je sauvegarde les modifications
            ancienneValeurNombreDeLigne.save()
            
            # Ré-entrainement du modèle
            X = np.array([ligne.salaire for ligne in Travailleur.objects.all()]).reshape(-1, 1)
            y = np.array([ligne.age for ligne in Travailleur.objects.all()])

            rl = LinearRegression()
            rl.fit(X, y)
            
            # Vérification du nouveau score
            # Si nouveau score supérieur au précédant effacement de l'ancien model rl.joblib
            if scoreModel.objects.get(id = 1) < rl.score(X, y):
                os.remove("rl.joblib")
                dump(rl, "rl.joblib") 
                nouveauScore = scoreModel.objects.get(id = 1)
                nouveauScore.scorePrecedant = rl.score(X, y)
                nouveauScore.save()
    else:
        nombre_valeurs = 200
        X = np.linspace(0, 10, nombre_valeurs).reshape(nombre_valeurs, 1)
        y = X + np.random.randn(nombre_valeurs, 1)
        rl = LinearRegression()
        rl.fit(X, y)
        dump(rl, 'rl.joblib')
except:
    pass

def prediction(valeur):
    regressionLineaire = load('rl.joblib') 
    if type(valeur) == int:
        return regressionLineaire.predict([[valeur]])[0][0]
    else:
        try:
            valeur = int(valeur)
            return regressionLineaire.predict([[valeur]])[0][0]
        except:
            return "La valeur n'est pas au format numérique"

