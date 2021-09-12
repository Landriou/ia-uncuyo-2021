from Enviroment import Enviroment
from random import randint, triangular, uniform
from linkedlist import *
import copy
import math

class GeneticAgent:
    env = None
    envMaximoLocal = None
    maxTryStates = None
    
    def __init__(self, maxTryStates):
        self.maxTryStates = maxTryStates
        

    def startGenetic(self, population):
        states = 0
        bestFitness = 9999
        size = length(population)
        for i in range(self.maxTryStates):
            states = states + 1
            new_population = LinkedList()
            population = self.killTheWorst(population)
            while length(new_population) < size//2:
                x = self.randomSelection(population)
                y = self.randomSelection(population)
                child = self.reproduce(x,y)
                if randint(0,100) > 60:
                    self.mutate(child)
                child.calculateH()
                fitness = child.calculateHObjetive()
                if fitness < bestFitness:
                    bestFitness = fitness
                    self.envMaximoLocal = child
                if fitness == 0:
                    return self.envMaximoLocal, states
                add(new_population, child)
                
            population = new_population
                
        return self.envMaximoLocal, states
            ## Si es peor busco otra nodo para cambiar la reina, es decir, voy a otra iteracion.
    
    def randomSelection(self,population):
        bestEnv = None
        rand = randint(0, length(population) - 1)
        return access(population, rand)
        
        
        return bestEnv
    def killTheWorst(self, population):
        currentNode = population.head
        size = length(population)
        Q = PriorityQueue()
        while currentNode != None:
            env = currentNode.value
            env.calculateH()
            fitness = env.calculateHObjetive()
            enqueueWithPriority(Q, env, fitness) 
            
            
            currentNode = currentNode.nextNode
        best = LinkedList()
        while(length(best) < size//4):
            add(best, dequeueWithPriority(Q))
        return best
    def reproduce(self,x,y):
        xQueenString = x.getQueenString()
        yQueenString = y.getQueenString()
        
        n = x.number_of_columns
        rand = randint(0,n)
        finalQueenString = ""
        finalQueenString = xQueenString[0:rand] + yQueenString[rand:n]
        env = Enviroment(n)
        env.putQueensForQueenString(finalQueenString)
        return env
        
    def mutate(self, env):
        # queenString = env.getQueenString()
        # queenStringInitial = queenString
        # rand = randint(0, env.number_of_columns - 1)
        # counter = 0
        # for position in queenString:
        #     if counter == rand:
        #         if rand == env.number_of_columns - 1:
        #             queenString = queenString[0:rand] + str(rand)
        #         elif rand == 0:
        #             queenString = str(rand) + queenString[rand+1:]
        #         else:
        #             queenString = queenString[0:rand] + str(rand) + queenString[rand+1:]
        #     counter = counter + 1
        # env.putQueensForQueenString(queenString)
        bestNode = self.findTheBestPlaceToSwitch(env)
        bestNode.HasBeenChoosed = True
            ##Copio el objeto

        bestNewNode = env.enviroment_space[bestNode.i][bestNode.j]
            ## busco la reina de esa columna
        for k in range(env.number_of_rows):
            if env.enviroment_space[k][bestNewNode.j].isQueen == True:
                columnQueen = env.enviroment_space[k][bestNewNode.j]
                columnQueen.isQueen = False
                columnQueen.representation_letter = "\u25A0 "
                break
            ## cambio la reina
            bestNewNode.isQueen = True
            bestNewNode.representation_letter = "\u2655 "
            bestNewNode.HasBeenChoosed = True
           
    def findTheBestPlaceToSwitch(self, env):
        minH = 999
        bestNode = None
        env.calculateH()
        for i in range(env.number_of_rows): 
            for j in range(env.number_of_columns): 
                    node = env.enviroment_space[i][j]
                    if node.H < minH and node.HasBeenChoosed == False and node.isQueen == False:
                        minH = node.H
                        bestNode = node                 
                        
        return bestNode    
