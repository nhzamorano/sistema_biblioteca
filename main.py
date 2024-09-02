import os
from usuarios import Usuario
from categorias import Categoria
from articulos import Articulo
from libros import Libro
from prestamos import Prestamo

user = Usuario()
categoria = Categoria()
articulo = Articulo()
libro = Libro()
prestamo = Prestamo()
#user.registrarUsuario()
def pedir_datos_usuario():
    idUsuario = input("Digite numero de cedula del usuario: ")
    nombre = input("Digite el nombre completo del usuario: ")
    direccion = input("Digite la direccion del usuario: ")

    while True:  
        celular = input("Digite el numero celular del usuario: ")
        if user.validar_telefono(celular):
            break
        else:
            print("ERROR!!!: El numero de telefono es inválido")

    while True:
        email = input("Digite el correo electronico del usuario: ")
        if user.validar_correo(email):
            break
        else:
            print("ERROR!!!: El correo electrónico es inválido")

    fecha = input("Digite la fecha de nacimiento del usuario: ")
    ocupacion = input("Digite la ocupacion del usuario: ")
    centro_estudio = input("Digite la institucion donde estudia: ")
    return (idUsuario,nombre,direccion,celular,email,fecha,ocupacion,centro_estudio)

def pedir_datos_categoria():
    nombre = input("Digite el nombre de la categoria: ")
    return nombre

def pedir_datos_catalogo():
    categorias=categoria.mostrar_categorias()
    print("")
    print("Categorias disponibles")
    for cat in categorias:
        print(f"{cat[0]} : {cat[1]}")
    print()    
    titulo = input("Digite el titulo del libro: ")
    autor = input("Digite el autor del libro: ")
    year = input("Digite el año de publicacion (YYYY-MM-DD): ")
    editorial = input("Digite la editorial del libro: ")
    isbn = input("Digite un isbn valido para el libro: ")
    palabras_clave = input("Digite las palabras cleve o keywords: ")
    idCategoria = input("Digite el numero de id de la categoria: ")
    return (titulo,autor,year,editorial,isbn,palabras_clave,idCategoria)

def pedir_datos_libros():
    libros = articulo.mostrar_articulos()
    print()
    print("Catalogo de articulos disponibles")
    for libro in libros:
        print(f"{libro[0]} : {libro[1]}")
    print()
    idLibro = input("Digite el codigo del libro: ")
    estado = input("Digite el estado del libro: ")
    return(idLibro,estado)

def pedir_datos_prestamo():
    """if libros == None:
        print("No hay datos disponibles")
    else:"""
    books = libro.mostrar_libros()
    if books != None:
        print()
        print("Listado de libros disponibles")
        for book in books:
            print(f"{book[0]} : {book[1]}")
        print()
        print("Usuarios ")
        usuarios = user.mostrar_usuarios()        
        for usuario in usuarios:
            print(f"{usuario[0]} : {usuario[1]}")
        print()
    
        idUsuario = input("Digite el numero de cedula del usuario: ")
        idLibro = input("Digite el codigo del libro a prestar: ")
        fecha_prestamo = input("Digite la fecha del prestamo (YYYY-MM-DD): ") 
        fecha_devolucion = input("Digite la fecha de dvolucion (YYYY-MM-DD): ")
        tipo_prestamo = input("Tipo prestamo, < Domiciliario > o < Sala >: ")
        return(idUsuario,idLibro,fecha_prestamo,fecha_devolucion,tipo_prestamo)
    else:
        return False



def menu():
    """Interaccion con el usuario"""
    os.system("cls")
    continuar = True 
    while continuar:
        print("\n\nSeleccione una opcion: ")
        print("    (1) Agregar un usuario")
        print("    (2) Agregar una categoria")
        print("    (3) Agregar un articulo al catalogo")
        print("    (4) Agregar un libro")
        print("    (5) Agregar un prestamo")
        print("    (6) Agregar una multa")
        print("    (7) Agregar una reserva")
        print("    (8) Agregar una notificacion") 
        print("    (9) Salir")

        opcion = int(input('Opcion: '))

        if opcion == 1:
            print("Agregar usuario")
            datos_usuario = pedir_datos_usuario()
            user.registrarUsuario(datos_usuario)
        elif opcion == 2:
            print("Agregar una categoria")
            datos_categoria = pedir_datos_categoria()
            categoria.registrar_categoria(datos_categoria)
        elif opcion == 3:
            print("Agregar un articulo al catalogo")
            catalogo = pedir_datos_catalogo()
            articulo.registrar_articulo(catalogo)
        elif opcion == 4:
            print("Agregar un libro")
            datos_libro = pedir_datos_libros()
            libro.registrar_libro(datos_libro)
        elif opcion == 5:
            print("Agregar prestamo")
            datos_prestamo = pedir_datos_prestamo()
            if datos_prestamo == False:
                print("No hay libros para prestar")
            else:
                prestamo.registrar_prestamo(datos_prestamo)
                if prestamo:
                    libro.actualizar_estado_libro(datos_prestamo[1])
            
        elif opcion == 6:
            print("Agregar una multa")
        elif opcion == 7:
            print("Agregar una reserva")
        elif opcion == 8:
            print("Agregar un notificacion")
        elif opcion == 9:
            print("Salir")
            continuar = False 
            break
        else:
            print("Debe seleccionar una opcion entre 1 y 9")
        input("Presione una tecla para continuar...")
        os.system("cls")

            



        
if __name__ == "__main__":
    menu()

#print(datos)


"""
def test():
    db1.execute_query("INSERT INTO users (
                  identification,full_name,address,phone,email,birthdate,occupation,study_center) 
                  VALUES('16251362','Pedro Herrera','Carrera 10 18A 46','3176289995','pedro@hotmail.com','1969-01-02','Ingeniero','Unilibre'  )")

datos = db1.execute_query("SELECT * FROM users")
for user in datos:
    print(f"ID: {user[1]}, Nombre: {user[2]}, Direccion: {user[3]}, Telefono: {user[4]},E-mail: {user[5]}, Fecha Nacimiento: {user[6]}, Profesion:{user[7]}, Centro de Estudio: {user[8]}")
    print("----------------------------------------------------------------------------------------")
    """