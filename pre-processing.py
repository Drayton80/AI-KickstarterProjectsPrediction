import pandas as pd
import numpy  as np

# FUNÇÕES IMPORTADAS #==========================================================================================================#
'''
' Função criada por Douglas de Lira Lima (douglasliralima) em conjunto com Armando Neto (ArmandoTGT)
'''
def atributoNeutro(df):
	new_df = pd.DataFrame(df)
	#print(new_df['LvL Adjustment'].tail())
	for atributo in new_df:
		print(atributo)
		i = 0		
		if(atributo == 'state'):
			aux = new_df[atributo].tolist() 
			for elemento in aux:
				print(i,elemento)
				if(elemento == "suspended"):
					new_df.drop(i, inplace = True)				
						
				if(elemento == "undefined"):
					new_df.drop(i, inplace = True)				
						
				if(elemento == "canceled"):
					new_df.drop(i, inplace = True)	

				if(elemento == "failed"):
					new_df.drop(i, inplace = True)	

				if(elemento == "live"):
					new_df.drop(i, inplace = True)			
				i+=1			
	#print(new_df['LvL Adjustment'].tail())
	return new_df

#====================#==========================================================================================================#

# DEFINIÇÂO DAS FUNÇÕES INTERNAS #==============================================================================================#
'''
' Função Convert to Days:
'   Descrição: Recebe uma data no formato ano-mês-dia e retorna ela num formato apenas em número de dias, contando
'    apenas os anos DC, ou seja, começando sempre com o ano 1 como primeiro de todos
'''
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


def deleteNoise(df):
	new_df = pd.DataFrame(df)
	#print(new_df['LvL Adjustment'].tail())
	for atributo in new_df:
		print(atributo)
		i = 0		
		if(atributo == 'usd pledged'):
			aux = new_df[atributo].tolist() 
			for elemento in aux:
				print(i,elemento)
				if(elemento == 0.0):
					new_df.drop(i, inplace = True)				
			
				i+=1			
	#print(new_df['LvL Adjustment'].tail())
	return new_df

#=======================#========================================================================================================#

#=#====================#=#=====================================================================================================#=#
#=# INICIO DO PROGRAMA #=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#

dataFrame = pd.read_csv("ks-projects-201801-preprocessed-complete.csv")

'''
print(len(dataFrame))
dataFrame = atributoNeutro(dataFrame)
dataFrame.to_csv("ks-projects-201801-preprocessed-incomplete2")
print(len(dataFrame))
'''

dataFrame = deleteNoise(dataFrame)

# dataFrame = dataFrame[[ 'main_category', 'currency', 'deadline', 'launched', 'country', 'usd pledged', 'usd_goal_real']]

initialDay = []	# No formato de data ano-mês-dia
finalDay = []	# No formato de data ano-mês-dia
duration = []	# No formato convertido para dias
dictionary = []

#print(dataFrame.tail())

'''
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
'''

print(dataFrame)

# Cria um atributo para cada gênero que existe para poder transformá-los de classe para número, já que é um
# problema de regressão e precisa apenas de número

dataFrameAuxiliary = pd.DataFrame(index = dataFrame.index)

for column, columnData in dataFrame.iteritems():   
    if columnData.dtype == object:
    	# Faz o 0 e 1 direitinho:
        columnData = pd.get_dummies(columnData, prefix = column)
        
    dataFrameAuxiliary = dataFrameAuxiliary.join(columnData)
    
dataFrame = dataFrameAuxiliary

dataFrame.to_csv("ks-projects-201801-preprocessed-complete")

#=#====================#=#=#===================================================================================================#=#=#
#=#====================#=#=====================================================================================================#=#
