from node import Node
from random import randint, triangular

class Enviroment:
    enviroment_space = None
    number_of_rows = None
    number_of_columns = None
    def __init__(self,sizeX,sizeY,obstacles_rate):
        self.enviroment_space = self.create_enviroment_matrix(sizeX,sizeY)
        self.number_of_rows = len(self.enviroment_space)
        self.number_of_columns = len(self.enviroment_space[0])
        self.assing_positions(self.enviroment_space)
        self.generate_obstacles(obstacles_rate, 0)
        

    def print_enviroment(self):
        self.print_matrix(self.enviroment_space)
        
    def create_enviroment_matrix(self,n,m):
        matriz = []
        for i in range(n):
            a = [0]*m
            matriz.append(a)
        return matriz

    def assing_positions(self, M):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                M[i][j] = Node() 
                M[i][j].positionX = j
                M[i][j].positionY = i
                M[i][j].path_cost = 1
                
    def resetEnviroment(self):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns):
                node = self.enviroment_space[i][j]
                if node.representation_letter == ".":
                    node.representation_letter =  "\u25A1"
                node.parent = None
                
    def print_matrix(self, M):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                print(M[i][j].representation_letter, end = "|") 
            print()      

    def generate_obstacles(self, obstacles_rate, obstacles_places):
        env = self.enviroment_space
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                node = env[i][j]
                #if self.get_obstacles_percentage(obstacles_places) >= obstacles_rate:
                 #   return
                rand = randint(0,100)
                if rand > 85:
                    if node.is_obstacle == False:
                        node.is_obstacle = True
                        node.representation_letter = "\u25A0"
                        obstacles_places = obstacles_places + 1                
       # self.generate_obstacles(obstacles_rate, obstacles_places)
                
    def get_obstacles_places_percentage(self):
        env = self.enviroment_space
        obstacle_places = 0
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                if env[i][j].is_obstacle == True:
                    obstacle_places = obstacle_places + 1
        return self.get_obstacles_percentage(obstacle_places)
    
    def get_obstacles_percentage(self, obstacle_places):
        spaces = self.number_of_columns * self.number_of_rows
        return obstacle_places / spaces