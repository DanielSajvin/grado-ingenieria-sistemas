library(tidyverse)
library(caret)
library(neuralnet)

# cargar datos
datos = iris

# separacion en grupo de entrenamiento y pruebas
muestra = createDataPartition(datos$Species, p=0.8, list=F)
train = datos[muestra,]
test = datos[-muestra,]

# analisis exploratorio
head(train, 5)
tail(train, 4)
train[6:10,]
sepal_length = train$Sepal.Length
hist(sepal_length)

# entrenamiento de la red neuronal 
red.neuronal = neuralnet(Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, data=train, hidden=c(2,3))

# visualizar la funcion de activacion
red.neuronal$act.fct

# visualizar la red neuronal 
plot(red.neuronal)

# aplicar la red al conjunto de pruebas para predecir las especies 
prediccion = predict(red.neuronal, test, type='class')

# decodificar la columna que contiene el maximo
# y por ende la especie de la que se trata 
decodificarCol = apply(prediccion, 1, which.max)

# crear columna nueva con los valores decodificados 
codificado = data_frame(decodificarCol)
codificado = mutate(codificado, especie=recode(codificado$decodificarCol, "1"="Setosa", "2"="Versicolor", "3"="Virginica"))
test$Especie.Pred = codificado$especie






