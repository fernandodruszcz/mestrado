import networkx as nx
import numpy    as np
import math
from random import choice

#
#==============================================================================
#
def clustering_exato (G):
  print ('Calculando EXATO')

  l = np.zeros((G.number_of_nodes(), ), dtype=float)
  clustering = nx.clustering (G)

  for i in G:
    l[int(i)] = clustering [i]

  return l

#
#==============================================================================
# Faz o calculo aproximado do coeficiente de clustering, baseado no artigo
#
def clustering_aprox (G, **kwargs):
  # Parametros
  erro  = kwargs.get('erro', 0.05)
  delta = kwargs.get('delta', 0.1)
  p     = kwargs.get('p', 0.1)
  c     = kwargs.get('c', 0.5) # (c linha) usar 0.5 ou 1?

  # Parametros devem estar entre 0 e 1
  if ((erro  < 0) or (erro  > 1)
  or  (delta < 0) or (delta > 1)
  or  (p     < 0) or (p     > 1)
  or  (c     < 0) or (c     > 1)):
    raise Exception ("Parametros invalidos, valores devem estar entre 0 e 1")


  T = np.zeros((G.number_of_nodes(), ), dtype=float)
  l = np.zeros((G.number_of_nodes(), ), dtype=float)
  edges = list (G.edges())

  # Constantes
  m = G.number_of_edges()

  # Pega o grau maximo de G
  D = max (G.degree, key=lambda x: x[1])[1]

  r = math.ceil(
    (c/(erro*erro*p))
    *
    (
    (math.floor(math.log2(D - 1)) + 1)*math.log(1/p) + math.log(1/delta)
    )
  )

  # Passo magico
  for i in range (1, r):
    e = choice (edges) # Escolhe uma aresta {a, b} aleatoriamente
    a = e[0]
    b = e[1]
    Na = G[a] # Vizinhos de a
    Nb = G[b] # Vizinhos de b
    for v in Na:
      if v in Nb:
        # v eh uma string com o nome do noh, e os nohs sao nomeados de 1 a n, ao inves de 0 a (n - 1), por isso para acessar fazemos int(v) - 1
        T[int(v) - 1] += m/r

  # Passo magico 2 que calcula o clustering coefficient
  for v in G:
    if G.degree(v)*(G.degree(v) - 1) == 0:
      l[int(v)] = 0
    else:
      l[int(v)] = 2*T[int(v) - 1]/(G.degree(v)*(G.degree(v) - 1))

  return l

#
#==============================================================================
#
def clustering (G, **kwargs):
  # Por padrao vamos calcular o clustering exato
  exato = kwargs.get ('exato', True)

  if exato:
    return clustering_exato (G)
  else:
    return clustering_aprox (G, **kwargs)