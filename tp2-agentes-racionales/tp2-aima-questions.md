## Aima questions:

2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.
a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, perfectamente racional no, considerando que un agente perfectamente racional es uno que intenta obtener su medida de performance más alta posible, este agente no puede ver su entorno y no puede siquiera calcular la forma en la cual se podría mover para perder menos puntos, es decir no es perfectamente racional.

b. What about a reflex agent with state? Design such an agent.


Quizás podría ser un poco más racional que el anterior, pero igual no podría ser perfectamente racional, al ver por donde camina podría calcular que no pase por el mismo lado, para mejorar un poco la medida de performance pero igual no sería perfecto. 

c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Para el agente A:
Considerando que se podría optimizar el movimiento del agente en base a esto, si, podría llegar a ser muchisimo mas racional buscando un movimiento que los haga llegar a la medida de performance más alta.
Para el agente B:
El hecho de que ya tenga un estado no hace que tenga mucho sentido lo del entorno, así que el caso se vuelve muy igual al caso A.



2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)


a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, no podría, no trabaja para mejorar su medida de rendimiento de ninguna forma y encima es obstruida por cuestiones de terreno, el agente no aprende de sus movimientos.


b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

No, dentro del código en este trabajo práctico se probó que el agente que no es aleatorio es bastante mejor que el agente que es puramente aleatorio, quizás podrían ser similares en entornos muy reducidos pero de todas maneras el agente no aleatorio lo supera bastante bien.

c. Can you design an environment in which your randomized agent will perform poorly?
Show your results.


Un agente aleatorio baja con creces su performance en ambientes cada vez más grandes, la prueba está en el archivo de resultados en este mismo directorio.


d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Si, si lo podría superar, en el caso de que el estado del agente influya en sus acciones, como en un algoritmo de mejora para no volver por lugares que ya camino o algoritmos similares, terminará mejorando mucho su performance contra un agente reflexivo simple. Esta diferencia se haría cada vez más grande en entornos más grandes, ya que podria calcular las zonas en las cuales ya se limpio y nunca más volver para ese lado, lo cual lo haría tremendamente más eficiente

