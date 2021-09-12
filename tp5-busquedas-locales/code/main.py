
from linkedlist import LinkedList, add
from GeneticAgent import GeneticAgent
from SimulateAnnealingAgent import SimulatedAnnealingAgent
from Enviroment import Enviroment
from HillClimbingAgent import HillClimbingAgent
#\u265E
#\u25A1 black square
#\u25A0 white squeare
# print("Estado inicial")
# env = Enviroment(8)
# env.print_enviroment()
# print()

# hc = HillClimbingAgent(env, 1000)
# envClimbed, states = hc.startClimbing()
# envClimbed.print_enviroment()
# print("target function final", envClimbed.calculateHObjetive())
# print("Estados recorridos ", states)
# print()


# env.resetEnviroment()

# sa = SimulatedAnnealingAgent(env, 10000)
# envAnnealed, states2 = sa.startAnnealing()
# envAnnealed.print_enviroment()
# print("target function final", envAnnealed.calculateHObjetive())
# print("Estados recorridos ", states2)
# print()


for i in range(30):
    ga = GeneticAgent(1000)
    population = LinkedList()

    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))
    add(population, Enviroment(8))



    envSolution, states3 = ga.startGenetic(population)
    envSolution.print_enviroment()
    print("target function final", envSolution.calculateHObjetive())
    print("Estados recorridos ", states3)
    print()