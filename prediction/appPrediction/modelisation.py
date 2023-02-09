# ML
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump, load
import os

if "rl.joblib" in os.listdir():
    pass
else:
    nombre_valeurs = 200
    X = np.linspace(0, 10, nombre_valeurs).reshape(nombre_valeurs, 1)
    y = X + np.random.randn(nombre_valeurs, 1)
    rl = LinearRegression()
    rl.fit(X, y)
    dump(rl, 'rl.joblib')

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

