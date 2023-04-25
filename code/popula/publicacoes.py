# Importa da data/all-researchers.csv:
#   o nome, instituicao de ensino e id no dblp dos pesquisadores
# -----------------------------------------------------------------------------

from config import inicializacao as ini
from xml.etree import ElementTree

conn, cur_list = ini.inicializa(1)
cur = cur_list[0]

sql = "SELECT FROM retornos_raw WHERE source = 'DBLP"


conn.commit()

ini.finaliza(conn, cur_list)
