from ReflexibleAgentRandom import ReflexibleAgentRandom
from Enviroment import Enviroment
from ReflexibleAgent import ReflexibleAgent

env2x2_0point1 = Enviroment(2,2,0.1)
env4x4_0point1 = Enviroment(4,4,0.1)
env8x8_0point1 = Enviroment(8,8,0.1)
env16x16_0point1 = Enviroment(16,16,0.1)
env32x32_0point1 = Enviroment(32,32,0.1)
env64x64_0point1 = Enviroment(64,64,0.1)
env128x128_0point1 = Enviroment(128,128,0.1)

env2x2_0point2 = Enviroment(2,2,0.2)
env4x4_0point2 = Enviroment(4,4,0.2)
env8x8_0point2 = Enviroment(8,8,0.2)
env16x16_0point2 = Enviroment(16,16,0.2)
env32x32_0point2 = Enviroment(32,32,0.2)
env64x64_0point2 = Enviroment(64,64,0.2)
env128x128_0point2 = Enviroment(128,128,0.2)

env2x2_0point4 = Enviroment(2,2,0.4)
env4x4_0point4 = Enviroment(4,4,0.4)
env8x8_0point4 = Enviroment(8,8,0.4)
env16x16_0point4 = Enviroment(16,16,0.4)
env32x32_0point4 = Enviroment(32,32,0.4)
env64x64_0point4 = Enviroment(64,64,0.4)
env128x128_0point4 = Enviroment(128,128,0.4)

env2x2_0point8 = Enviroment(2,2,0.8)
env4x4_0point8 = Enviroment(4,4,0.8)
env8x8_0point8 = Enviroment(8,8,0.8)
env16x16_0point8 = Enviroment(16,16,0.8)
env32x32_0point8 = Enviroment(32,32,0.8)
env64x64_0point8 = Enviroment(64,64,0.8)
env128x128_0point8 = Enviroment(128,128,0.8)


test_env = Enviroment(16,16,0.8)
test_env.print_enviroment()
print("porcentaje de suiciedad antes de limpiar", test_env.get_dirty_places_percentage())
normal_agent = ReflexibleAgent(test_env)
normal_agent.start_cleanning()
test_env.print_enviroment()
print("porcentaje de suiciedad despues de limpiar", test_env.get_dirty_places_percentage())
print("medida de performance del agente normal", normal_agent.get_performance_measure())

test_env2 = Enviroment(16,16,0.8)

test_env2.print_enviroment()
print("porcentaje de suiciedad antes de limpiar", test_env2.get_dirty_places_percentage())
random_agent = ReflexibleAgentRandom(test_env2)
random_agent.start_cleanning()
test_env2.print_enviroment()
print("porcentaje de suiciedad despues de limpiar", test_env2.get_dirty_places_percentage())
print("medida de performance del agente random", random_agent.get_performance_measure())


def performance_measure_print(size, performance, dirtiness):
    print("Para un ambiente de ", size, "x", size, "con una suiciedad de", dirtiness, "la performance del agente fue de ", performance)

# 0.1 dirtiness
env2x2_0point1Agent = ReflexibleAgent(env2x2_0point1)
env2x2_0point1Agent.start_cleanning()
performance_measure_print(2, env2x2_0point1Agent.get_performance_measure(), 0.1)


env4x4_0point1Agent = ReflexibleAgent(env4x4_0point1)
env4x4_0point1Agent.start_cleanning()
performance_measure_print(4, env4x4_0point1Agent.get_performance_measure(), 0.1)


env8x8_0point1Agent = ReflexibleAgent(env8x8_0point1)
env8x8_0point1Agent.start_cleanning()
performance_measure_print(8, env8x8_0point1Agent.get_performance_measure(), 0.1)


env16x16_0point1Agent = ReflexibleAgent(env16x16_0point1)
env16x16_0point1Agent.start_cleanning()
performance_measure_print(16, env16x16_0point1Agent.get_performance_measure(), 0.1)

env32x32_0point1Agent = ReflexibleAgent(env32x32_0point1)
env32x32_0point1Agent.start_cleanning()
performance_measure_print(32, env32x32_0point1Agent.get_performance_measure(), 0.1)

env64x64_0point1Agent = ReflexibleAgent(env64x64_0point1)
env64x64_0point1Agent.start_cleanning()
performance_measure_print(64, env64x64_0point1Agent.get_performance_measure(), 0.1)

env128x128_0point1Agent = ReflexibleAgent(env128x128_0point1)
env128x128_0point1Agent.start_cleanning()
performance_measure_print(128, env128x128_0point1Agent.get_performance_measure(), 0.1)



# 0.2 dirtiness

