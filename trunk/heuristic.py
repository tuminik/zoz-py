from utils import infinity
from ai import Node

from constantes import *
from zozProblema import accions

def zozHeuristic(state):
	return len(state.blank) - blankMove(state)

def blankMove(state):
	x, y, c = -1, -1, 0
	listMoves = state.accions(state)
	for i in listMoves
		if x =! i[1] and y =! i[2]
			c += 1
			x, y = i[1], i[2]
	return c