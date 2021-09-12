## Metricas con A*
|Metrica | bfs | dfs |uniform cost|
| ------------- | ------------- |------------- |------------- |
|Desviacion Estandar |2598.666192| 2068.856447 |2598.666192|
|Media	| 4639.387097 |3794.258065 | 4639.387097|

## Grafico de barras
![image](https://user-images.githubusercontent.com/39389586/131274456-657b14ba-d696-4da7-8781-407e7fcc5763.png)

## Pregunta C
C)  Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.
Me parece que el mas adecuado para resolver este tipo de problema es la busqueda en amplitud.
Porque si bien recorre menos estados, es bastante seguro que va a encontrar la respuesta en cambio frente al algoritmo de busqueda en profundidad, este ultimo
puede tardar un monton en muchisimos casos y no encontrar siquiera la respuesta, aunque explore menos nodos
por eso pienso que el algoritmo en amplitud es bastante mejor. 
Respecto al de busqueda uniforme, como los caminos tienen el mismo costo, los resultados son identicos al de busqueda en amplitud, si hubiera costos involucrados, eligiria el de costo uniforme sin dudarlo.
