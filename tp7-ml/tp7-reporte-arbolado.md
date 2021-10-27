# Procedimiento
Para para poder completar el desafio en kaggle, lo que hice fue en principio, comparar las clases mayoritarias del archivo de train.
Vi que la cantidad estaba muy despareja con respecto a los arboles no peligrosos, asique decidi cortar aleatoriamente la cantidad de arboles no peligrosos hasta llegar a un numero cercano a los peligrosos.
Luego, como en la parte A, cambie el valor diametro tronco a un valor nominal exactamente como en la parte A.
Despues saque las columnas que no interesaban y ensuciaban el modelo, dejando solo 
    altura
    especie
    diametro_tronco
    circ_tronco_cm_cat

Y por ultimo elimine al arbol del cielo porque me rompia todo el codigo en los datasets


# Resultados obtenidos en el conjunto de validacion

# Resultado de Kaggle

# Descripcion detalla del algoritmo propuesto
Ademas de lo que puse en el procedimiento, decidi usar arboles de decision, porque randomForest y Knn me funcionaban de forma rara y no me convencian, y ademas del algoritmo usado y el procedimiento dicho anteriormente no hay mucho mas que detallar.