import sqlite3
import datetime


def insert_into(comunidade, idade, data , sexo, qtd):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    query = conn.cursor()
    

    query.execute(
        f"INSERT INTO vac(comunidade, idade, data, sexo, qtd) values('{comunidade}' ,'{idade}' ,'{data}' , '{sexo}', '{qtd}')"
    )
    
    conn.commit()
    
    conn.close()

def my_query(query):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    fetchData = conn.execute(query)
    
    fetchData = fetchData.fetchall()
    
    conn.close()
    
    return fetchData