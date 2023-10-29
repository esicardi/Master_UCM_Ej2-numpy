import numpy as np


def read_data(fname: str, tipo: type) -> np.ndarray:
    #read_data lee una matriz de datos a partir de un archivo de texto
    #debe especificarse el nombre del archivo (con la forma nombre.txt, suponiendo que se encuentran en el mismo directorio del programa ) y el tipo de variable (int o float) de los datos
    #Las zonas son formato 'int', los valores son formato 'float'
    # Escribe aquí tu código
    # No olvides documentar la función
    a = np.loadtxt("./"+fname, dtype=tipo)
    # devuelve un array de numpy con el formato especificado
    return a

#read_data("zonas.txt",'int')
#read_data("valores.txt",'float')

def set_of_areas(zonas: np.ndarray)-> set[int]:
    """

    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    # Escribe aquí tu código
    # No olvides documentar la función
    ss=set()
    #crea el conjunto vacío
    zonas2=zonas.flatten()
    #define un vector a partir del array de entrada
    largo=len(zonas2)
    #largo es la longitud de dicho vector
    for i in range(largo):
        #recorro el vector
        if zonas2[i].dtype!= int:
            # si hay elementos no enteros da error
            raise Exception('TypeError: The elements type must be int, not float64')
            return None
        else:
            # si los elementos son enteros, agrega los elementos al conjunto
            # el tipo set no toma en cuenta los datos repetidos
            ss.add(zonas2[i])
    #se devuelve como salida el conjunto con las areas contenidas en el array
    return ss


#set_of_areas(np.arange(10).reshape(5, 2))
#set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
#set_of_areas(np.zeros(3, dtype=np.float_))

# def mean_areas ...

    # Escribe aquí el código de la función mean_areas
    # No olvides documentar la función y escribir las anotaciones de tipos
    # Añade más ejemplos para doctest
def mean_areas(zonas: np.ndarray, valores: np.ndarray) -> np.ndarray:
    """

    Examples:
    --------
    >>> mean_areas(np.array([[2,2],[1,2]]),np.array([[4.,5.],[6.,2.]]))
    array([[3.67, 3.67],
          [6.  , 3.67]])
    >>> mean_areas(np.array([[2,2],[2,1],[1,2]]),np.array([[4.,5.],[6.,2.]]))
    Traceback (most recent call last):
        ...
    IndexError: Shape of input arrays should be the same
    """
    rows1=zonas.shape[0]
    rows2=valores.shape[0]
    cols1=zonas.shape[1]
    cols2=zonas.shape[1]
    #calculo dimensiones de arrays de entrada
    if rows1!=rows2 or cols1!=cols2:
        raise Exception("IndexError: Shape of input arrays should be the same") 
        return None
    # si alguna dimension no coincide, da error
    else:
    # areas es el conjunto de indices de las zonas
    #inicializo con ceros de tipo float una matriz de iguales dimensiones
        areas=set_of_areas(zonas)
        aa=np.zeros((rows1,cols1),dtype=float)
        for k in areas:
            # recorro las areas
            nn=0.
            aux=0.
            # nn es el contador de variables sumadas
            # aux es una variable auxiliar donde los elementos de la misma zona
            for i in range(rows1):
                for j in range(cols1):
                    # recorro todos los indices
                    if(zonas[i,j]==k):
                        aux=aux+valores[i,j]
                        nn=nn+1
                        # si la zona coincide con el k evaluado, sumo un elemento
            aux=aux/nn
            #una vez sumados todos los elementos para este k, divido por el numero 
            # de sumandos para obtener el promedio
            for i in range(rows1):
                for j in range(cols1):
                    #recorro las zonas
                    if(zonas[i,j]==k):
                        aa[i,j]=aux
                        #sustituyo los elementos de la matriz aa por el promedio 
                        #del K correspondiente
    return np.round(aa,decimals=2) # devuelve el array de promedios segun zonas, redondeado a 2 cifras decimales

#zonas=np.array([[2,2],[1,2]])
#zonas
#valores=np.array([[4.,5.],[6.,2.]])
#valores
#mean_areas(zonas,valores)
#prue=np.array([[2,2],[2,1],[1,2]])
#mean_areas(prue,valores)

# ------------ test  --------#
import doctest

def test_doc()-> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()   # executing tests
