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
        f"INSERT INTO queimadas(data, satelite, pais, estado, municipio, bioma, diassemchuva, precipitacao, riscofogo, latitude, longitude, frp) values('{data}' ,'{satelite}' ,'{pais}' , '{estado}', '{municipio}', '{bioma}', '{diassemchuva}', '{precipitacao}', '{riscofogo}', '{latitude}', '{longitude}', '{municipio}')"
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

def umidade_ar(data, dias_precipitacao_fluvial, t_max, t_min, umi_relativa_p, velo_vento_m_s, velo_vento_media_m_s, latitude, longitude, municipio):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    query = conn.cursor()
    

    query.execute(
        f"INSERT INTO umidade_ar(data, dias_precipitacao_fluvial, t_max, t_min, umi_relativa_p, velo_vento_m_s, velo_vento_media_mes_m_s, latitude, longitude, municipio) values('{data}', '{dias_precipitacao_fluvial}', '{t_max}', '{t_min}', '{umi_relativa_p}', '{velo_vento_m_s}', '{velo_vento_media_m_s}', '{latitude}', '{longitude}', '{municipio}')"
    )
    
    conn.commit()
    
    conn.close()

def my_query(query):
    
    conn = sqlite3.connect(".\\src\\database\\db.sqlite3")
    
    fetchData = conn.execute(query)
    
    fetchData = fetchData.fetchall()
    
    conn.close()
    
    return fetchData