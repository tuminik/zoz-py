import Tkinter as tkinter
import tkMessageBox as messagebox
import sys
import copy
import time
from easygui import ccbox
from easygui import codebox
from search import Problem
from search import breadth_first_tree_search
from search import breadth_first_search
from search import uniform_cost_search
from search import depth_first_tree_search
from search import depth_first_graph_search
from search import depth_limited_search
#from search import recursive_depth_first_search
from search import iterative_deepening_search
from search import greedy_best_first_graph_search
#from search import recursive_greedy_best_first_graph_search
from search import astar_search
from utils import infinity
from zozParser import obtenerMapa
from problem import generateGoalState
from problem import zozProblem
printTableFather=False
MONOSPACE_FONT_SIZE =  10

class tables():
    tabs= []
    cont=0
    excTime=""
    expand=0
    buttons=[]
    filas=0
    columnas=0  
    
def tableToStr(tableS):
    tableR=[]
    for i in tableS:
        tableR.append("".join(i))
        tableR.append("\n")
    return tableR  

def callmove(i):
    def wrap():
        move(i)
    return wrap

def printText(text, eTime ,cont, textArea):
    try:
        text = "".join(text)  # convert a list or a tuple to a string
    except:
        sys.exit(16)
    textArea.configure(state=tkinter.NORMAL) 
    textArea.delete(1.0, tkinter.END)
    textArea.insert(tkinter.END,"ZOZ\n\n", "normal")    
    textArea.insert(tkinter.END,text, "normal")
    textArea.insert(tkinter.END,eTime, "normal")
    textArea.insert(tkinter.END,"\nPaso nro:" + str(cont), "normal")
    textArea.insert(tkinter.END,"\nCantidad de Pasos:" + str(len(tables.tabs)), "normal")
    textArea.insert(tkinter.END,"\nCantidad de Nodos Expandidos:" + str(tables.expand), "normal")
    textArea.configure(state=tkinter.DISABLED)
    
def changeTableNext(textA, tables):
    if tables.cont >= len(tables.tabs)-1:
        messagebox.showinfo("END", "BINGO!")
        tables.cont = -1
        text = tableToStr(tables.tabs[tables.cont])
    else:
        tables.cont=tables.cont + 1
        text = tableToStr(tables.tabs[tables.cont])
        printText(text, tables.excTime,tables.cont ,  textA)
        x=0
        for i in tables.tabs[tables.cont]:
            for j in i:
                if j=='*':
                    show=blank
                if j==' ':
                    show=brick
                if j=='#':
                    show=ficha  
                tables.buttons[x].configure(image=show)
                x+=1
        
    return
    
def changeTablePrev(textA, tables):
    if tables.cont <= 0:
        messagebox.showinfo("START", "PRESS NEXT STEP!")
       
    else:
        tables.cont=tables.cont-1
        text = tableToStr(tables.tabs[tables.cont])
        printText(text, tables.excTime ,tables.cont,  textA)
        x=0
        for i in tables.tabs[tables.cont]:
            for j in i:
                if j=='*':
                    show=blank
                if j==' ':
                    show=brick
                if j=='#':
                    show=ficha            
                tables.buttons[x].configure(image=show)
                x+=1
    return
    
def tableNext(textA,  table):
    def wrapNext():
        changeTableNext( textA, table)
    return wrapNext

def tablePrev(textA,  table):
    def wrapPrev():
        changeTablePrev( textA, table)
    return wrapPrev

TOP = "top"
YES = True
BOTH = "both"
BOTTOM = "bottom"
NO = False
X = "x"
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width    = int((screen_width * 0.8))
btnframe = tkinter.Frame(root)
btnframe.pack(side=TOP, expand=YES, fill=BOTH)

character_width = int((root_width * 0.6) / MONOSPACE_FONT_SIZE)
textArea = tkinter.Text(root,height=10,width=character_width, padx="1m", pady="1m")
textArea.pack(side=tkinter.LEFT, fill=BOTH, expand=YES)

nextbtn = tkinter.Button(root, command=tableNext(textArea, tables), text="NEXT STEP")
nextbtn.pack(side=BOTTOM, expand=NO, fill=X)

prevbtn = tkinter.Button(root, command=tablePrev(textArea, tables), text="PREV STEP")
prevbtn.pack(side=BOTTOM, expand=NO, fill=X)

zoz   = tkinter.PhotoImage(file="images/zozPlay.gif")
brick = tkinter.PhotoImage(file="images/brick.gif")
blank = tkinter.PhotoImage(file="images/blank.gif")
ficha = tkinter.PhotoImage(file="images/ficha.gif")
label = tkinter.Label(image=zoz)
label.pack(side=BOTTOM, expand=NO, fill=X)

def main():
    columna = 0
    fila = 0
    if len(sys.argv)==2:
        initial = obtenerMapa(sys.argv[1], fila, columna)
        goal = generateGoalState(initial) #encontrar el estado final
        zoz = zozProblem(initial, goal)
        x1= time.time()
        #search = astar_search(zoz)
        #search = breadth_first_tree_search(zoz)
        #search = breadth_first_search(zoz)
        #search = uniform_cost_search(zoz)
        #search = depth_first_tree_search(zoz)
        #search = depth_first_graph_search(zoz)
        search = depth_limited_search(zoz)
        #search = iterative_deepening_search(zoz)
        #search = greedy_best_first_graph_search(zoz, zoz.h)
        x2= time.time()
        tables.filas = initial.matrixX
        tables.columnas = initial.matrixY
        
        for i in initial.matrix:
            for j in i:
                if j=='*':
                    show=blank
                if j==' ':
                    show=brick
                if j=='#':
                    show=ficha          
                tables.buttons.append(tkinter.Label(btnframe, image=show))
                
        for i, button in enumerate(tables.buttons):
                button.grid(row=i//tables.columnas, column=i%tables.columnas, sticky="N"+"E"+"W"+"S")
        
        if search:            
            pathS = search.path()
            timediff = x2 - x1
            
            #Genera la secuencia de estados
            path = [node.state for node in pathS]
            states = []
            
            for state in path:
                states.append(state)
            
            i = len(states) - 1
            while i >= 0:
                tables.tabs.append(states[i].matrix)
                i -= 1
            tables.excTime= 'Tiempo:', round(timediff,4),'segundos'
            tables.expand = zoz.expanded
        else:
            print "No se pudo encontrar la solucion al problema"
    else:
        if len(sys.argv)<2:
            print "Debe recibir el nombre del archivo..."
        if len(sys.argv)>3:
            print "Demasiados arguementos..."
    
    text = tableToStr(tables.tabs[0])
    printText(text,tables.excTime, tables.cont,textArea)
    root.mainloop()

if __name__ == "__main__":
    main()
    