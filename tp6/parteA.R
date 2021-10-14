# For manipulating the datasets
library(dplyr)
library(readr)
# For plotting correlation matrix
library(ggcorrplot)
# Machine Learning library
library(caret)


#1
arbolado <- read_csv("data/arbolado-mza-dataset.csv")
trainset <- arbolado
trainIndex <- createDataPartition(as.factor(trainset$inclinacion_peligrosa), p=0.80, list=FALSE)
data_train <- trainset[ trainIndex,]
data_test <-  trainset[-trainIndex,]

write.csv(data_train,"arbolado-publico-mendoza-2021-train.csv")
write.csv(data_test,"arbolado-publico-mendoza-2021-validation.csv")

#2.a
distri <- data_train %>% group_by(inclinacion_peligrosa) %>% summarise(n=n())
#ggplot(distri, aes(inclinacion_peligrosa, n)) +  geom_bar(stat="identity")

#2.b
seccion_mas_dangerous <- data_train %>% filter(inclinacion_peligrosa == 1) %>% group_by(nombre_seccion) %>% summarise(n=n())
#ggplot(seccion_mas_dangerous, aes(nombre_seccion, n)) + geom_bar(stat="identity")

#2.c
especie_mas_dangerous <- data_train %>% filter(inclinacion_peligrosa == 1) %>% group_by(especie) %>% summarise(n=n())
#ggplot(especie_mas_dangerous, aes(especie, n)) + geom_bar(stat="identity")


#3.b

#ggplot(data = data_train, aes(x = circ_tronco_cm)) + geom_histogram(bins=10)

#3.c

circ_con_filter <-  data_train %>% filter(inclinacion_peligrosa == 1)
#ggplot(data = circ_con_filter, aes(x = circ_tronco_cm)) + geom_histogram(bins=10)

#3.d
data_train_with_circ_cat <- data_train %>% mutate(circ_tronco_cm_cat = ifelse(`circ_tronco_cm` <= 50,'bajo',
                                                                       ifelse(`circ_tronco_cm` > 50 & `circ_tronco_cm` <= 100, 'medio',
                                                                       ifelse(`circ_tronco_cm` > 100 & `circ_tronco_cm` <= 150, 'alto','muy alto'))))
#write.csv(data_train_with_circ_cat,"arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv")

#4.a

add_prediction_probs <- function(dataframe) {
  number_of_rows <- nrow(dataframe)
  array_with_prediction_probs <- runif(number_of_rows, 0, 1) 
  dataframe$prediction_prob <- array_with_prediction_probs
  return(dataframe)
}

prediction_probs_dataframe <- add_prediction_probs(data_train_with_circ_cat)
#4.b
random_classifier <- function(dataframe) {
  dataframe <-dataframe %>% mutate(prediction_class = ifelse(`prediction_prob` >= 0.5, 1 ,0))
  return(dataframe)
}

randomclasifierdataset <- random_classifier(prediction_probs_dataframe)
#4.c
arbolado_validation <- read_csv("arbolado-publico-mendoza-2021-validation.csv")
validation_with_probs <- add_prediction_probs(arbolado_validation)
validation_with_clasiffiers <- random_classifier(validation_with_probs)



truePositive <- validation_with_clasiffiers %>% filter(inclinacion_peligrosa == 1 & prediction_class == 1)
trueNegative <- validation_with_clasiffiers %>% filter(inclinacion_peligrosa == 0 & prediction_class == 0)
falsePositive <- validation_with_clasiffiers %>% filter(inclinacion_peligrosa == 0 & prediction_class == 1)
falseNegative <- validation_with_clasiffiers %>% filter(inclinacion_peligrosa == 1 & prediction_class == 0)

truePositivesNumber <- nrow(truePositive)
trueNegativesNumber <- nrow(trueNegative)
falsePositivesNumber <- nrow(falsePositive)
falseNegativesNumber <- nrow(falseNegative)
truePositivesNumber
trueNegativesNumber
falsePositivesNumber
falseNegativesNumber

#5
biggerclass_classifier <- function(dataframe) {
  dataframe <-dataframe %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
  return(dataframe)
}

majorityClassCount <- treesDataset 