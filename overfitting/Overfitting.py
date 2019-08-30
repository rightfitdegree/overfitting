import sys
import VectorAleatorio as VA

MyPuntos = None

def main():
    print("Generando lista de polinomios...")
    MyPuntos = ListaDeRandpol(10)
    print("Lista generada, ", len(MyPuntos), " puntos")

    #for dframe in MyPuntos:
    #    print(dframe)



    import tensorflow as tf
    import keras as K
    from keras.models import Sequential  


    model = Sequential()
    from keras.layers import Dense
    Tamano=VA.RandPol.CANTIDAD_PUNTOS

    model.add(Dense(units=Tamano, input_shape=(Tamano,),  activation='relu'))
    model.add(Dense(units=Tamano, activation='relu'))
    #Tamaño=coeficientes polinomiales + overfitting + probabilidad + error distribucion
    model.add(Dense(units=Tamano+2, activation='relu'))

    model.compile( optimizer='adam' , loss='mean_squared_error')

    model.summary()


    input('Press Enter to exit')


def Agregar(Lista, i):  # the managed list `L` passed explicitly.
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
