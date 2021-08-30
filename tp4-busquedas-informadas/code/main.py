
from Enviroment import Enviroment
from GoalAgent import GoalAgent
#\u265E
#\u25A1 black square
#\u25A0 white squeare
env = Enviroment(100,100,0.2)
agent = GoalAgent(env)
env.print_enviroment() 
print("\n\n\n\n\n\n")
agent.startFindingTheGoal("a*")
env.print_enviroment()
print()
