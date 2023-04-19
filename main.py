import src.utils.injectSQL as sql
import pandas as pd




## VAC INSERTION SQL SCRIPT 
#df = pd.read_excel("src\database\VACINAÇÃO COMPLETO.xlsx")
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


## Queimadas    
# queimadas_abas = ["Planilha1" , "Planilha2", "Planilha3", "Planilha4", "Planilha5"]
# for name in queimadas_abas:
#     df = pd.read_excel("src\database\queimadas_geral.xlsx", sheet_name=name)
#     print("*"*100)
#     for x in range(len(df)):
#         lat = df["latitude"][x]
#         lon = df["longitude"][x]
#         lat_str = len(str(lat))
#         lon_str = len(str(lon))
#         lat_decimal = lat/10**(lat_str-1)
#         lon_decimal = lon/10**(lon_str-3)
#         sql.queimadas(  
#                 df["datahora"][x], 
#                 df["satelite"][x],
#                 df["pais"][x],
#                 df["estado"][x],
#                 df["municipio"][x],
#                 df["bioma"][x],
#                 df["diasemchuva"][x],
#                 df["precipitacao"][x],
#                 df["riscofogo"][x],
#                 lat_decimal,
#                 lon_decimal,
#                 df["frp"][x]
#                 )
#         print(df["datahora"][x], 
#                 df["satelite"][x],
#                 df["pais"][x],
#                 df["estado"][x],
#                 df["municipio"][x],
#                 df["bioma"][x],
#                 df["diasemchuva"][x],
#                 df["precipitacao"][x],
#                 df["riscofogo"][x],
#                 lat_decimal,
#                 lon_decimal,
#                 df["frp"][x])


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