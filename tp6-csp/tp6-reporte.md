## 1)
Una solucion podria ser la siguiente, usando constraints globales, ponemos como restricción las reglas principales del sudoku, poniendo que cada fila sea AllDiff con cada uno de los elementos de la fila hasta la última fila, repetimos procedimiento con las columnas, y luego con las diagonales de cada cuadrado.

 Alldiff (A1, A2, A3, A4, A5, A6, A7, A8, A9) 
Alldiff (B1, B2, B3, B4, B5, B6, B7, B8, B9) 
··· 
Alldiff (A1, B1, C1, D1, E1, F1, G1, H1, I1)
Alldiff (A2, B2, C2, D2, E2, F2, G2, H2, I2)
···
Alldiff (A1, A2, A3, B1, B2, B3, C1, C2, C3) 
Alldiff (A4, A5, A6, B4, B5, B6, C4, C5, C6)
··· 

## 2)
 Supongamos que tenemos la siguiente asignación parcial, {WA=red, V=blue} 
Tenemos en cuenta que el uso del algoritmo AC-3 tiene una cola con todos los valores cuyos dominios fueron modificados al aplicar el arco consistencia de la asignación parcial anterior.
Los dominios de los valores de la cola serían, NT = { blue, green }, SA = { green }, NSW = { red, green }.
Luego, si aplicamos arco consistencia al desencolar eventualmente SA, nos damos cuenta, al aplicar el algoritmo de borrado, nos quedamos sin valor posible en el dominio para SA, por lo tanto, la inconsistencia es detectada y nos volvemos hacia atrás buscando otro camino de solución posible.

## 3)

En un grafo que tenga una estructura de árbol, los arcos solo se van a considerar como máximo una sola vez, lo que lleva a que la complejidad del algoritmo AC-3 en este caso es de O(A*D) donde A, es el número de Aristas y D es el tamaño del dominio más largo.

## 4)
La idea básica es preprocesar las restricciones de modo que, para cada valor de Xi, hagamos un seguimiento de las variables Xk para las que un arco de Xk a Xi se satisface con ese valor particular de Xi. Esta estructura de datos se puede calcular en el tiempo proporcional al tamaño de la representación del problema. Luego, cuando se elimina un valor de Xi, reducimos en 1 el recuento de valores permitidos para cada arco (Xk, Xi) registrado bajo ese valor.

## 5)
Teniendo en cuenta que el algoritmo CSP para árboles estructurados  tiene los siguientes pasos:
a) 1. Generamos un árbol con los nodos ordenados de manera tal que el padre de cada nodo en el árbol lo precede en el ordenamiento.

 2. Aplicamos arco consistencia a la inversa en los nodos. lo que elimina valores inconsistentes del dominio

 3. asignamos los valores del dominio a cada nodo. 

 El algoritmo aplicado asegura dos puntos claves a destacar.

Primero, después del paso 2 el PSR es directamente arco-consistente, entonces la asignación de valores en el paso 3 no requiere ninguna vuelta atrás.
Segundo, aplicando la comprobación de consistencia de arco en orden inverso en el paso 2, el algoritmo asegura que cualquier valor suprimido no puede poner en peligro la consistencia de arcos que ya han sido tratados.  

Teniendo en cuenta todo esto, podemos demostrar que el algoritmo implica k-consistencia, como dijimos anteriormente, es arco consistente( 2-consistencia), y si analizamos con detenimiento el grafo, al estar ordenado y que cada nodo sólo tiene un padre por como se ordenó en el paso 1, solo encontramos relaciones padre-hijo, por lo cual, nunca encontraríamos una situación en la cual debamos resolver una mayor consistencia que la arco consistencia, por lo tanto nos da que es k-consistente por la propia naturaleza del árbol.

b) Gracias a la explicación anterior, siempre y cuando el grafo de restricciones sea un árbol, podemos decir que el algoritmo es correcto y k-consistente a través de aplicar la arco consistencia en el mismo algoritmo, por lo tanto es lo demostrado en a es suficiente.


## 6) Graficos de cajas
