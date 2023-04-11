import pandas as pd


comunidade = []
idade = []
sexo = []
qtd = []
data = []

vac = ['VACINAÇÃO 2017','VACINAÇÃO 2018', 'VACINAÇÃO 2019' , 'VACINAÇÃO 2020']

for name in vac:
    number = 8
    if(name == "VACINAÇÃO 2020"):
        number = 4
    for x in range(number):
        url = ".\src\database\\"+name+".xlsx"
        df = pd.read_excel(url,sheet_name=x)


        for i in range(len(df)):
            
            comunidade.append(df['COMUNIDADE'][i])
            idade.append(df['IDADE'][i])
            data.append(df['DATA'][i])
            qtd.append(df['MACHO'][i])
            sexo.append("M")
            comunidade.append(df['COMUNIDADE'][i])
            idade.append(df['IDADE'][i])
            data.append(df['DATA'][i])
            qtd.append(df['FÊMEA'][i])
            sexo.append("F")
    

data = {'COMUNIDADE' : comunidade, 'IDADE': idade , 'DATA' : data , 'SEXO' : sexo , 'QTD' : qtd}

data_complete = pd.DataFrame(data)
data_complete.to_excel(".\\tmp\\data-frame.xlsx")
print(data)