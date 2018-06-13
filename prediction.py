import pandas as pd
import numpy  as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing

from sklearn.linear_model import RidgeCV

#=#====================#=#=====================================================================================================#=#
#=# INICIO DO PROGRAMA #=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#

dataFrame = pd.read_csv("ks-projects-201801-preprocessed-complete2.csv")
dataFrame.dropna(inplace = True)
# Aqui é deletado todos as linhas de 40000 até o final da tabela, sendo isso feito pois com o número original
# havia um erro de memória devida ao número muito grande de elementos
#dataFrame = dataFrame.drop(range(200001, len(dataFrame)))

# x e y são duas variáveis são convensões para o nome de duas variáveis que têm o seguinte significado:
#	x é o data frame sem o atributo de saída, ou seja, as entradas 
#	y é o data frame apenas com a saída
x = np.array(dataFrame.drop(['usd_goal_real'], axis = 1)).astype(float)
y = np.array(dataFrame['usd_goal_real'])


print("\n\n Tamanho de teste 0.1:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.1, random_state = 2)


# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\nRandom Forest Tree:", accuracyTree)

decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)

print("\nDecision Tree:", accuracyTree)

regr_2 = RidgeCV()
regr_2.fit(xTrain, yTrain)
acuracia1 = regr_2.score(xTest, yTest)
print("\nRidgeCV:", acuracia1)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("\nK-Nearest Neighbors:", AcuraciaVizinhos)


print("\n\n Tamanho de teste 0.2:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state = 2)


# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\nRandom Forest Tree:", accuracyTree)

decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)

print("\nDecision Tree:", accuracyTree)

regr_2 = RidgeCV()
regr_2.fit(xTrain, yTrain)
acuracia1 = regr_2.score(xTest, yTest)
print("\nRidgeCV:", acuracia1)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("\nK-Nearest Neighbors:", AcuraciaVizinhos)


print("\n\n Tamanho de teste 0.3:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state = 2)


# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\nRandom Forest Tree:", accuracyTree)

decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)

print("\nDecision Tree:", accuracyTree)

regr_2 = RidgeCV()
regr_2.fit(xTrain, yTrain)
acuracia1 = regr_2.score(xTest, yTest)
print("\nRidgeCV:", acuracia1)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("\nK-Nearest Neighbors:", AcuraciaVizinhos)

print("\n\n Tamanho de teste 0.4:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.4, random_state = 2)


# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\nRandom Forest Tree:", accuracyTree)

decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)

print("\nDecision Tree:", accuracyTree)

regr_2 = RidgeCV()
regr_2.fit(xTrain, yTrain)
acuracia1 = regr_2.score(xTest, yTest)
print("\nRidgeCV:", acuracia1)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("\nK-Nearest Neighbors:", AcuraciaVizinhos)

#=#====================#=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#