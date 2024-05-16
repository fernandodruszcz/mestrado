# Pra poder chamar as funcoes da pasta lib
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/ferna/Documents/Faculdade/Pesquisa/lib')

from gerador_pl_grg import pl_grg

from networkx       import barabasi_albert_graph, write_adjlist
n = 100
m = 1
n_list = (100, 250, 500, 1000, 2000, 4000, 8000, 16000)
for n in n_list:
  for i in range (0,5):
    # G = barabasi_albert_graph (n, m)
    G = pl_grg (n)
    # write_adjlist (G, f'ba_{n:05}_{m}_{i}.al')
    write_adjlist (G, f'pl_grg_{n:05}_{i}.al')
