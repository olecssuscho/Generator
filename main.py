import time
import numpy as np
from tkinter import *

root = Tk()

rowsGlobal=0
colsGlobal=0
matrix = np.empty((rowsGlobal, colsGlobal), dtype=object)
class Node:
    def __init__(self,row,col,val,ill,im):
        self.row=row
        self.col=col
        self.val=val
        self.ill=ill
        self.im=im
    
    def getVal(self):
        return self.val
    
    def getIll(self):
        return self.ill
    
    def getIm(self):
        return self.im
    
    def increaceIll(self):
        self.ill+=1
    
    def increaceIm(self):
        self.im+=1
    
def generateMatrix(rows:int,cols:int):
    global matrix,rowsGlobal,colsGlobal
    rowsGlobal=rows
    colsGlobal=cols
    matrix = np.empty((rowsGlobal, colsGlobal), dtype=object)
    for i in range(rowsGlobal):
        for j in range(colsGlobal):
            matrix[i][j]=Node(i,j,2,0,0)       
    matrix[int(rowsGlobal/2)][int(colsGlobal/2)].val=0
    return matrix

def printMatrix():
    global matrix, rowsGlobal, colsGlobal
    for i in range(rowsGlobal):
        for j in range(colsGlobal):
            print(matrix[i][j].getVal(),end=" ")
        print("\n")
    print("\n")

def mainEvent():
    global matrix, rowsGlobal, colsGlobal
    for i in range(rowsGlobal):
        for j in range(colsGlobal):
            if i==0 or j==0:
                continue
            if i==rowsGlobal-1 or j==colsGlobal-1:
                continue
            if matrix[i-1][j].getVal()==0 or matrix[i][j-1].getVal()==0 or matrix[i+1][j].getVal()==0 or matrix[i][j+1].getVal()==0:
                if matrix[i][j].getVal()==1 and matrix[i][j].getIm()==4:
                    matrix[i][j].val=2
                    matrix[i][j].im=0
                elif matrix[i][j].getVal()==1 and matrix[i][j].getIm()<4:
                    matrix[i][j].increaceIm()
                elif matrix[i][j].getVal()==0 and matrix[i][j].getIll()==6:
                    matrix[i][j].val=1
                    matrix[i][j].ill=0
                elif (matrix[i][j].getVal()==2 or matrix[i][j].getVal()==0) and matrix[i][j].getIll()<6:
                    matrix[i][j].val=0
                    matrix[i][j].increaceIll()
    printMatrix()

generateMatrix(5,5)
printMatrix()
while True:
    time.sleep(2)
    mainEvent()