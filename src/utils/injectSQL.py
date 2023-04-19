import sqlite3
import datetime


def vac(comunidade, idade, data , sexo, qtd):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    query = conn.cursor()
    

    query.execute(
        f"INSERT INTO vac(comunidade, idade, data, sexo, qtd) values('{comunidade}' ,'{idade}' ,'{data}' , '{sexo}', '{qtd}')"
    )
    
    conn.commit()
    
    conn.close()
    

def queimadas(data, satelite, pais, estado, municipio, bioma, diassemchuva, precipitacao, riscofogo, latitude, longitude, frp):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    query = conn.cursor()
    

    query.execute(
        f"INSERT INTO queimadas(data, satelite, pais, estado, municipio, bioma, diassemchuva, precipitacao, riscofogo, latitude, longitude, frp) values('{data}' ,'{satelite}' ,'{pais}' , '{estado}', '{municipio}', '{bioma}', '{diassemchuva}', '{precipitacao}', '{riscofogo}', '{latitude}', '{longitude}', '{frp}')"
    )
    
    conn.commit()
    
    conn.close()
    
def pecuaria(animal, ano, municipio, qtd):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    query = conn.cursor()
    

    query.execute(
        f"INSERT INTO pecuaria(animal, ano, municipio, qtd) values('{animal}', '{ano}', '{municipio}', '{qtd}')"
    )
    
    conn.commit()
    
    conn.close()

def my_query(query):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    fetchData = conn.execute(query)
    
    fetchData = fetchData.fetchall()
    
    conn.close()
    
    return fetchData