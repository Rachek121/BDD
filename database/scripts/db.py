import pytest
import sqlite3

@pytest.fixture(scope="function")
def temp_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create tables for testing
    cursor.execute("CREATE TABLE Orders (id_order INTEGER PRIMARY KEY, type_of_work TEXT, description TEXT, acceptance_date TEXT, customer TEXT, executor TEXT, status TEXT)")
    cursor.execute("CREATE TABLE Works (id_work INTEGER PRIMARY KEY, work TEXT)")
    cursor.execute("CREATE TABLE Employees (id_employee INTEGER PRIMARY KEY, surname TEXT)")
    cursor.execute("CREATE TABLE Statuses (id_status INTEGER PRIMARY KEY, status TEXT)")

    yield conn

class Data:
    _instance = None

    def __new__(cls, conn):
        if cls._instance is None:
            cls._instance = super(Data, cls).__new__(cls)
            cls.data = []
            cls._instance.conn = conn
            cls.connect()
        return cls._instance

    @staticmethod
    def connect():
        Data._instance.cur = Data._instance.conn.cursor()

    def add_order(self, **kwargs):
        try:
            sqlite_insert_query = """
                INSERT INTO Orders (type_of_work, description, acceptance_date, customer, executor, status)
                VALUES (?, ?, ?, ?, ?, ?);
            """
            data = (kwargs['type_of_work'], kwargs['description'], kwargs['acceptance_date'],
                    kwargs['customer'], kwargs['executor'], kwargs['status'])
            self.cur.execute(sqlite_insert_query, data)
            self.conn.commit()
            return "Запись добавлена"
        except sqlite3.Error as e:
            raise Exception(f"Ошибка добавления: {e}")

    def get_all_orders(self, column=None, fltr=None):
        try:
            if column is not None:
                request = f"SELECT * FROM Orders WHERE {column} like ?"
                self.data = self.cur.execute(request, (fltr,)).fetchall()
            else:
                request = f"SELECT * FROM Orders"
                self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = []
        return self.data

    def __del__(self):
        self.conn.close()

    def update_order(self, **kwargs):
        try:
            sqlite_update_query = """
                UPDATE Orders
                SET type_of_work = ?, description = ?, acceptance_date = ?, 
                    customer = ?, executor = ?, status = ?
                WHERE id_order = ?;
            """
            data = (kwargs['type_of_work'], kwargs['description'], kwargs['acceptance_date'],
                    kwargs['customer'], kwargs['executor'], kwargs['status'], kwargs['id_order'])
            self.cur.execute(sqlite_update_query, data)
            self.db.commit()
            return "Запись обновлена"
        except sqlite3.Error as e:
            return f"Ошибка обновления: {e}"

    def delete_order(self, **kwargs):
        try:
            sqlite_delete_query = "DELETE FROM Orders WHERE id_order = ?;"
            data = (kwargs['id_order'],)
            self.cur.execute(sqlite_delete_query, data)
            self.db.commit()
            return "Запись удалена"
        except sqlite3.Error as e:
            return f"Ошибка удаления: {e}"

    def get_work_types(self):
        try:
            request = "SELECT id_work, work FROM Works"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e

    def get_executors(self):
        try:
            request = "SELECT id_employee, surname FROM Employees"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e

    def get_statuses(self):
        try:
            request = "SELECT id_status, status FROM Statuses"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e