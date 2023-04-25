# Importa da data/all-researchers.csv: 
#   o nome, instituicao de ensino e id no dblp dos pesquisadores
# -----------------------------------------------------------------------------

from config import inicializacao as ini
import csv

conn, cur_list = ini.inicializa(1)
cur = cur_list[0]

l_pesquisadores = []
with open('./data/all-researchers.csv') as pesquisadores_raw:
    csv_reader = csv.reader(pesquisadores_raw, delimiter=',')
    for pesquisador in csv_reader:
        l_pesquisadores.append(
            (pesquisador[0], pesquisador[1], pesquisador[2])
          )

sql = """INSERT INTO pesquisadores
         VALUES (%s, %s, %s)"""

for p in l_pesquisadores:
    cur.execute(sql, (p[0], p[1], p[2]))

conn.commit()

ini.finaliza(conn, cur_list)
