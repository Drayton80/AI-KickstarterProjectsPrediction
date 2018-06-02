import pandas as pandaObj
import numpy  as numpyObj

dataFrame = pandaObj.read_csv("ks-projects-201801.csv")
dataFrame = dataFrame[['category', 'main_category', 'deadline', 'launched', 'state', 'country', 'usd_pledged_real', 'usd_goal_real']]

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

dataFrame = dataFrame.drop(['deadline', 'launched'], axis = 1)
dataFrame['duration'] = duration

print(dataFrame)





