import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing
from sklearn import linear_model

from sklearn.linear_model import RidgeCV

#=#====================#=#=====================================================================================================#=#
#=# INICIO DO PROGRAMA #=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#

dataFrame = pd.read_csv("ks-projects-201801-preprocessed-complete2.csv")
dataFrame.dropna(inplace = True)
dataFrame.drop(['usd pledged'], axis = 1)
# Aqui é deletado todos as linhas de 40000 até o final da tabela, sendo isso feito pois com o número original
# havia um erro de memória devida ao número muito grande de elementos
#dataFrame = dataFrame.drop(range(200001, len(dataFrame)))

print(dataFrame)

# x e y são duas variáveis são convensões para o nome de duas variáveis que têm o seguinte significado:
#	x é o data frame sem o atributo de saída, ou seja, as entradas 
#	y é o data frame apenas com a saída
x = np.array(dataFrame.drop(['usd_goal_real'], axis = 1)).astype(float)
y = np.array(dataFrame['usd_goal_real'])


# 1ª Tamanho de Teste #-------------------------------------------------------------------------------------------------#
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.1, random_state = 2)

print("\n\nTamanho de teste 0.1:")
# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 4)
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)
print("  Random Forest Tree:", accuracyTree)

bayes = linear_model.BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
                                   fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
                                   normalize=False, tol=0.001, verbose=False)
bayes.fit(xTrain, yTrain)
accuracyBayes = bayes.score(xTest, yTest)
print("  Bayes Ridge Regression:", accuracyBayes)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("  K-Nearest Neighbors:", AcuraciaVizinhos)
#---------------------#-------------------------------------------------------------------------------------------------#


# 2ª Tamanho de Teste #-------------------------------------------------------------------------------------------------#
print("\n\nTamanho de teste 0.2:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state = 2)

decisionTree = RandomForestRegressor(random_state = 4) 
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)
print("  Random Forest Tree:", accuracyTree)

bayes = linear_model.BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
                                   fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
                                   normalize=False, tol=0.001, verbose=False)
bayes.fit(xTrain, yTrain)
accuracyBayes = bayes.score(xTest, yTest)
print("  Bayes Ridge Regression:", accuracyBayes)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("  K-Nearest Neighbors:", AcuraciaVizinhos)
#---------------------#-------------------------------------------------------------------------------------------------#


# 3ª Tamanho de Teste #-------------------------------------------------------------------------------------------------#
print("\n\nTamanho de teste 0.3:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state = 2)

decisionTree = RandomForestRegressor(random_state = 4) 
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)
print("  Random Forest Tree:", accuracyTree)

bayes = linear_model.BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
                                   fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
                                   normalize=False, tol=0.001, verbose=False)
bayes.fit(xTrain, yTrain)
accuracyBayes = bayes.score(xTest, yTest)
print("  Bayes Ridge Regression:", accuracyBayes)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("  K-Nearest Neighbors:", AcuraciaVizinhos)
#---------------------#-------------------------------------------------------------------------------------------------#


# 4ª Tamanho de Teste #-------------------------------------------------------------------------------------------------#
print("\n\nTamanho de teste 0.4:")
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.4, random_state = 2)

decisionTree = RandomForestRegressor(random_state = 4) 
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)
print("  Random Forest Tree:", accuracyTree)

bayes = linear_model.BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
                                   fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
                                   normalize=False, tol=0.001, verbose=False)
bayes.fit(xTrain, yTrain)
accuracyBayes = bayes.score(xTest, yTest)
print("  Bayes Ridge Regression:", accuracyBayes)

knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("  K-Nearest Neighbors:", AcuraciaVizinhos)
#---------------------#-------------------------------------------------------------------------------------------------#

#=#====================#=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#