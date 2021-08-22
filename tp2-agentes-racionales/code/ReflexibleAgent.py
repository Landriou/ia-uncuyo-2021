from random import randint


class ReflexibleAgent:
    env = None
    positionX = None # Column in the enviroment
    positionY = None # Row in the enviroment
    life_time = None
    performance_measure = None
    
    def __init__(self, enviroment):
        self.env = enviroment
        self.positionX = randint(0, self.env.number_of_columns - 1)
        self.positionY = randint(0, self.env.number_of_rows - 1)
        self.life_time = 1000
        self.performance_measure = 0
      
    def start_cleanning(self):
        while self.life_time >= 0:
            self.action() 
      
    def get_performance_measure(self):
        return self.performance_measure
    
    def action(self):
        if self.scan() == 1:
            self.clean()
        else:
            self.idle()
        self.movement()
             
    def scan(self):
        return self.env.enviroment_space[self.positionY][self.positionX]
        
    def clean(self):
        if self.scan() == 1:
            self.performance_measure = self.performance_measure + 1
        self.env.enviroment_space[self.positionY][self.positionX] = 0
        self.life_time = self.life_time - 1
        
    def idle(self):
        self.life_time = self.life_time - 1
        
    def movement(self):
        self.life_time = self.life_time - 1
        
        rand = randint(1,4)
        if rand == 1:
            self.up()
        
        if rand == 2:
            self.down()
            
        if rand == 3:
            self.left()
            
        if rand == 4:
            self.right()   
        
    # Returns True if the accions was performed, otherwise, return false
    def up(self):
        # The agent cant move more than the position 0 in the env matrix
        max_up_position = self.env.number_of_rows - 1
        if self.positionY == max_up_position:
            return False
        else:
            self.positionY = self.positionY + 1
            return True       
     
     
     # Returns True if the accions was performed, otherwise, return false
    def down(self):
        # The agent cant move more than the max of rows - 1 (because arrays starts in 0) in the env matrix
        max_down_position = 0
        
        if self.positionY == max_down_position:
            return False
        else:
            self.positionY = self.positionY - 1
            return True       
        
    # Returns True if the accions was performed, otherwise, return false
    def right(self):
        # The agent cant move more than the max of columns - 1 in the env matrix
        max_right_position = self.env.number_of_columns - 1
        if self.positionX == max_right_position:
            return False
        else:
            self.positionX = self.positionX + 1
            return True  
        
        # Returns True if the accions was performed, otherwise, return false
    def left(self):
        # The agent cant move more than 0 in the env matrix
        max_left_position = 0
        if self.positionX == max_left_position:
            return False
        else:
            self.positionX = self.positionX - 1
            return True  
        
        