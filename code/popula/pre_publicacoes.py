# Pega o retorno do DBLP das publicacoes dos autores e salva cru no db para
# processar depois
# -----------------------------------------------------------------------------

from config import inicializacao as ini
import requests
import json

conn, cur_list = ini.inicializa(1)
cur = cur_list[0]

l_id_pesquisadores = []
sql = "SELECT id_dblp FROM pesquisadores"
cur.execute (sql)
for linha in cur:
    l_id_pesquisadores.append(linha[0])

sql = """INSERT INTO retornos_raw
         VALUES (%s, %s)"""

for id_pesquisador in l_id_pesquisadores:
    url = "https://dblp.org/pid/" + id_pesquisador + '.xml'
    retorno = requests.get (url=url)
    cur.execute (sql, (retorno.content, 'DBLP'))
    conn.commit()

conn.commit()

ini.finaliza(conn, cur_list)
