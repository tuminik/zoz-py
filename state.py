#!/usr/bin/env python

import copy

from utils import FIFOQueue
from constantes import *

class zozState:
    # Variables que definen las dimensiones del tablero
    matrixX = 0
    matrixY = 0
    matrix = []
    
    # Variable para ayudar a ubicar rapidamente la posicion del jugador
    playerX = -1
    playerY = -1
    
    # Listas con las coordenadas de los blank
    blank = []

    def __init__(self, map):
        self.matrix = copy.deepcopy(map)
        self.listBlank()
        self.steps = 0
        self.pushes = 0

    def clone(self):
        newState = zozState(self.matrix)
        newState.playerX = self.playerX
        newState.playerY = self.playerY
        newState.matrixX = self.matrixX
        newState.matrixY = self.matrixY
        newState.steps = self.steps
        newState.pushes = self.pushes
        return newState

    def canMove(self, move):
        if move == MOVE_RIGHT:
            return self.canMoveDir(0, 2)
        if move == MOVE_LEFT:
            return self.canMoveDir(0, -2)
        if move == MOVE_UP_RIGHT:
            return self.canMoveDir(-1, 1)
        if move == MOVE_UP_LEFT:
            return self.canMoveDir(-1, -1)
        if move == MOVE_DOWN_RIGHT:
            return self.canMoveDir(1, 1)
        if move == MOVE_DOWN_LEFT:
            return self.canMoveDir(1, -1)

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

    def getItemR(self, x, y):
        return self.getItem(self.playerX + x, self.playerY + y)
        
    def setItem(self, x, y, value):
        self.matrix[self.playerX + x][self.playerY + y] = value

    def setItemR(self, x, y):
        self.setItem(0, 0, CHAR_FICHA)
        self.setItem(x, y, CHAR_SPACE)
        self.setItem(2*x, 2*y, CHAR_SPACE)
    
    def movePlayer(self, action):
        self.playerX=action[1]
        self.playerY=action[2]
        if action[0] == MOVE_RIGHT:
            self.setItemR(0, 2)
        if action[0] == MOVE_LEFT:
            self.setItemR(0, -2)
        if action[0] == MOVE_UP_RIGHT:            
            self.setItemR(-1, 1)
        if action[0] == MOVE_UP_LEFT:
            self.setItemR(-1, -1)
        if action[0] == MOVE_DOWN_RIGHT:
            self.setItemR(1, 1)
        if action[0] == MOVE_DOWN_LEFT:
            self.setItemR(1, -1)
    
    def listBlank(self):       #Genera una lista de las coordenadas de las cajas en el laberinto
        list=[] 
        x=0

        try:
            for column in self.matrix:
                y=0
                for position in column:
                    if position == CHAR_SPACE:
                        list.append((x, y))
                    y += 1
                x += 1
            self.blank = list
        except Exception as ex:
            errorMsg = "Error al listar los espacios en blanco en el tablero"
            raise Exception(errorMsg, ex)

def validPosition(state, x, y):     # Verifica si las coordenadas proporcionadas se encuentran dentro de los limites del laberinto
    return (0 <= x and x < state.matrixX) and (0 <= y and y < state.matrixY)