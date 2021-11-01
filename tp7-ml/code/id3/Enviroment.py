import copy
from node import Node
from random import randint

class Enviroment:
    enviroment_space = None
    number_of_rows = None
    number_of_columns = None
    initialState = None
    Hactual = None
    def __init__(self,size):
        self.enviroment_space = self.create_enviroment_matrix(size,size)
        self.number_of_rows = len(self.enviroment_space)
        self.number_of_columns = len(self.enviroment_space[0])
        self.assingNodePositions(self.enviroment_space)
        self.assingQueens_positions(self.enviroment_space)
        self.initialState = copy.deepcopy(self.enviroment_space)
        
    def print_enviroment(self):
        self.print_matrix(self.enviroment_space)
        
    def create_enviroment_matrix(self,n,m):
        matriz = []
        for i in range(n):
            a = ["\u25A0 "]*m
            matriz.append(a)
        return matriz

    def assingQueens_positions(self, M):
        for j in range(self.number_of_columns):
                rand = randint(0, self.number_of_rows - 1)
                M[rand][j].representation_letter = "\u2655 "
                M[rand][j].isQueen = True

    def assingNodePositions(self, M):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                M[i][j] = Node()
                M[i][j].representation_letter = "\u25A0 "
                M[i][j].i = i
                M[i][j].j = j
                M[i][j].isQueen = False
                
    def resetEnviroment(self):
        self.enviroment_space = self.initialState
                
    def print_matrix(self, M):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                print(M[i][j].representation_letter, end=" ") 
            print()     
    
    ################# H functions #############
    
            
    def print_matrixHFunctions(self):
        M = self.enviroment_space
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                print(M[i][j].H, end=" ") 
            print()  
            
    def calculateH(self):
        M = self.enviroment_space
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                HFunction = 0
                HFunction = HFunction + self.findUpQueen(M,i, j)
                HFunction = HFunction + self.findDownQueen(M,i, j)
                HFunction = HFunction + self.findRightQueen(M,i, j)
                HFunction = HFunction + self.findLeftQueen(M,i, j)
                HFunction = HFunction + self.findUpRightQueen(M,i, j)
                HFunction = HFunction + self.findUpLeftQueen(M,i, j)
                HFunction = HFunction + self.findDownRightQueen(M,i, j)
                HFunction = HFunction + self.findDownLeftQueen(M,i, j)
                M[i][j].H = HFunction 
                M[i][j].HasBeenChoosed = False  
    
    def calculateHObjetive(self):
        M = self.enviroment_space
        HFunction = 0
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                if M[i][j].isQueen == True:
                     HFunction = HFunction + M[i][j].H
        self.Hactual = HFunction
        return HFunction       
    
    def getQueenString(self):
        queenString = ""
        M = self.enviroment_space
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                if M[j][i].isQueen == True:
                    queenString = queenString + str(j)     
        return queenString     
    
    def putQueensForQueenString(self, queenString):
        j = 0
        self.assingNodePositions(self.enviroment_space)
        for position in queenString:
            node = self.enviroment_space[int(position)][j] 
            node.isQueen = True
            node.representation_letter = "\u2655 "
            j = j + 1
            
             
    def findUpQueen(self, M,i, j):
        i = i - 1
        while i >= 0:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i - 1
        return 0
        
        
    def findDownQueen(self, M, i, j):
        i = i + 1
        while i <= self.number_of_rows - 1:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i + 1
        return 0
    
    def findRightQueen(self, M, i, j):
        j = j + 1
        while j <= self.number_of_columns - 1:
            if M[i][j].isQueen == True:
                return 1
            else:
                j = j + 1
        return 0
    
    def findLeftQueen(self, M, i, j):
        j = j - 1
        while j >= 0:
            if M[i][j].isQueen == True:
                return 1
            else:
                j = j - 1
        return 0
    
    def findUpRightQueen(self, M,i, j):
        i = i - 1
        j = j + 1
        while i >= 0 and j <= self.number_of_columns - 1:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i - 1
                j = j + 1
        return 0
    
    def findUpLeftQueen(self, M,i, j):
        i = i - 1
        j = j - 1
        while i >= 0 and j >= 0:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i - 1
                j = j - 1
        return 0
    
    def findDownRightQueen(self, M,i, j):
        i = i + 1
        j = j + 1
        while i <= self.number_of_rows - 1 and j <= self.number_of_columns - 1:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i + 1
                j = j + 1
        return 0
    
    def findDownLeftQueen(self, M,i, j):
        i = i + 1
        j = j - 1
        while i <= self.number_of_rows - 1 and j >= 0:
            if M[i][j].isQueen == True:
                return 1
            else:
                i = i + 1
                j = j - 1
        return 0