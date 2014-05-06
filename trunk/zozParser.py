#!/usr/bin/env python
import sys

from state import zozState
from constantes import *

characters = [CHAR_FICHA, 		# Lista de caracteres permitidos dentro de un archivo
              CHAR_SPACE, 
              CHAR_SPACE_O,
              '\n']
			  
def imprimir(lista):
    for i in lista:
        #for j in range(len(lista[i])):
        print i
        #print "\n\n"
			
def cantidadChar(lista, fila, char):
    cantidad = 0
    for i in range(fila):
        cantidad += lista[i].count(char)
        
    return cantidad

def encuadrarLista(lista, columna):
    for i in range(len(lista)):
         for j in range(columna - len(lista[i])):
            lista[i].append(CHAR_SPACE_O)
    return lista
			
def obtenerIndiceLinea(linea, columna, char):
    try:
        return linea.index(char)
    except:
        return columna

def rellenarEspaciosBlancos(columna, linea):
    linea2 = []
    linea2 = list(linea)
    if linea2[len(linea2) - 1] == '\n':
        linea2[len(linea2) - 1] = CHAR_SPACE_O
    #for i in range(obtenerIndice(linea, columna)):
    #    linea2[i] = CHAR_SPACE_O
    return linea2

def obtieneTamFilCol(columna, fila, linea): #obtiene las dimensiones del mapa
    if len(linea) > columna: #obtiene la columna
        columna = len(linea)
                
    fila += 1 #obtiene la fila
    return fila, columna
	
def validaCaracteres(linea): #verifica si los caracteres extraidos del archivo son validos
    for i in range(len(linea)):
        if linea[i] not in characters:
            print linea[i], i #imprime el caracter invalido y la posicion
            sys.exit("algun caracter no es aceptado, Arreglelo!!")#al no ser validos detiene la ejecucion
			
def obtenerMapa(filename, fila, columna):
    lista =[]
    with open(filename, 'r') as f: #abre y cierra el archivo apropiadamente incluso si se genero una excepcion
        for linea in f:
            validaCaracteres(linea)
            fila, columna = obtieneTamFilCol(columna, fila, linea)
            lista.append(rellenarEspaciosBlancos(columna, linea)) #carga linea por linea el archivo a la lista
    f.closed
    if not cantidadChar(lista, fila, CHAR_SPACE):
        sys.exit("No se encontraron espacios en blanco, Arreglelo!!")
    elif not cantidadChar(lista, fila, CHAR_FICHA):
        sys.exit("No se encontraron Fichas, Arreglelo!!")
    else:
        lista = encuadrarLista(lista, columna)

    #try
    estado = zozState(lista)
    estado.matrixX = fila
    estado.matrixY = columna

    return estado
	
"""def main():
    columna = 0
    fila = 0	
    initial = obtenerMapa("problem", fila, columna)
    print initial.matrix
    print initial.matrixX
    print initial.matrixY
	
if __name__ == "__main__":
    main()"""