
from Enviroment import Enviroment
from GoalAgent import GoalAgent
#\u265E
#\u25A1 black square
#\u25A0 white squeare
env = Enviroment(100,100,0.2)
agent = GoalAgent(env)
env.print_enviroment()
print("\n\n\n\n\n\n")
agent.startFindingTheGoal("bfs")
env.print_enviroment()
print()
agent.startFindingTheGoal("dfs")
env.print_enviroment()
print()
agent.startFindingTheGoal("uc")
print()
env.print_enviroment()