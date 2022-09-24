from tabnanny import verbose
import numpy as np
import argparse

def f(lista, verbose):
    """calcula suma, media, stdv, min, max

    Args:
        list (lista): lista de numeros del 1 al 4

    Returns:
        tupla: (suma, media, stdv, min, max)
    """
    
    suma_lista = sum(lista)
    media = np.mean(lista)
    desviacion = np.std(lista)
    minimo = min(lista)
    maximo = max(lista)
    
    if verbose== 1:
        print("esta es la suma lista", suma_lista)
        print("esta es la media", media)
        print("esta es la desviacion estandar", desviacion)
        print("esta es el min y max", minimo, maximo)
        print("y estos son todos los valores agrupados en una tupla:")
    else:
        pass
    return suma_lista, media, desviacion, minimo, maximo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", type=int,default=0,help="para decidir si imprime información o no")
    args = parser.parse_args()
    verbose = args.verbose

    suma_lista, media, desviacion, minimo, maximo = f([1,2,3,4],verbose)

    
    print("DONE")

if __name__ == "__main__":
    main()