from random import randint

# 1 is for dirty
# 0 is for clean
class Enviroment:
    enviroment_space = None
    number_of_rows = None
    number_of_columns = None
    def __init__(self,sizeX,sizeY,dirt_rate):
        self.enviroment_space = self.create_enviroment_matrix(sizeX,sizeY)
        self.number_of_rows = len(self.enviroment_space)
        self.number_of_columns = len(self.enviroment_space[0])
        self.put_some_trash_in_the_enviroment(dirt_rate, 0)

    def print_enviroment(self):
        self.print_matrix(self.enviroment_space)
        
    def create_enviroment_matrix(self,n,m):
        matriz = []
        for i in range(n):
            a = [0]*m
            matriz.append(a)
        return matriz

    def print_matrix(self, M):
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                print(M[i][j], end = " ") 
            print()      

    def put_some_trash_in_the_enviroment(self, dirty_rate, dirty_places):
        env = self.enviroment_space
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                if self.get_dirty_percentage(dirty_places) >= dirty_rate:
                    return
                rand = randint(0,100)
                if rand > 90:
                    if env[i][j] == 0:
                        env[i][j] = 1
                        dirty_places = dirty_places + 1                
        self.put_some_trash_in_the_enviroment(dirty_rate, dirty_places)
                
    def get_dirty_places_percentage(self):
        env = self.enviroment_space
        dirty_places = 0
        for i in range(self.number_of_rows): 
            for j in range(self.number_of_columns): 
                if env[i][j] == 1:
                    dirty_places = dirty_places + 1
        return self.get_dirty_percentage(dirty_places)
    
    def get_dirty_percentage(self, dirtyPlaces):
        spaces = self.number_of_columns * self.number_of_rows
        return dirtyPlaces / spaces
    
    
    def accept_action(self,action):
        print("hola") 