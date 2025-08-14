import mysql.connector


class DAL:

    def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table


    def select(self, condition = ""):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            query = f"SELECT * FROM {self.table} {condition}"
            cursor = connection.cursor()
            cursor.execute(query)
            rows_agents = cursor.fetchall()
            return rows_agents


    def insert(self, table_columns,  new_values):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            columns = ", ".join(table_columns)
            values = "', '".join(new_values)
            query = f"INSERT INTO {self.table}({columns}) VALUES('{values}')"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()


    def delete(self, condition= ""):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            query = f"DELETE FROM {self.table} {condition}"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()


    def update(self, update, condition= ""):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            query = f"UPDATE {self.table} SET {update} {condition}"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
