from networkx    import *
from collections import deque

#
#==============================================================================
#
def degreeOneRemoval_v1 (G):
  removed = True
  while removed:
    removed = False
    nodes = list(G)
    for v in nodes:
      if degree (G, v) <= 1:
        G.remove_node(v)
        removed = True


#
#==============================================================================
#
def degreeOneRemoval_v2 (G):
  # Q = []
  # for v in G:
  #   if degree(G, v) <= 1:
  #     Q.append(v)

  # while len(Q) > 0:
  #   v = Q.pop()
  #   try:
  #     a = list (neighbors(G, v))[0] # unico vizinho
  #   except:
  #     pass
  #   G.remove_node(v)
  #   try:
  #     if degree(G, a) == 1:
  #       Q.append(a)
  #   except:
  #     pass

  #
  # Versao usando o "deque" eh um pouco mais rapida que usando lista
  #

  Q = deque()
  for v in G:
    if degree(G, v) <= 1:
      Q.append(v)

  while (len(Q) > 0):
    v = Q.popleft()
    try:
      a = list (neighbors(G, v))[0] # unico vizinho
    except:
      pass
    try:
      G.remove_node(v)
    except:
      pass
    try:
      if degree(G, a) == 1:
        Q.append(a)
    except:
      pass

#
#==============================================================================
#
def degreeOneRemoval (G, **kwargs):
  v1 = kwargs.get('v1', False)
  if v1:
    degreeOneRemoval_v1 (G)
  else:
    degreeOneRemoval_v2 (G)