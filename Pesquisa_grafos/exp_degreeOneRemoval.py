from glob     import glob
from networkx import read_adjlist
from time     import time
from lib.degreeOneRemoval import degreeOneRemoval
from networkx import *
import math

#
#==============================================================================
#
def experimenta (v1, file):
  ver_alg = '2'
  if v1:
    ver_alg = '1'

  G = read_adjlist (file)

  qtde_nos_ant = G.number_of_nodes()
  grau_max_ant = max (G.degree, key=lambda x: x[1])[1]

  #
  # Calculo do r feito no clustering.py
  #

  # Valores padrao
  erro = 0.05
  p = 0.1
  c = 0.5
  delta = 0.1

  r_ant = math.ceil(
    (c/(erro*erro*p))
    *
    (
    (math.floor(math.log2(grau_max_ant - 1)) + 1)*math.log(1/p) + math.log(1/delta)
    )
  )

  for i in range (5):
    G = read_adjlist (file)
    ini = time()
    degreeOneRemoval (G, v1=v1)
    fin = time()
    dif = fin - ini

    qtde_nos_dps = G.number_of_nodes()
    grau_max_dps = max (G.degree, key=lambda x: x[1])[1]
    r_dps = math.ceil(
        (c/(erro*erro*p))
        *
        (
        (math.floor(math.log2(grau_max_dps - 1)) + 1)*math.log(1/p) + math.log(1/delta)
        )
      )

    # 'grafo,versao_algoritmo,rodada,tempo_execucao,qtde_nos_ant,qtde_nos_dps,grau_max_ant,grau_max_dps,r_ant,r_dps'
    print(f'{file[7:]},{ver_alg},{i},{dif*1000},{qtde_nos_ant},{qtde_nos_dps},{grau_max_ant},{grau_max_dps},{r_ant},{r_dps}')

#
#==============================================================================
#
def main ():
  print(f'grafo,versao_algoritmo,rodada,tempo_execucao,qtde_nos_ant,qtde_nos_dps,grau_max_ant,grau_max_dps,r_ant,r_dps')
  # for file in sorted (glob ("grafos/*_2_*.al")):
  # for file in sorted (glob ("grafos/ba_0_2_0.al")):
  v1 = True
  for file in sorted (glob ("grafos/pl_grg_*.al")):
    experimenta (v1, file)

  v1 = False
  for file in sorted (glob ("grafos/pl_grg_*.al")):
    experimenta (v1, file)

#
#==============================================================================
# INICIO EXECUCAO
#
main()
