import re
from database_connection import DatabaseConnection

class Usuario:
    def __init__(self):
        self.blocked = False
        self.db = DatabaseConnection()
    
    def registrarUsuario(self,datos):
        userid,fullname,address,phone,email,birthdate,ocupation,study_center = datos
        query= """INSERT INTO users (
            identification,full_name,address,phone,email,birthdate,occupation,study_center) 
            VALUES(?,?,?,?,?,?,?,?)"""
        self.db.execute_query(query, (
            userid,
            fullname,
            address,
            phone,
            email,
            birthdate,
            ocupation,
            study_center))
        
    def validar_telefono(self,celular):
        if not celular.isdigit():
            return False
        else:
            return True
        
    def validar_correo(self,correo):
        regex = r".*@.*"
        if not re.fullmatch(regex,correo):
            return False
        else:
            return True
    
