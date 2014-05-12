def zozHeuristic(state):
    return len(state.blank) - blankMove(state)
	
def generateMoves(state, listMoves):
    try:
        state.listBlank()
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
        return listMoves
		
def blankMove(state):
    x, y, c = -1, -1, 0
    listMoves=[]
    listMoves = generateMoves(state, listMoves)
    for i in listMoves:
        if x != i[1] and y != i[2]:
            c += 1
            x, y = i[1], i[2]
    return c