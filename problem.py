#!/usr/bin/env python

import sys
import copy

from search import Problem
from constantes import *
from heuristic import zozHeuristic
from zozParser import imprimir

class zozProblem(Problem):                                 #hereda la clase Problem de search.py
    expanded = 0
    
    def _init_(self):                                   #recibe la tabla de juego y construye
        self.initial=self
        self.expanded = 0

    def goal_test(self, state):
        cantidad = 0
        for i in range(state.matrixX):
            cantidad += state.matrix[i].count(CHAR_FICHA)
        #imprimir(state.matrix)
        #print cantidad
        #print len(state.blank)+1
        #print
        #print
        if cantidad == 1:
            #print "Entro en estado final"
            return True
        else:
            #print "no Entro"
            return False
            
    def actions(self, state):
        listMoves=[]
        listMoves = generateMoves(state, listMoves)
        #print "nuevo:"
        #print listMoves
        
        if not listMoves:                               #si la lista esta vacia, no hay movimientos posibles por ende no posibles sucesores
            return []                                   #retorna lista vacia la funcion sucesor
        else:                                          #si la lista tiene algo!!
            return listMoves
    
    def result(self,  state, action):
        self.expanded += 1
        #print self.expanded
        newState = state.clone()                        #generar nuevo estado
        newState.movePlayer(action)                     #mueve el jugador
        return newState
        
    def h(self, node):
        return zozHeuristic(node.state)
        
def generateMoves(state, listMoves):
    try:
        state.listBlank()
        #print "blank:"
        #print state.blank
        for blank in state.blank:
            state.playerX, state.playerY = blank
            if state.canMove(MOVE_RIGHT):
                listMoves.append((MOVE_RIGHT, blank[0], blank[1]))
            if state.canMove(MOVE_LEFT):
                listMoves.append((MOVE_LEFT, blank[0], blank[1]))
            if state.canMove(MOVE_UP_RIGHT):
                listMoves.append((MOVE_UP_RIGHT, blank[0], blank[1]))
            if state.canMove(MOVE_UP_LEFT):
                listMoves.append((MOVE_UP_LEFT, blank[0], blank[1]))
            if state.canMove(MOVE_DOWN_RIGHT):
                listMoves.append((MOVE_DOWN_RIGHT, blank[0], blank[1]))
            if state.canMove(MOVE_DOWN_LEFT):
                listMoves.append((MOVE_DOWN_LEFT, blank[0], blank[1]))
        
        return listMoves
    except:
        print "error"
        return listMoves
        
def generateGoalState(state):
    lista=[]
    i=0
    goal = state.clone()
    for linea in goal.matrix:
        for j in range(len(linea)):
            if goal.matrix[i][j] == CHAR_FICHA:
                goal.matrix[i][j] = CHAR_SPACE
        i+=1
 
    i=0
    for linea in goal.matrix:
        for j in range(len(linea)):
            goal.matrix[i][j] = CHAR_FICHA
            lista.append(goal.matrix)
            goal.matrix[i][j] = CHAR_SPACE
        i+=1
    return lista