from database_connection import DatabaseConnection

class Articulo:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def registrar_articulo(self,catalogo):
        titulo,autor,year,editorial,isbn,palabras_clave,idCategoria = catalogo 
        query= """INSERT INTO articles (
            title,author,year_publication,publisher,isbn_issn,keywords,categorie_id) 
            VALUES(?,?,?,?,?,?,?)"""
        self.db.execute_query(query, (
            titulo,
            autor,
            year,
            editorial,
            isbn,
            palabras_clave,
            idCategoria))

    def mostrar_articulos(self):
        query = "SELECT id,title FROM articles"
        articles = self.db.execute_query(query)
        return articles