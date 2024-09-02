import sqlite3

class Create_db:
    def __init__(self):
        self.conexion = sqlite3.connect('biblioteca.sqlite3')
        self.cursor = self.conexion.cursor()
    
    
    def Crear_Tablas(self):
        resp = input("Desea crear la estructura de la base de datos, se elliminaran todos los datos existentes, <S/N>: ")
        if resp.upper() == 'S':
            print("Creando estructura de la base de datos BIBLIOTECA")
            print()
            print("Creando tabala usuarios ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS users;
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                identification TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                address TEXT,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                birthdate DATE,
                occupation TEXT,
                study_center TEXT,
                blocked TEXT DEFAULT 'False'
                );
            """)
            print()
            print("Creando tabala categorias ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS categories;
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
                );
            """)
            print()
            print("Creando tabala articulos ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS articles;
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                year_publication INTEGER,
                publisher TEXT,
                isbn_issn TEXT UNIQUE,
                keywords TEXT,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,                
                categorie_id INTEGER NOT NULL,
                FOREIGN KEY (categorie_id) REFERENCES categories(id)
                );
            """)

            print()
            print("Creando tabala libros ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS books;
            """)
            #available,borrowed,lost,damaged
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                article_id INTEGER NOT NULL,
                state TEXT NOT NULL DEFAULT 'available', 
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (article_id) REFERENCES articles(id)
                );
            """)

            print()
            print("Creando tabala prestamos ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS loans;
            """)
            #loan_type: domiciliario, sala
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                loan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                estimated_return_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                actual_return_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                loan_type TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
                );
            """)

            print()
            print("Creando tabala multas ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS fines;
            """)

            #state pending,paid
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fines(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                state TEXT NOT NULL DEFAULT 'pending',
                generation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(loan_id) REFERENCES loans(id)
                );
            """)

            print()
            print("Creando tabala reservas ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS reservations;
            """)

            #state: active, completed, cancelled
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                article_id INTEGER NOT NULL,
                state TEXT NOT NULL DEFAULT 'active',
                reservation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(article_id) REFERENCES articles(id)
                );
            """)

            print()
            print("Creando tabala notificaciones ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS notifications;
            """)

            #type: recordatorio devoluciona, reserva disponible, etc
            #method: enail, sms
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                type TEXT NOT NULL,
                method TEXT NOT NULL,
                shipping_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
                );
            """)
    

db=Create_db()
db.Crear_Tablas()
