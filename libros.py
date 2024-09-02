from database_connection import DatabaseConnection

class Libro:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def registrar_libro(self,libro):
        article_id,state = libro
        query= """INSERT INTO books (article_id,state) VALUES(?,?)"""
        self.db.execute_query(query, (article_id,state))
    
    def mostrar_libros(self):
        query = """SELECT b.id,a.title,b.state 
                    FROM books b
                    INNER JOIN  articles a
                    ON a.id = b.id 
                    WHERE state = 'Disponible' """
        libros = self.db.execute_query(query)
        if libros:
            return libros
        else: 
            return None
    
    def actualizar_estado_libro(self,id):
        query = "UPDATE books SET state = 'Prestado' WHERE id = ? "
        self.db.execute_query(query, (id,))
