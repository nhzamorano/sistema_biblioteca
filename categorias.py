from database_connection import DatabaseConnection

class Categoria:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def registrar_categoria(self,cat):
        query= """INSERT INTO categories (name) VALUES(?)"""
        self.db.execute_query(query, (cat,))

    def mostrar_categorias(self):
        query = "SELECT * FROM categories"
        categorias = self.db.execute_query(query)
        return categorias