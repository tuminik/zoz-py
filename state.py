#!/usr/bin/env python

import copy

from utils import FIFOQueue			#crear
from constantes import *			#crear
from debug import * 				#crear
from heuristic import zozHeuristic	#crear

class zozState:    
    matrixX = 0		# Variables que definen las dimensiones del tablero
    matrixY = 0
    matrix = []
    
    playerX = -1	# Variable para ayudar a ubicar rapidamente la posicion de la ficha vacia
    playerY = -1
	
    blank = []		# Listas con las coordenadas de los blank

    """# Variable de depuracion
    steps = 0
    pushes = 0
    h = -1"""

    def __init__(self, map):
        self.matrix = copy.deepcopy(map)
		self.blank = listBlank(self)
		playerX, playerY = findPlayer(self)
        """self.steps = 0
        self.pushes = 0"""
		
	"""Crea una copia del estado actual
    def clone(self):
        newState = SokobanState(self.matrix)
        newState.playerX = self.playerX
        newState.playerY = self.playerY
        newState.matrixX = self.matrixX
        newState.matrixY = self.matrixY
        newState.steps = self.steps
        newState.pushes = self.pushes
        return newState"""
    
    def canMove(self, move):
        if move == MOVE_UP_RIGHT:
            return self.canMoveDir(1, 1)
		if move == MOVE_UP_LEFT:
            return self.canMoveDir(-1, 1)
        if move == MOVE_DOWN_RIGHT:
            return self.canMoveDir(1, -1)
		if move == MOVE_DOWN_LEFT:
            return self.canMoveDir(-1, -1)
        if move == MOVE_LEFT:
            return self.canMoveDir(-2, 0)
        if move == MOVE_RIGHT:
            return self.canMoveDir(2, 0)
        
		return False
    
    def canMoveDir(self, x, y):
        pos1 = self.getItemR(x, y)           # Adelante
        pos2 = self.getItemR(2 * x, 2 * y)   # a 2 pasos
        
        if pos1 == CHAR_FICHA and pos2 == CHAR_FICHA:
			return True
				
        return False

    def getItem(self, x, y):
        if validPosition(self, x, y):
            return self.matrix[x][y]
        else:
            return CHAR_SPACE_O
            
    """def setItem(self, x, y, value):
        if validPosition(self, x, y):
            if self.matrix[x][y] == CHAR_WALL:
                errorMsg = "No se puede modificar pared en " + printCoords(x, y) + "!"
                errorMsg += "\nJugador en " + printCoords(self.playerX, self.playerY) + "\n"
                #errorMsg += "".join(printTable(self.matrix, "Error"))
                raise Exception(errorMsg)
            self.matrix[x][y] = value
        else:
            #manejar error de coordenadas incorrectas
            errorMsg = "SetItem: Coordenadas " + printCoords(x, y) + " invalidas"
            raise Exception(errorMsg)"""
			
    def getItemR(self, x, y):
        return self.getItem(self.playerX + x, self.playerY + y)
    """def setItemR(self, x, y, value):
        self.setItem(self.playerX + x, self.playerY + y, value)"""


def validPosition(state, x, y):		# Verifica si las coordenadas proporcionadas se encuentran dentro de los limites del laberinto
    return (0 <= x and x < state.matrixX) and (0 <= y and y < state.matrixY)

"""def validRelPosition(state, x, y):
    if x == 0 and (y == 1 or y == -1) or y == 0 and (x == 1 or x == -1):
        return True
    else:
        return False"""
  
def ListBlank(state):		#Genera una lista de las coordenadas de las cajas en el laberinto
	list=[]
	x=0

	try:
		for column in state.matrix:
			y=0
			for position in column:
				if position == CHAR_SPACE:
					list.append((x, y))
				y += 1
			x += 1
	except Exception as ex:
		errorMsg = "Error al listar los espacios en blanco en el tablero"
		raise Exception(errorMsg, ex)

	return list
	
def findPlayer(state):
	i=0
    if playerX == -1 and playerY == -1
		return state.blank[0][0], state.blank[0][1]
	else
		i = state.blank.index((playerX, playerY))
		return state.blank[i+1][0], state.blank[i+1][1]