BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"identification"	TEXT NOT NULL UNIQUE,
	"full_name"	TEXT NOT NULL,
	"address"	TEXT,
	"phone"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"birthdate"	DATE,
	"occupation"	TEXT,
	"study_center"	TEXT,
	"blocked"	TEXT DEFAULT 'False',
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "articles" (
	"id"	INTEGER,
	"title"	TEXT NOT NULL,
	"author"	TEXT,
	"year_publication"	INTEGER,
	"publisher"	TEXT,
	"isbn_issn"	TEXT UNIQUE,
	"keywords"	TEXT,
	"creation_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"categorie_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("categorie_id") REFERENCES "categories"("id")
);
CREATE TABLE IF NOT EXISTS "books" (
	"id"	INTEGER,
	"article_id"	INTEGER NOT NULL,
	"state"	TEXT NOT NULL DEFAULT 'available',
	"date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("article_id") REFERENCES "articles"("id")
);
CREATE TABLE IF NOT EXISTS "loans" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"book_id"	INTEGER NOT NULL,
	"loan_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"estimated_return_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"actual_return_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"loan_type"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "books"("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE TABLE IF NOT EXISTS "fines" (
	"id"	INTEGER,
	"loan_id"	INTEGER NOT NULL,
	"amount"	REAL NOT NULL,
	"state"	TEXT NOT NULL DEFAULT 'pending',
	"generation_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("loan_id") REFERENCES "loans"("id")
);
CREATE TABLE IF NOT EXISTS "reservations" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"article_id"	INTEGER NOT NULL,
	"state"	TEXT NOT NULL DEFAULT 'active',
	"reservation_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("article_id") REFERENCES "articles"("id")
);
CREATE TABLE IF NOT EXISTS "notifications" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"message"	TEXT NOT NULL,
	"type"	TEXT NOT NULL,
	"method"	TEXT NOT NULL,
	"shipping_date"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
INSERT INTO "users" VALUES (1,'16465368','Roberto Gomez Bolaños','Calle la valenciana','3174569987','rgb@hotmail.com','1950-01-02','comediante','Harvard','False');
INSERT INTO "users" VALUES (2,'656565','Pepe Cortizona','Calle 25','31636323','pepe@pepe.lat','1969-06-01','Comediante','Valle','False');
INSERT INTO "users" VALUES (3,'154652563','Felipe Noguera','Calle 70 No. 20 - 55','3154639878','felipe@hotmail.com','1970-05-26','Ayudante','Libre','False');
INSERT INTO "users" VALUES (4,'58663323','Pedro Casas','Calle 50','6536563','fff@fff.com','1965-12-31','inge','catolica','False');
INSERT INTO "users" VALUES (5,'65656565','Rony','Calle 50','55555555','rony@hotmail.com','2012-10-04','Hacer pereza','universidad de la vida','False');
INSERT INTO "categories" VALUES (1,'Ingenieria');
INSERT INTO "categories" VALUES (2,'Audiolibro');
INSERT INTO "categories" VALUES (3,'Filosofia');
INSERT INTO "categories" VALUES (4,'Derecho');
INSERT INTO "categories" VALUES (5,'Historia');
INSERT INTO "categories" VALUES (6,'Electronica');
INSERT INTO "articles" VALUES (1,'Diseño de Bases de Datos','Jose Capacho Portilla','2017-01-01','E-book',' ISBN-13: 9789587418255','Diseño bases de datos','2024-09-02 03:50:47',1);
INSERT INTO "articles" VALUES (2,'Comunicacion Diseño Digital','Eduardo Enrrique Zurek','2018-01-01','E-book',' ISBN-13: 9789587419672','Electronica, diseño, digital','2024-09-02 03:53:17',6);
INSERT INTO "articles" VALUES (3,'Modelado y simulación de redes de computadores','Jose Marquez Diaz',2013,'E-book',' ISBN-13: 9789587413755','Redes, datos, modelado, computadores','2024-09-02 03:55:50',1);
COMMIT;
