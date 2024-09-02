from database_connection import DatabaseConnection

class Prestamo:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def registrar_prestamo(self,prestamo):
        idUsuario,idLibro,fecha_prestamo,fecha_devolucion,tipo_prestamo = prestamo
        query= """INSERT INTO loans (
            user_id,book_id,loan_date,estimated_return_date,actual_return_date,loan_type) 
            VALUES(?,?,?,?,?,?)"""
        prest=self.db.execute_query(query, (
            idUsuario,
            idLibro,
            fecha_prestamo,
            fecha_devolucion,
            fecha_devolucion,
            tipo_prestamo))
        if prest:
            return True 
        
        