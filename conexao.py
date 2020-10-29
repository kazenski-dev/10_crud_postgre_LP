import psycopg2

class Conexao():
    def get_connection(self):
        conexao = psycopg2.connect(user="postgres",password="8pcapdoe6gdd", host="127.0.0.1", port="5432", database="pessoa_lp")
        return conexao