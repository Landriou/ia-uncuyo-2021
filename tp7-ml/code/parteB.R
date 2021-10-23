# For manipulating the datasets
library(dplyr)
library(readr)
# For plotting correlation matrix
library(ggcorrplot)
# Machine Learning library
library(caret)
library(rpart)
library(randomForest)
#1
arbolado <- read_csv("../data/arbolado-mza-dataset.csv")
trainset <- arbolado



trainIndex <- createDataPartition(as.factor(trainset$inclinacion_peligrosa), p=0.80, list=FALSE)
data_train <- trainset[ trainIndex,]
data_test <-  trainset[-trainIndex,]

indexes <- which(data_train$inclinacion_peligrosa == 0)
eliminatedData <- sample(indexes, length(indexes) - 2864)
# equlibrate the majority class 
new_data_train <- data_train[-eliminatedData,]
# add circ cat to predict for a nominal value instead of a numeric value
data_train_with_circ_cat <- new_data_train %>% mutate(circ_tronco_cm_cat = ifelse(`circ_tronco_cm` <= 50,'bajo',
                                                                            ifelse(`circ_tronco_cm` > 50 & `circ_tronco_cm` <= 100, 'medio',
                                                                                   ifelse(`circ_tronco_cm` > 100 & `circ_tronco_cm` <= 150, 'alto','muy alto'))))

data_test_with_circ_cat <-  data_test %>% mutate(circ_tronco_cm_cat = ifelse(`circ_tronco_cm` <= 50,'bajo',
                                                                                  ifelse(`circ_tronco_cm` > 50 & `circ_tronco_cm` <= 100, 'medio',
                                                                                         ifelse(`circ_tronco_cm` > 100 & `circ_tronco_cm` <= 150, 'alto','muy alto'))))

#eliminate the non important values
data_filtered <- subset(data_train_with_circ_cat, select = -c(ultima_modificacion, long, lat,circ_tronco_cm ,area_seccion, nombre_seccion, seccion))
data_test_filtered <- subset(data_test_with_circ_cat, select = -c(ultima_modificacion, long, lat,circ_tronco_cm ,area_seccion, nombre_seccion, seccion))



train_formula<-formula(inclinacion_peligrosa~altura+
                         especie+
                         diametro_tronco
)

# generamos el modelo 
tree_model<-rpart(train_formula,data=data_train)
tree_model
# obtenemos la predicción
p<-predict(tree_model,data_test,type='class') 




#randon forest
rfmodel <- randomForest(inclinacion_peligrosa~altura+
                                   circ_tronco_cm_cat+
                                   especie+
                                   diametro_tronco , data = data_filtered)


rfmodel
data_filtered
data_test_filtered

predictions<-predict(rfmodel,data_test_filtered,type='class')
predictions
caret::confusionMatrix(predictions,data_test_filtered$inclinacion_peligrosa)



#caret


ctrl_fast <- trainControl(method="cv", 
                          number=4, 
                          verboseIter=T,
                          classProbs=F,
                          allowParallel = TRUE)  
train_formula<-formula(inclinacion_peligrosa~altura+
                         circ_tronco_cm_cat+
                         especie+
                         diametro_tronco
)

model_caret<- train(train_formula,
                    data = data_filtered,
                    method = "rf",
                    trControl = ctrl_fast)


preds <- predict(model_caret,data_test_filtered)
confusionMatrix(preds,as.factor(data_test_filtered$inclinacion_peligrosa))


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


sensitivity1 <- truePositivesNumber / (truePositivesNumber + falseNegativesNumber)
specificity1 <- trueNegativesNumber / (trueNegativesNumber + falsePositivesNumber)
precision1 <- truePositivesNumber / (truePositivesNumber + falsePositivesNumber)
accuracy1 <- (truePositivesNumber + trueNegativesNumber ) / ( truePositivesNumber + trueNegativesNumber +falsePositivesNumber + falseNegativesNumber)

sensitivity1
specificity1
precision1
accuracy1



