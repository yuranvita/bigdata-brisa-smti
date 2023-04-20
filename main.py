import src.utils.injectSQL as sql
import pandas as pd




# # VAC INSERTION SQL SCRIPT 
# df = pd.read_excel("src\database\VACINAÇÃO COMPLETO.xlsx")
# for x in range(len(df)):
#     sql.vac(
#         comunidade=df["COMUNIDADE"][x], 
#         idade=df["IDADE"][x],
#         data=df["DATA"][x],
#         qtd=df["QTD"][x],
#         sexo=df["SEXO"][x]
#         )
#     print(  df["COMUNIDADE"][x], 
#         df["IDADE"][x],
#        df["DATA"][x],
#        df["QTD"][x],
#         df["SEXO"][x])


##Queimadas
list_arr_csv = ["Focos_de_Queimadas_2017-01-01_2017-12-31.csv", "Focos_de_Queimadas_2018-01-01_2018-12-31.csv", "Focos_de_Queimadas_2019-01-01_2019-12-31.csv", "Focos_de_queimadas_2020-01-01_2020-12-31.csv", "Focos_2021-01-01_2021-12-31.csv", "Focos_de_Queimadas_2023.csv"]

for name in list_arr_csv:
    url = "src\database\\"+name
    df = pd.read_csv(url, delimiter=",")
    for x in range(len(df)):
         sql.queimadas(  
                df["datahora"][x], 
                df["satelite"][x],
                df["pais"][x],
                df["estado"][x],
                df["municipio"][x],
                df["bioma"][x],
                df["diasemchuva"][x],
                df["precipitacao"][x],
                df["riscofogo"][x],
                str(df["latitude"][x]),
                str(df["longitude"][x]),
                df["frp"][x]
                )
         print("success", x, "-", df["latitude"][x] , "-" , df["longitude"][x])

## Pecuaria 
# pecuaria_sheet = [ "Alto Alegre", "Amajari", "Boa Vista", "Bonfim", "Cantá", "Caracaraí", "Caroebe", "Iracema", "Mucajaí", "Normandia", "Pacaraima", "Rorainópolis", "São João da Baliza", "São Luiz", "Uiramutã" ]

# detalhamento = []
# ano = []
# qtd = []
# municipio = []
# for name_sheet in pecuaria_sheet:
#     # print(name_sheet)
#     df = pd.read_excel("src\database\Pecuária.xlsx", sheet_name=name_sheet)
#     data_melt = pd.melt(df.reset_index(), id_vars=["Detalhamento"],var_name='ano', value_name='qtd')
#     for x in range(len(data_melt)):
    
#         if data_melt["ano"][x] == "index":
#             print("error index não adicionado")
#         else:
#             # print("sucesso")
#             # detalhamento.append(data_melt["Detalhamento"][x])
#             # ano.append(data_melt["ano"][x])
#             # qtd.append(data_melt["qtd"][x])
#             # municipio.append(name_sheet)
#             sql.pecuaria(data_melt["Detalhamento"][x], data_melt["ano"][x], name_sheet, data_melt["qtd"][x])
        
            
    
# # data_complete = pd.DataFrame({"animal" : detalhamento, "ano" : ano, "qtd": qtd , "munucipio" : municipio})
# # data_complete.to_excel("tmp/data-frame.xlsx")



#Meteorologia dados Boa Vista

# df = pd.read_excel('src\database\Dados Meteorologico de Boa Vista.xlsx')


# for x in range(len(df)):
#     sql.umidade_ar(
#         df["Data"][x],
#         df["DIAS PRECIPTACAO FLUVIAL"][x],
#         df["TEMPERATURA MAX"][x],
#         df["TEMPERATURA MIN"][x],
#         df["UMI. RELATIVA P."][x],
#         df["V. VENTO M/S"][x],
#         df["V. VENTO MEDIA MENSAL"][x],
#         df["LAT"][x],
#         df["LON"][x],
#         df["MUNICIPIO"][x]
#           )
#     print("success data for range", x)