# Pega o retorno do OpenCitaions da quantidade de citacoes da publicacao e
# salva cru no db para processar depois
# -----------------------------------------------------------------------------

from config import inicializacao as ini
import requests
import json

conn, cur_list = ini.inicializa(1)
cur = cur_list[0]

l_doi = ['10.1109/SEGAH.2014.7067084']
# sql = "SELECT doi FROM publicacoes"
# cur.execute(sql)
# for linha in cur:
#     l_doi.append(linha[0])

sql = """INSERT INTO retornos_raw
         VALUES (%s, %s)"""

for doi in l_doi:
    url = "https://opencitations.net/index/api/v1/citation-count/" + doi
    retorno = requests.get(url=url).json()
    retorno = json.dumps(retorno)
    print(retorno)
    cur.execute(sql, (retorno, doi))
    break

conn.commit()

ini.finaliza(conn, cur_list)
