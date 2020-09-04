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
import csv
import re


# https://extendsclass.com/sqlite-browser.html


def create_schema():

   
    conn = sqlite3.connect('libreria.db')

  
    c = conn.cursor()

   
    c.execute("""
                DROP TABLE IF EXISTS libro;
            """)

  
    c.execute("""
            CREATE TABLE libro(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] TEXT NOT NULL,
                [pags] INTEGER NOT NULL,
                [author] TEXT NOT NULL
            );
            """)



   
    conn.commit()

    conn.close()

def fill():
    
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    

    with open('libreria.csv') as csvfile:
        
        data = list(csv.DictReader(csvfile))
        
        

        for i in range(len(data)):
            row = data[i]
            values= [row.get("titulo"), row.get("cantidad_paginas"), row.get("autor")]
            c.execute("""
            INSERT INTO libro (title, pags, author) VALUES (?, ?, ?);""", values)
    
            conn.commit()

    conn.close()






def fetch(id):
    
    
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM libro')
   
    for row in c.execute('SELECT * FROM libro'):
        if id == 0:
            print(row)
        elif row[0] == id:
            print(row)
        else:
            pass


def search_author(book_title):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM libro')
   
    for row in c.execute('SELECT * FROM libro'):
        if row[1] == book_title:
            print(row[3])
        else:
            pass
    
#En estas dos ultimas funciones no supe como usar el where, me dirian como seria? gracias!
        

if __name__ == "__main__":
  
  create_schema()

  
  fill()

  
  fetch(0)  # Ver todo el contenido de la DB
  fetch(3)  # Ver la fila 3
  fetch(20)  # Ver la fila 20

  
  print(search_author('Relato de un naufrago'))