import pandas as pd
import numpy  as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

def atributoNeutro(df):
	#Lembrando que ao recebermos um dicionário no for, ele vai printando suas palavras chave, então basta que
	#a cada palavra chave no for, nós percorramos toda a linha
	new_df = pd.DataFrame(df)
	#print(new_df['LvL Adjustment'].tail())
	for atributo in new_df:
		#print(atributo)
		i = 0		
		if(atributo == 'state'):
		#Vamos percorrer essa lista
			aux = new_df[atributo].tolist() #Nos temos Series em nossas palavras chaves, elas são como listas, só que com outros metodos
			for elemento in aux:
				print(i,elemento)
				if(elemento == "failed"):
					new_df.drop(i, inplace = True)				
					#Como todos os elementos são strings que serão convertidas para inteiros, colocamos ele como string tbm	
				if(elemento == "canceled"):
					new_df.drop(i, inplace = True)				
					#Como todos os elementos são strings que serão convertidas para inteiros, colocamos ele como string tbm				
				i+=1			
	#print(new_df['LvL Adjustment'].tail())
	return new_df


dataFrame = pd.read_csv("ks-projects-201801.csv")
dataFrame = dataFrame[[ 'main_category', 'deadline', 'launched', 'state', 'country', 'usd_pledged_real', 'usd_goal_real']]
print(len(dataFrame))
dataFrame = atributoNeutro(dataFrame)
print(len(dataFrame))
# Aqui é deletado todos as linhas de 40000 até o final da tabela, sendo isso feito pois com o número original
# havia um erro de memória devida ao número muito grande de elementos
dataFrame = dataFrame.drop(range(200001, len(dataFrame)))

# DEFINIÇÂO DAS FUNÇÕES #==========================================================================================================#

def convertToDays(date):
	#|print("Ano:", int(date[0:4]))
	# Soma-se os dias de todos os anos anteriores [ ( int(date[0:4])-1 )*365 ], contando com à soma dos dias à 
	# mais advindos dos anos bissextos anteriores [ int( (int(date[0:4])-1)/4) ], até chegar no ano da data e 
	# verificar quantos dias em específico ele têm indo para os meses e, por fim, os dias
	days = 0 + ( int(date[0:4])-1 )*365 + int( (int(date[0:4])-1)/4)

	#|print("Dias após anos:", days)

	# Se for maior que o mês significa que o número de dias do respectivo mês deve ser
	# acrescentado na conta dos dias, ou seja, a cada mês passado seu número de dias deve ser
	# incrementado na contagem de dias até que chegue no mês que o atributo da data está para só assim
	# poder passar para a parte dos dias e somá-los na conta
	# somar com os dos meses posteriores
	#|print("Mês:", int(date[5:7]) )
	if 1 < int(date[5:7]):
		days += 31
	if 2 < int(date[5:7]):
		# Se o ano for bissexto Fevereiro terá 29 dias
		if (int(date[0:4])%4) == 0:
			days += 29
		else:
			days += 28
	if 3 < int(date[5:7]):
		days += 31
	if 4 < int(date[5:7]):
		days += 30
	if 5 < int(date[5:7]):
		days += 31
	if 6 < int(date[5:7]):
		days += 30
	if 7 < int(date[5:7]):
		days += 31
	if 8 < int(date[5:7]):
		days += 31
	if 9 < int(date[5:7]):
		days += 30
	if 10 < int(date[5:7]):
		days += 31
	if 11 < int(date[5:7]):
		days += 30
	
	#|print("Dias após meses:", days)

	#|print("Dia: ", int(date[8:10]))
	# Por fim, soma-se os dias da data aos dias totais:
	days += int(date[8:10])

	#|print("Dias após dias", days)

	return days

#=======================#==========================================================================================================#

initialDay = []	# No formato de data ano-mês-dia
finalDay = []	# No formato de data ano-mês-dia
duration = []	# No formato convertido para dias
dictionary = []

#print(dataFrame.tail())

counter = 0
for dateBegin in dataFrame['launched']:
	initialDay.append(convertToDays(dateBegin))
	counter += 1

counter = 0
for dateEnd in dataFrame['deadline']:
	finalDay.append(convertToDays(dateEnd))
	
	# A duração dos dias é igual a diferença entre o dia final e o inicial
	duration.append(finalDay[counter] - initialDay[counter])

	counter += 1

dataFrame = dataFrame.drop(['deadline', 'launched'], 1)
dataFrame['duration'] = duration

#print(dataFrame)

# Cria um atributo para cada gênero que existe para poder transformá-los de classe para número, já que é um
# problema de regressão e precisa apenas de número
dataFrameAuxiliary = pd.DataFrame(index = dataFrame.index)

for column, columnData in dataFrame.iteritems():   
    if columnData.dtype == object:
    	# Faz o 0 e 1 direitinho:
        columnData = pd.get_dummies(columnData, prefix = column)
        
    dataFrameAuxiliary = dataFrameAuxiliary.join(columnData)
    
dataFrame = dataFrameAuxiliary

# x e y são duas variáveis são convensões para o nome de duas variáveis que têm o seguinte significado:
#	x é o data frame sem o atributo de saída, ou seja, as entradas 
#	y é o data frame apenas com a saída
x = np.array(dataFrame.drop(['duration'], 1))
y = np.array(dataFrame['duration'])
# train_test_split é o nosso treinamento dos sets (o split funciona como o cross validation, o cross validation
# em si foi decreptado) 0.2 significa que tá dividindo em 5 folds (se fosse dividir em 10 seria 0.1)
# Cria tbm o x e y de teste e de treino
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.7, random_state = 2)

# Rodando todos os métodos de Machine learning:
decisionTree = DecisionTreeRegressor(random_state = 4) # Mudar outrs parametros é aqui dentro
# Para treinar
decisionTree.fit(xTrain, yTrain)
# Para testar
accuracyTree = decisionTree.score(xTest, yTest)

print("\n\nAcuracia da Arvore de decisão:", accuracyTree)

vizinhos = KNeighborsRegressor()
vizinhos.fit(xTrain, yTrain)
AcuraciaVizinhos = vizinhos.score(xTest, yTest)
print("\n\nAcuracia do método de vízinhos próximos:", AcuraciaVizinhos)


