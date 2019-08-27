import random    
random.seed()

import pandas as pd
import numpy as np


class LineaAleatoriaDF(pd.DataFrame):
    """Dataframe para generar polinomios aleatorios
    en intervalo -1 ≤ X ≤ 1; -1 ≤ Y ≤ 1   
    """
    #Headers para columnas del DataFrame
    Nº = 'Nº'
    X = 'X'
    Y = 'Y'

    #Constantes para definir los intervalos
    MIN_X = -1.0
    MAX_X = 1.0
    MIN_Y = -1.0
    MAX_Y = 1.0

    #Cantidad de puntos aleatorios para generar un polinomio por regresión de
    #los puntos
    CANTIDAD_PUNTOS = 10

    TITULOS_COLUMNAS = [Nº, X, Y]


    @property
    def _constructor(self):
        return LineaAleatoriaDF

    def __init__(self, *args, **kwargs):
        print("Iniciando " + self.__class__.__name__)
        super().__init__(*args, **kwargs)

        #self.index = LineaAleatoriaDF.TITULOS_COLUMNAS
        self[LineaAleatoriaDF.X] = self.__PuntosAleatorios()
        self[LineaAleatoriaDF.Y] = self.__PuntosAleatorios()


    def  __GradoPolinomialAleatorio():
        return random.randint(0,9)

    def __PuntosAleatorios(self, cantidad=CANTIDAD_PUNTOS, min=MIN_X, max=MAX_X) -> []:
        if cantidad < 2 :
            raise Exception('La cantidad de puntos debe ser mayor a 2')
   
        respuesta = [min]
        tempRand = np.random.uniform(low=min, high=max, size=(cantidad - 2))
        respuesta.extend(tempRand)
        respuesta.append(max)

        return respuesta
