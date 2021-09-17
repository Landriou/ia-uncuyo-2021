from random import randint, uniform
from linkedlist import *
import copy
import math

class SimulatedAnnealingAgent:
    env = None
    envMaximoLocal = None
    maxTryStates = None
    
    def __init__(self, enviroment, maxTryStates):
        self.env = enviroment
        self.maxTryStates = maxTryStates
        self.envMaximoLocal = copy.deepcopy(enviroment)

    def startAnnealing(self):
        self.env.calculateH()
        targetFunction = self.env.calculateHObjetive()
        states = 0
        if targetFunction == 0: 
            return self.env, states
        for i in range(self.maxTryStates):
            states = states + 1
            T = self.schedule(states)
            ## Encuentro el mejor lugar 
            bestNode = self.findThePlaceToSwitch()
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
            ## Si es mejor lo piso sobre el enviroment y voy a otra iteracion ese objeto
            if newTargetFunction < targetFunction:
                self.env = newEnviroment
                self.envMaximoLocal = copy.deepcopy(newEnviroment)
            else:
                if uniform(0,1) < 1/(newTargetFunction/T):
                    self.env = newEnviroment
                    self.envMaximoLocal = copy.deepcopy(newEnviroment)
                
        return self.envMaximoLocal, states
            ## Si es peor busco otra nodo para cambiar la reina, es decir, voy a otra iteracion.
            
    def findThePlaceToSwitch(self):
        bestNode = None
        while bestNode == None:
            randI = randint(0, self.env.number_of_rows -1)
            randJ = randint(0, self.env.number_of_columns -1)
            node = self.env.enviroment_space[randI][randJ]
            if node.HasBeenChoosed == False and node.isQueen == False:
                bestNode = node
        return bestNode           
                
    def schedule(self, t):
        return t/10
