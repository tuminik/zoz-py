#!/usr/bin/env python
import sys

from state import ZozState
from constantes import *

characters = [CHAR_FICHA, 		# Lista de caracteres permitidos dentro de un archivo
              CHAR_SPACE, 
              CHAR_SPACE_O,
              '\n']
			  
def imprimir(lista):
    for i in range(len(lista)):
        #for j in range(len(lista[i])):
            print lista[i]#[j]
			
def cantidadChar(lista, fila, char):
    cantidad = 0
    for i in range(fila):
        cantidad += lista[i].count(char)
        
    return cantidad
			
def obtenerIndiceLinea(linea, columna, char):
    try:
        return linea.index(char)
    except:
        return columna

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
            lista.append(linea) #carga linea por linea el archivo a la lista
    f.closed
    if not cantidadChar(lista, fila, CHAR_SPACE):
        sys.exit("No se encontraron espacios en blanco, Arreglelo!!")
    elif not cantidadChar(lista, fila, CHAR_FICHA):
        sys.exit("No se encontraron Fichas, Arreglelo!!")

    #try
    estado = zozState(lista)
    estado.matrixX = fila
    estado.matrixY = columna

    return estado