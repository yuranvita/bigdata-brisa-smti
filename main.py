import src.utils.vacConvertTotal as vacConvertTotal
import src.utils.injectSQL as sql
import pandas as pd

df = pd.read_excel("src\database\VACINAÇÃO COMPLETO.xlsx")


for x in range(len(df)):
    sql.insert_into(
        comunidade=df["COMUNIDADE"][x], 
        idade=df["IDADE"][x],
        data=df["DATA"][x],
        qtd=df["QTD"][x],
        sexo=df["SEXO"][x]
        )
    print(  df["COMUNIDADE"][x], 
        df["IDADE"][x],
       df["DATA"][x],
       df["QTD"][x],
        df["SEXO"][x])


print(sql.my_query('SELECT * FROM vac'))