env2x2_0point2Agent = ReflexibleAgent(env2x2_0point2)
env2x2_0point2Agent.start_cleanning()
performance_measure_print(2, env2x2_0point2Agent.get_performance_measure(), 0.2)


env4x4_0point2Agent = ReflexibleAgent(env4x4_0point2)
env4x4_0point2Agent.start_cleanning()
performance_measure_print(4, env4x4_0point2Agent.get_performance_measure(), 0.2)


env8x8_0point2Agent = ReflexibleAgent(env8x8_0point2)
env8x8_0point2Agent.start_cleanning()
performance_measure_print(8, env8x8_0point2Agent.get_performance_measure(), 0.2)


env16x16_0point2Agent = ReflexibleAgent(env16x16_0point2)
env16x16_0point2Agent.start_cleanning()
performance_measure_print(16, env16x16_0point2Agent.get_performance_measure(), 0.2)

env32x32_0point2Agent = ReflexibleAgent(env32x32_0point2)
env32x32_0point2Agent.start_cleanning()
performance_measure_print(32, env32x32_0point2Agent.get_performance_measure(), 0.2)

env64x64_0point2Agent = ReflexibleAgent(env64x64_0point2)
env64x64_0point2Agent.start_cleanning()
performance_measure_print(64, env64x64_0point2Agent.get_performance_measure(), 0.2)

env128x128_0point2Agent = ReflexibleAgent(env128x128_0point2)
env128x128_0point2Agent.start_cleanning()
performance_measure_print(128, env128x128_0point2Agent.get_performance_measure(), 0.2)


####### 0.4 dirtiness ############


env2x2_0point4Agent = ReflexibleAgent(env2x2_0point4)
env2x2_0point4Agent.start_cleanning()
performance_measure_print(2, env2x2_0point4Agent.get_performance_measure(), 0.4)


env4x4_0point4Agent = ReflexibleAgent(env4x4_0point4)
env4x4_0point4Agent.start_cleanning()
performance_measure_print(4, env4x4_0point4Agent.get_performance_measure(), 0.4)


env8x8_0point4Agent = ReflexibleAgent(env8x8_0point4)
env8x8_0point4Agent.start_cleanning()
performance_measure_print(8, env8x8_0point4Agent.get_performance_measure(), 0.4)


env16x16_0point4Agent = ReflexibleAgent(env16x16_0point4)
env16x16_0point4Agent.start_cleanning()
performance_measure_print(16, env16x16_0point4Agent.get_performance_measure(), 0.4)

env32x32_0point4Agent = ReflexibleAgent(env32x32_0point4)
env32x32_0point4Agent.start_cleanning()
performance_measure_print(32, env32x32_0point4Agent.get_performance_measure(), 0.4)

env64x64_0point4Agent = ReflexibleAgent(env64x64_0point4)
env64x64_0point4Agent.start_cleanning()
performance_measure_print(64, env64x64_0point4Agent.get_performance_measure(), 0.4)

env128x128_0point4Agent = ReflexibleAgent(env128x128_0point4)
env128x128_0point4Agent.start_cleanning()
performance_measure_print(128, env128x128_0point4Agent.get_performance_measure(), 0.4)


#### 0.8 dirtiness ###


env2x2_0point8Agent = ReflexibleAgent(env2x2_0point8)
env2x2_0point8Agent.start_cleanning()
performance_measure_print(2, env2x2_0point8Agent.get_performance_measure(), 0.8)


env4x4_0point8Agent = ReflexibleAgent(env4x4_0point8)
env4x4_0point8Agent.start_cleanning()
performance_measure_print(4, env4x4_0point8Agent.get_performance_measure(), 0.8)


env8x8_0point8Agent = ReflexibleAgent(env8x8_0point8)
env8x8_0point8Agent.start_cleanning()
performance_measure_print(8, env8x8_0point8Agent.get_performance_measure(), 0.8)


env16x16_0point8Agent = ReflexibleAgent(env16x16_0point8)
env16x16_0point8Agent.start_cleanning()
performance_measure_print(16, env16x16_0point8Agent.get_performance_measure(), 0.8)

env32x32_0point8Agent = ReflexibleAgent(env32x32_0point8)
env32x32_0point8Agent.start_cleanning()
performance_measure_print(32, env32x32_0point8Agent.get_performance_measure(), 0.8)

env64x64_0point8Agent = ReflexibleAgent(env64x64_0point8)
env64x64_0point8Agent.start_cleanning()
performance_measure_print(64, env64x64_0point8Agent.get_performance_measure(), 0.8)

env128x128_0point8Agent = ReflexibleAgent(env128x128_0point8)
env128x128_0point8Agent.start_cleanning()
performance_measure_print(128, env128x128_0point8Agent.get_performance_measure(), 0.8)
