from glob     import glob
from networkx import read_adjlist
from time     import time
from lib.degreeOneRemoval import degreeOneRemoval
from networkx import *
import math

#
#==============================================================================
#
def experimenta (G):
  print('Antes')
  print (G)
  print (f'Grau max {max (G.degree, key=lambda x: x[1])[1]}')

  #
  # Calculo do r feito no clustering.py
  #

  # Valores padrao
  erro = 0.05
  p = 0.1
  c = 0.5
  delta = 0.1

  D = max (G.degree, key=lambda x: x[1])[1]
  r = math.ceil(
    (c/(erro*erro*p))
    *
    (
    (math.floor(math.log2(D - 1)) + 1)*math.log(1/p) + math.log(1/delta)
    )
  )

  ini = time()
  degreeOneRemoval (G, v1=True)
  fin = time()

  dif = fin - ini

  print (f'Tempo de execucao: {dif*1000:6.3f}') # tempo em milissegundos

  ini = time()
  degreeOneRemoval (G, v1=False)
  fin = time()

  dif2 = fin - ini

  print (f'Tempo de execucao: {dif2*1000:6.3f}') # tempo em milissegundos

  print (f'Diferenca de tempo da V1 para V2: {1000*dif - 1000*dif2}')

  print('Depois')
  print(G)
  print (f'Grau max {max (G.degree, key=lambda x: x[1])[1]}')

  D = max (G.degree, key=lambda x: x[1])[1]
  r2 = math.ceil(
    (c/(erro*erro*p))
    *
    (
    (math.floor(math.log2(D - 1)) + 1)*math.log(1/p) + math.log(1/delta)
    )
  )
  if r != r2:
    print (f'!!!! r mudou de {r} para {r2}')

  

  


#
#==============================================================================
#
def main ():
  # for file in sorted (glob ("grafos/*_2_*.al")):
  # for file in sorted (glob ("grafos/ba_0_2_0.al")):
  for file in sorted (glob ("grafos/pl_grg_*.al")):
    G = read_adjlist (file)
    experimenta (G)

#
#==============================================================================
# INICIO EXECUCAO
#
main()
