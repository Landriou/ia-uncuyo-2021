from random import randint
from linkedlist import *
import copy

class HillClimbingAgent:
    env = None
    envMaximoLocal = None
    maxTryStates = None
    
    def __init__(self, enviroment, maxTryStates):
        self.env = enviroment
        self.maxTryStates = maxTryStates
        self.envMaximoLocal = copy.deepcopy(enviroment)

    def startClimbing(self):
        self.env.calculateH()
        targetFunction = self.env.calculateHObjetive()
        print("Target function actual", targetFunction)
        states = 0
        if targetFunction == 0: 
            return self.env, states
        for i in range(self.maxTryStates):
            states = states + 1
            ## Encuentro el mejor lugar 
            bestNode = self.findTheBestPlaceToSwitch()
            bestNode.HasBeenChoosed = True
            ##Copio el objeto
            newEnviroment = copy.deepcopy(self.env)
            bestNewNode = newEnviroment.enviroment_space[bestNode.i][bestNode.j]
            ## busco la reina de esa columna
            for k in range(self.env.number_of_rows):
                if newEnviroment.enviroment_space[k][bestNewNode.j].isQueen == True:
                    columnQueen = newEnviroment.enviroment_space[k][bestNewNode.j]
                    columnQueen.isQueen = False
                    columnQueen.representation_letter = "\u25A0 "
                    break
            ## cambio la reina
            bestNewNode.isQueen = True
            bestNewNode.representation_letter = "\u2655 "
            bestNewNode.HasBeenChoosed = True
            
            #calculo H devuelta
            newEnviroment.calculateH()
            newTargetFunction = newEnviroment.calculateHObjetive()
            if newTargetFunction == 0:
                return newEnviroment, states
            ## Si es mejor lo piso sobre el enviroment y voy a otra iteraicon ese objeto
            if newTargetFunction < targetFunction:
                self.env = newEnviroment
                self.envMaximoLocal = copy.deepcopy(newEnviroment)
        return self.envMaximoLocal, states
            ## Si es peor busco otra nodo para cambiar la reina, es decir, voy a otra iteracion.
            
    def findTheBestPlaceToSwitch(self):
        minH = 999
        bestNode = None
        for i in range(self.env.number_of_rows): 
            for j in range(self.env.number_of_columns): 
                    node = self.env.enviroment_space[i][j]
                    if node.H < minH and node.HasBeenChoosed == False and node.isQueen == False:
                        minH = node.H
                        if bestNode != None:
                            if bestNode.H == node.H:
                                if randint(0, 100) > 60:
                                    bestNode = node
                            else:
                                bestNode = node
                        else:
                            bestNode = node                 
                        
        return bestNode           
                

