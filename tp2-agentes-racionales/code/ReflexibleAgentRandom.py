from random import randint
from ReflexibleAgent import ReflexibleAgent
class ReflexibleAgentRandom(ReflexibleAgent):
    def action(self):
        rand = randint(1,6)
        if rand == 1:
            self.life_time = self.life_time - 1
            super().up()
        if rand == 2:
            self.life_time = self.life_time - 1
            super().down()
        if rand == 3:
            self.life_time = self.life_time - 1
            super().left()
        if rand == 4:
            self.life_time = self.life_time - 1
            super().right()
        if rand == 5:
            super().clean()
        if rand == 6:
            super().idle()