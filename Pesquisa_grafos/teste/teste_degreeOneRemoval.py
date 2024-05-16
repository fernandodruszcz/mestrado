from networkx import *

def degreeOneRemoval (G):
    Q = []
    for n in G:
        if degree(G, n) <= 1:
            Q.append(n)

    while len(Q) > 0:
        n = Q.pop()
        try:
            a = list (neighbors(G, n))[0] # unico vizinho
        except:
            pass
        G.remove_node(n)
        try:
            if degree(G, a) == 1:
                Q.append(a)
        except:
            pass


G = balanced_tree (3, 3)
print (G.edges)
degreeOneRemoval (G)
print (G.edges)