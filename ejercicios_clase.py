#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos

    new_student('Luciana', 14, 'Carmela')
    new_student('Manuela', 12, 1)
    new_student('Marta', 16, 5, 'Yoconda')
    new_student('Melania', 15, 4, 'Angela')
    new_student('Micaela', 12, 'Monica')
    new_student('Eva', 15, 3, 'Penelope')
    


def fetch():
   
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute('SELECT * FROM estudiante')
    data = c.fetchall()
    print(data)

    c.execute('SELECT * FROM estudiante')
   
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

    conn.close()

    grade = 3
    search_by_grade(grade)

    name = 'Ananda'
    id = 1
    modify(id, name)


def insert():
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria

    new_student('Apollonia', 17, 6)
    new_student('Afrodita', 13, 2, 'Minerva')
    new_student('Venus', 14, 3)


def new_student(name, age, grade="", tutor=""):
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values = [name, age, grade, tutor]

    c.execute("""
        INSERT INTO estudiante (name, age, grade, tutor)
        VALUES (?,?,?,?);""", values)

    conn.commit()
    
    conn.close()


def search_by_grade(grade):
    
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM estudiante')
   
    for row in c.execute('SELECT * FROM estudiante'):
        if row[grade] == grade:
            print(row[0], row[1], row[2])
        else:
            pass
                    


def modify(id, name):
    
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE estudiante SET name =? WHERE id =?",(name, id)).rowcount

    print('Filas actualizadas:', rowcount)

    
    conn.commit()
    
    conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    insert()
    fetch()
    

  

    
