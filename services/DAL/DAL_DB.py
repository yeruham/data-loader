import mysql.connector
from contextlib import closing


class DAL_DB:

    def __init__(self, host, port, user, password, database, table):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table



    def select(self, condition = ""):

        db_conn_info = {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "auth_plugin": 'mysql_native_password'
        }


        query = f"SELECT * FROM {self.table} {condition}"
        with closing(mysql.connector.connect(**db_conn_info)) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result


