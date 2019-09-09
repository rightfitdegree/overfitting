import sys
import VectorAleatorio as VA
import numpy as np

MyPuntos = None
def Generar_Puntos():
    while True:
        MyPuntos=VA.RandPol()
        X=MyPuntos.XY().transpose()
        Y=MyPuntos[VA.RandPol.POL].values.transpose()
        print('shape(X)= ',X.shape)
        print('shape(Y)= ',Y.shape)
        yield (X,Y)

def main():
    #print("Generando lista de polinomios...")
    #MyPuntos = ListaDeRandpol(10)
    #print("Lista generada, ", len(MyPuntos), " puntos")

    #for dframe in MyPuntos:
    #    print(dframe)#



    import tensorflow as tf
    import keras as K
    from keras.models import Sequential  


    model = Sequential()

    from keras.layers import Dense
    Tamano=VA.RandPol.CANTIDAD_PUNTOS
    model.add(Dense(units=Tamano*2, input_shape=(Tamano*2,),  activation='relu'))
    model.add(Dense(units=Tamano, activation='relu'))
    #Tamaño=coeficientes polinomiales + overfitting + probabilidad + error distribucion
    model.add(Dense(units=Tamano, activation='sigmoid',))

    model.compile( optimizer='adam' , loss='mean_squared_error')

    model.summary()
         
    from keras.utils import plot_model
    plot_model(model, to_file='C:\Borrar\model.png')

    model.fit_generator(Generar_Puntos(),
                        steps_per_epoch=10000, epochs=10)

    input('Press Enter to exit')



def Agregar(Lista, i):  
    Lista.append(VA.RandPol())

def ListaDeRandpol(Cantidad):
    from multiprocessing import Process, Manager
    ListaParalela = None #Lista de dataframes creados en paralelo

    #with Manager() as manager:
    ListaParalela = Manager().list()  # <-- can be shared between processes.
    processes = []
    for i in range(Cantidad):
        p = Process(target=Agregar, args=(ListaParalela,i))  # Passing the list
        p.start()
        processes.append(p)

    
    for i,p in enumerate(processes):
        p.join() #Espera a que termine el proceso
        print("joined process", i)
        

    return ListaParalela
      

    
    
if __name__ == "__main__":
    import pandas as pd
    main()
