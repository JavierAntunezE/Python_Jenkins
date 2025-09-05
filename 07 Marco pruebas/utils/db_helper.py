import pyodbc

class Database:
    def __init__(self, server="localhost", database="TestLoginDB", username="sa", password="YourPassword123"):
        self.conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        self.cursor = self.conn.cursor()

    def get_user(self, username):
        self.cursor.execute("SELECT Username, Password FROM Users WHERE Username = ?", (username,))
        return self.cursor.fetchone()  # Devuelve una tupla (Username, Password)



    def close(self):
        self.conn.close()
