from random import randint
from linkedlist import *
import math

class GoalAgent:
    env = None
    positionX = None # Column in the enviroment
    positionY = None # Row in the enviroment
    life_time = None
    performance_measure = None
    representation_letter = "\u265E"
    goalPositionX = None
    goalPositionY = None
    
    def __init__(self, enviroment):
        self.env = enviroment
        self.positionX = randint(0, self.env.number_of_columns - 1)
        self.positionY = randint(0, self.env.number_of_rows - 1)
        self.env.enviroment_space[self.positionY][self.positionX].representation_letter = self.representation_letter
        self.life_time = 1000
        self.performance_measure = 0
        self.settingGoal()
      
    def get_performance_measure(self):
        return self.performance_measure    
 
    def settingGoal(self):
        self.goalPositionX = randint(0, self.env.number_of_columns - 1)
        self.goalPositionY = randint(0, self.env.number_of_rows - 1)
        self.env.enviroment_space[self.goalPositionY][self.goalPositionX].representation_letter = "G"
        print("G esta en la posicion", self.goalPositionY, self.goalPositionX )
        print("El agente esta en la posicion", self.positionY, self.positionX )
 
    def startFindingTheGoal(self, algorythm):
        self.env.resetEnviroment()
        if algorythm == "bfs":
            node = self.traverseBreadFirst(self.env.enviroment_space[self.positionY][self.positionX],self.goalPositionX,self.goalPositionY)
            if node != None:
                self.getSolutionPath(node)
                
        if algorythm == "dfs":
            node = self.traverseDeepFirstLimited(self.env.enviroment_space[self.positionY][self.positionX],self.goalPositionX,self.goalPositionY, 8000)
            if node != None:
                self.getSolutionPath(node)
        
        if algorythm == "uc":
            node = self.uniformCostTraverse(self.env.enviroment_space[self.positionY][self.positionX],self.goalPositionX,self.goalPositionY)
            if node != None:
                self.getSolutionPath(node)
                
        if algorythm == "a*":
            node = self.AStarTraverse(self.env.enviroment_space[self.positionY][self.positionX],self.goalPositionX,self.goalPositionY)
            if node != None:
                self.getSolutionPath(node)
        
        
    # Returns True if the accions was performed, otherwise, return false
    def getUpNode(self, node):
        # The agent cant move more than the position 0 in the env matrix
        max_up_position = self.env.number_of_rows - 1
        if node.positionY == max_up_position:
            return None
        else:
            return self.env.enviroment_space[node.positionY + 1][node.positionX]       
     
     
     # Returns True if the accions was performed, otherwise, return false
    def getDownNode(self, node):
        # The agent cant move more than the max of rows - 1 (because arrays starts in 0) in the env matrix
        max_down_position = 0
        
        if node.positionY == max_down_position:
            return None
        else:
            return self.env.enviroment_space[node.positionY - 1][node.positionX]   
        
    # Returns True if the accions was performed, otherwise, return false
    def getRightNode(self, node):
        # The agent cant move more than the max of columns - 1 in the env matrix
        max_right_position = self.env.number_of_columns - 1
        if node.positionX == max_right_position:
            return None
        else:
            return self.env.enviroment_space[node.positionY][node.positionX + 1]   
        
        # Returns True if the accions was performed, otherwise, return false
    def getLeftNode(self, node):
        # The agent cant move more than 0 in the env matrix
        max_left_position = 0
        if node.positionX == max_left_position:
            return None
        else:
            return self.env.enviroment_space[node.positionY][node.positionX - 1]   
        

    def isSolution(self, node, positionXGoal, positionYGoal):
        if node.positionX == positionXGoal and node.positionY == positionYGoal:
            return True
        else:
            return False
            
    def traverseBreadFirst(self, node, positionXGoal, positionYGoal):
        if node == None:
            return None
        if self.isSolution(node, positionXGoal, positionYGoal):
            print("La cantidad de estados explorados fue", 1)
            return node
        
        frontier = LinkedList()
        explored = LinkedList()
        enqueue(frontier,node) #Meto la raiz en una cola aux

        while(length(frontier) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
            actualNode = dequeue(frontier)
            enqueue(explored,actualNode)
            
            up = self.getUpNode(actualNode)
            down = self.getDownNode(actualNode)
            left = self.getLeftNode(actualNode)
            right = self.getRightNode(actualNode)
            
            if up != None:
                if search(frontier, up) == None and search(explored, up) == None and up.is_obstacle != True:
                    up.parent = actualNode
                    if self.isSolution(up, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return up
                    enqueue(frontier,up)
            
            if down != None:
                if search(frontier, down) == None and search(explored, down) == None and down.is_obstacle != True:
                    down.parent = actualNode
                    if self.isSolution(down, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return down
                    enqueue(frontier, down)
                    
            if left != None:
                if search(frontier, left) == None and search(explored, left) == None and left.is_obstacle != True:
                    left.parent = actualNode
                    if self.isSolution(left, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return left
                    enqueue(frontier, left)        
            
            if right != None:
                if search(frontier, right) == None and search(explored, right) == None and right.is_obstacle != True:
                    right.parent = actualNode
                    if self.isSolution(right, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return right
                    enqueue(frontier, right)  
        print("La cantidad de estados explorados fue", length(explored))
        return None  

    def traverseDeepFirstLimited(self, node, positionXGoal, positionYGoal, limit):
        if node == None:
            return None
        if self.isSolution(node, positionXGoal, positionYGoal):
            print("La cantidad de estados explorados fue", 1)
            return node
        
        frontier = LinkedList()
        explored = LinkedList()
        push(frontier,node) #Meto la raiz en una pila aux

        while(length(frontier) != 0 and limit > 0):#Voy sacando uno por uno de la pila auxiliar mientras meto en otra pila los hijos de cada uno y asi sucesivamente
            limit = limit - 1
            actualNode = pop(frontier)
            push(explored, actualNode)
            
            up = self.getUpNode(actualNode)
            down = self.getDownNode(actualNode)
            left = self.getLeftNode(actualNode)
            right = self.getRightNode(actualNode)
            
            if up != None:
                if search(frontier, up) == None and search(explored, up) == None and up.is_obstacle != True:
                    up.parent = actualNode
                    if self.isSolution(up, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return up
                    enqueue(frontier,up)
            
            if down != None:
                if search(frontier, down) == None and search(explored, down) == None and down.is_obstacle != True:
                    down.parent = actualNode
                    if self.isSolution(down, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return down
                    enqueue(frontier, down)
                    
            if left != None:
                if search(frontier, left) == None and search(explored, left) == None and left.is_obstacle != True:
                    left.parent = actualNode
                    if self.isSolution(left, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return left
                    enqueue(frontier, left)        
            
            if right != None:
                if search(frontier, right) == None and search(explored, right) == None and right.is_obstacle != True:
                    right.parent = actualNode
                    if self.isSolution(right, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return right
                    enqueue(frontier, right)  
        print("La cantidad de estados explorados fue", length(explored))
        return None  

    def uniformCostTraverse(self, node, positionXGoal, positionYGoal):
        if node == None:
            return None
        if self.isSolution(node, positionXGoal, positionYGoal):
            print("La cantidad de estados explorados fue", 1)
            return node
        
        frontier = PriorityQueue()
        explored = LinkedList()
        enqueueWithPriority(frontier, node, node.path_cost) #Meto la raiz en una cola aux

        while(length(frontier) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
            actualNode = dequeueWithPriority(frontier)
            enqueue(explored,actualNode)
            
            up = self.getUpNode(actualNode)
            down = self.getDownNode(actualNode)
            left = self.getLeftNode(actualNode)
            right = self.getRightNode(actualNode)
            
            if up != None:
                if search(frontier, up) == None and search(explored, up) == None and up.is_obstacle != True:
                    up.parent = actualNode
                    up.path_cost = up.path_cost + actualNode.path_cost
                    if self.isSolution(up, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return up
                    enqueueWithPriority(frontier,up, up.path_cost)
            
            if down != None:
                if search(frontier, down) == None and search(explored, down) == None and down.is_obstacle != True:
                    down.parent = actualNode
                    down.path_cost = down.path_cost + actualNode.path_cost
                    if self.isSolution(down, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return down
                    enqueueWithPriority(frontier, down, down.path_cost)
                    
            if left != None:
                if search(frontier, left) == None and search(explored, left) == None and left.is_obstacle != True:
                    left.parent = actualNode
                    left.path_cost = left.path_cost + actualNode.path_cost
                    if self.isSolution(left, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return left
                    enqueueWithPriority(frontier, left, left.path_cost)        
            
            if right != None:
                if search(frontier, right) == None and search(explored, right) == None and right.is_obstacle != True:
                    right.parent = actualNode
                    right.path_cost = right.path_cost + actualNode.path_cost
                    if self.isSolution(right, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return right
                    enqueueWithPriority(frontier, right, right.path_cost)  
        print("La cantidad de estados explorados fue", length(explored))
        return None  


    def AStarTraverse(self, node, positionXGoal, positionYGoal):
        if node == None:
            return None
        if self.isSolution(node, positionXGoal, positionYGoal):
            print("La cantidad de estados explorados fue", 1)
            return node
        
        
        frontier = PriorityQueue()
        explored = LinkedList()
        enqueueWithPriority(frontier, node, node.path_cost) #Meto la raiz en una cola aux

        while(length(frontier) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
            leng = length(explored)
            actualNode = dequeueWithPriority(frontier)
            heuristic = math.sqrt(abs(actualNode.positionX - positionXGoal) **2 + abs(actualNode.positionY - positionYGoal) **2)
            actualNode.path_cost = actualNode.path_cost + heuristic
            enqueue(explored,actualNode)
            
            up = self.getUpNode(actualNode)
            down = self.getDownNode(actualNode)
            left = self.getLeftNode(actualNode)
            right = self.getRightNode(actualNode)
            
            if up != None:
                if search(frontier, up) == None and search(explored, up) == None and up.is_obstacle != True:
                    up.parent = actualNode
                    up.path_cost = up.path_cost + actualNode.path_cost
                    if self.isSolution(up, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return up
                    enqueueWithPriority(frontier,up, up.path_cost)
            
            if down != None:
                if search(frontier, down) == None and search(explored, down) == None and down.is_obstacle != True:
                    down.parent = actualNode
                    down.path_cost = down.path_cost + actualNode.path_cost
                    if self.isSolution(down, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return down
                    enqueueWithPriority(frontier, down, down.path_cost)
                    
            if left != None:
                if search(frontier, left) == None and search(explored, left) == None and left.is_obstacle != True:
                    left.parent = actualNode
                    left.path_cost = left.path_cost + actualNode.path_cost
                    if self.isSolution(left, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return left
                    enqueueWithPriority(frontier, left, left.path_cost)        
            
            if right != None:
                if search(frontier, right) == None and search(explored, right) == None and right.is_obstacle != True:
                    right.parent = actualNode
                    right.path_cost = right.path_cost + actualNode.path_cost
                    if self.isSolution(right, positionXGoal, positionYGoal) == True:
                        print("La cantidad de estados explorados fue", length(explored))
                        return right
                    enqueueWithPriority(frontier, right, right.path_cost)  
        print("La cantidad de estados explorados fue", length(explored))
        return None  

        
    def getSolutionPath(self, node):
        currentNode = node.parent
        while currentNode.parent != None:
            currentNode.representation_letter = "."
            currentNode = currentNode.parent
