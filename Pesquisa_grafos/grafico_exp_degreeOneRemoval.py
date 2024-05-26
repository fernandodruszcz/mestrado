import csv
x1 = []
x2 = []
with open('resultados/exp_degreeOneRemoval.csv') as csvfile:
  tam_grafo_ant = ''
  reader = csv.reader(csvfile, delimiter=',')
  next(reader, None) # Pula o header
  for row in reader:
    # print(f'{row}')
    # print(f'{row[0][7:12]}')
    # grafo,versao_algoritmo,rodada,tempo_execucao,qtde_nos_ant,qtde_nos_dps,grau_max_ant,grau_max_dps,r_ant,r_dps
    grafo            = row[0]
    versao_algoritmo = row[1]
    rodada           = row[2]
    tempo_execucao = float (row[3])
    qtde_nos_ant     = row[4]
    qtde_nos_dps     = row[5]
    grau_max_ant     = row[6]
    grau_max_dps     = row[7]
    r_dps            = row[9]
    r_ant            = row[8]

    tam_grafo = row[0][7:12]
    if tam_grafo_ant == '':
      versao_algoritmo_ant = versao_algoritmo 
      tam_grafo_ant = tam_grafo
      count = 0
      soma  = 0

    if tam_grafo_ant != tam_grafo:
      media = soma/count
      # print(f'Grafo {tam_grafo_ant} : {soma}/{count} = {media}')
      count = 0
      soma  = 0
      if versao_algoritmo_ant == '1':
        x1.append(media)
      else:
        x2.append(media)

    count += 1
    soma  += tempo_execucao

    tam_grafo_ant = tam_grafo
    versao_algoritmo_ant = versao_algoritmo

media = soma/count
# print(f'Grafo {tam_grafo_ant} : {soma}/{count} = {media}')
count = 0
soma  = 0
if versao_algoritmo_ant == '1':
  x1.append(media)
else:
  x2.append(media)


import matplotlib.pyplot as plt 
  
y = [100,250,500,1000,2000,4000,8000,16000,32000] 
  
plt.plot(y, x1, label = "v1") 
plt.plot(y, x2, label = "v2") 
plt.legend() 
plt.show()
