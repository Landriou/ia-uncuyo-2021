
from linkedlist import LinkedList, add
from GeneticAgent import GeneticAgent
from SimulateAnnealingAgent import SimulatedAnnealingAgent
from Enviroment import Enviroment
from HillClimbingAgent import HillClimbingAgent
import time
#\u265E
#\u25A1 black square
#\u25A0 white squeare
queensNumber = 8


for i in range(1):
    print("estado inicial")
    env = Enviroment(queensNumber)
    env.print_enviroment()
    inicio2 = time.time()
    print("Simulated Annealing: ")
    sa = SimulatedAnnealingAgent(env, 2000)
    envAnnealed, states2 = sa.startAnnealing()
    envAnnealed.print_enviroment()
    print("target function final", envAnnealed.calculateHObjetive())
    fin2 = time.time()
    print("El tiempo final utilizado fue: ", fin2-inicio2)
    print("Estados recorridos ", states2)
    print()


for i in range(1):
    print()
    print("Genetic: ")
    inicio = time.time()
    ga = GeneticAgent(2000)
    population = LinkedList()

    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))
    add(population, Enviroment(queensNumber))



    envSolution, states3 = ga.startGenetic(population)
    envSolution.print_enviroment()
    print("target function final", envSolution.calculateHObjetive())
    print("Estados recorridos ", states3)
    fin = time.time()
    print("El tiempo final utilizado fue: ", fin-inicio)
    print()
print()   
for i in range(1):
    print("estado inicial")
    env = Enviroment(queensNumber)
    env.print_enviroment()
    print()
    inicio1 = time.time()
    print("Hill climbing: ", i)
    hc = HillClimbingAgent(env, 2000)
    envClimbed, states = hc.startClimbing()
    envClimbed.print_enviroment()
    print("target function final", envClimbed.calculateHObjetive())
    print("Estados recorridos ", states)
    fin1 = time.time()
    print("El tiempo final utilizado fue: ", fin1-inicio1)
    print()