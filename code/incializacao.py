import psycopg2 as ps
from .config import config


def inicializa(n_cur):
  conn = ps.connect(**config())

  cur_list = []
  for i in range(n_cur):
    cur = conn.cursor()
    cur_list.append(cur)

  return (conn, cur_list)

def finaliza(conn, cur_list):
  for i in cur_list:
    i.close()

  conn.close()
