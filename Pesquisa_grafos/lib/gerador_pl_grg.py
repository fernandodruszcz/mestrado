from math     import floor
from networkx import *
from random   import random
#
#==============================================================================
#
def pl_grg (n, **kwargs):
  c = kwargs.get ('c', 2.5)
  #
  # Primeiro montamos o vetor com a sequencia de graus esperado
  #

  # Calcula a
  a = 0
  for k in range (1, n - 1):
    a += pow (k, -1*c)

  fim = False
  lista_graus = []
  grau = 1
  # Vai adicionando ate o resultado ser 0 vertices
  while not fim:
    qtde_vertices = floor (n/(a*pow(grau, c)))
    if qtde_vertices == 1:
      fim = True
    for i in range (qtde_vertices):
      lista_graus.append (grau)
    grau += 1

  #
  # Agora montamos o grafo de fato
  #
  G = Graph()
  for i in range (len (lista_graus)):
    G.add_node (i)

  soma_graus = 0
  for i in lista_graus:
    soma_graus += i

  for i in G:
    for j in G:
      if i != j:
        if random () < lista_graus[i]*lista_graus[j]/soma_graus:
          G.add_edge(i, j)

  return G
