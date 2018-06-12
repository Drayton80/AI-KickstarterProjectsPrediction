import pandas as pd
import numpy  as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing

#=#====================#=#=====================================================================================================#=#
#=# INICIO DO PROGRAMA #=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#

dataFrame = pd.read_csv("ks-projects-dataset-altered.csv")
dataFrame = dataFrame[[ 'main_category', 'deadline', 'launched', 'country', 'usd_goal_real', 'usd_pledged_real']]
# Aqui é deletado todos as linhas de 40000 até o final da tabela, sendo isso feito pois com o número original
# havia um erro de memória devida ao número muito grande de elementos
#dataFrame = dataFrame.drop(range(200001, len(dataFrame)))

# x e y são duas variáveis são convensões para o nome de duas variáveis que têm o seguinte significado:
#	x é o data frame sem o atributo de saída, ou seja, as entradas 
#	y é o data frame apenas com a saída
x = np.array(dataFrame.drop(['usd_goal_real'], axis = 1)).astype(float)
y = np.array(dataFrame['usd_goal_real'])

# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.5, random_state = 2)


# Rodando todos os métodos de Machine learning:
decisionTree = RandomForestRegressor(random_state = 3) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\n\nRandom Forest Tree:", accuracyTree)

decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
decisionTree.fit(xTrain, yTrain)
accuracyTree = decisionTree.score(xTest, yTest)

print("\n\nDecision Tree:", accuracyTree)
'''
knn = KNeighborsRegressor()
knn.fit(xTrain, yTrain)
AcuraciaVizinhos = knn.score(xTest, yTest)
print("\n\nK-Nearest Neighbors:", AcuraciaVizinhos)
'''
#=#====================#=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#