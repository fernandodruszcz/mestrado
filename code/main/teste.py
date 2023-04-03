from config import inicializacao as ini

conn, cur_list = ini.inicializa(3)

ini.finaliza(conn, cur_list)