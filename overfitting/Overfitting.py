import sys
import VectorAleatorio as VA

MyPuntos = None

def main():
    print("Generando lista de polinomios...")
    MyPuntos = ListaDeRandpol(100)
    print("Lista generada")

    #for dframe in MyPuntos:
    #    print(dframe)



    import tensorflow as tf
    #print(tf.__version__)
    
    import keras as K
    #print(K.__version__)

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
    i=1

    for p in processes:
        p.join() #Espera a que termine el proceso
        print("joined process", i)
        i +=1

    return ListaParalela
      

    
    
if __name__ == "__main__":
    import pandas as pd
    main()
