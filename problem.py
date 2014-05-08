#!/usr/bin/env python

import sys
import copy

from search import Problem
from heuristic import zozHeuristic
from constantes import *

def zozProblem(Problem)                                 #hereda la clase Problem de search.py
    expand = 0
    
    def _init_(self):                                   #recibe la tabla de juego y construye
        self.initial=self
        self.expanded = 0

    def goal_test(self, state):
        spaces_s=0        
        spaces_s = len(state.blank)
        
        if spaces_s == 1:
            return True
        else:
            return False
            
    def actions(self, state):
        listMoves[]
        listStates[]
        listMoves = generateMoves(state, listMoves)
        self.expanded += 1
        
        if not listMoves:                               #si la lista esta vacia, no hay movimientos posibles por ende no posibles sucesores
            return []                                   #retorna lista vacia la funcion sucesor
        else:                                           #si la lista tiene algo!!           
            return listMoves
    
    def result(self,  state, action)
        newState = state.clone()                        #generar nuevo estado
        newState.movePlayer(action)              		#mueve el jugador
        return newState
        
    def h(self, node):
        return zozHeuristic(node.state) 
        
def generateMoves(state, listMoves):
    try:
        for blank in state.blank
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
        return listMoves
        
def generateGoalState(state):
    lista=[]
    goal = state.clone()
    for i in len(goal.matrix)
        for j in len(i)
            if goal.matrix[i][j] == CHAR_FICHA
                goal.matrix[i][j] = CHAR_SPACE
 
    for i in len(goal.matrix)
        for j in len(i)
            goal.matrix[i][j] = CHAR_FICHA
            lista.append(goal.matrix)
            goal.matrix[i][j] = CHAR_SPACE

    return lista