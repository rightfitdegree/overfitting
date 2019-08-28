import random    
random.seed()

import pandas as pd
import numpy as np

#from scipy.optimize import minimize_scalar

class RandPol(pd.DataFrame):
    """Dataframe para generar polinomios aleatorios
    en intervalo -1 ≤ X ≤ 1; -1 ≤ Y ≤ 1   
    """
    #Headers para columnas del DataFrame
    Nº = 'Nº'
    X = 'X'
    Y = 'Y'
    POL = 'Pol'
    ERR = 'Err'
    POL_ERR = 'Pol+Err'

    #Constantes para definir los intervalos
    MIN_X = -1.0
    MAX_X = 1.0
    MIN_Y = -1.0
    MAX_Y = 1.0

    #Cantidad de puntos aleatorios para generar un polinomio por regresión de
    #los puntos
    CANTIDAD_PUNTOS = 10

    TITULOS_COLUMNAS = [Nº, X, Y]

    GradoDelPolinomio = None

    Polinomio = None

    #Error = None

    #Polinomio_Error = None

    #generación de errores

    @property
    def _constructor(self):
        return RandPol


    def __init__(self, *args, **kwargs):
        print("Iniciando " + self.__class__.__name__)
        super().__init__(*args, **kwargs)

        #Creación de puntos aleatorios
        self[RandPol.X] = self.__RandomPointsX()
        self[RandPol.Y] = self.__RandomPoints()

        self.GradoDelPolinomio = self.__GradoPolinomialAleatorio()
        print("Grado del polinomio: " , self.GradoDelPolinomio)

        #Obtención de polinomio ajustado a los puntos
        self.Polinomio = self.GenerarPolinomio()

        print("Polinomio: \n", self.Polinomio)

        #Evaluación del polinomio
        self[RandPol.POL] = self.Polinomio(self[RandPol.X])

        #Generación de errores
        self[RandPol.ERR] = self.__RandomPoints()

        self[RandPol.POL_ERR] = self[RandPol.POL] + self[RandPol.ERR]



        #Obtención de máximos
        print('Dataframe: \n',self)
        #myplot = self.plot(x =RandPol.X, y =RandPol.Y, kind ='scatter')	


    def  __GradoPolinomialAleatorio(self):
        return random.randint(0,9)

    def __RandomPoints(self, cantidad=CANTIDAD_PUNTOS, min=MIN_X, max=MAX_X) -> []:
        if cantidad < 2 :
            raise Exception('La cantidad de puntos debe ser mayor a 2')
   
        respuesta = np.random.uniform(low=min, high=max, size=cantidad)

        return respuesta

    def __RandomPointsX(self, cantidad=CANTIDAD_PUNTOS, min=MIN_X, max=MAX_X) -> []:
        if cantidad < 2 :
            raise Exception('La cantidad de puntos debe ser mayor a 2')
   
        respuesta = self.__RandomPoints(cantidad, min, max)
        respuesta[0] = min
        respuesta[-1] = max

        return respuesta

    
    def GenerarPolinomio(self):
        x = np.array(self[RandPol.X])
        y = np.array(self[RandPol.Y])
        z = np.polyfit(x, y, self.GradoDelPolinomio)
        
        return np.poly1d(z)