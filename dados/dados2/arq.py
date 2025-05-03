import pandas as pd

df = pd.read_csv("erros.csv")
f = df[(df['regiao'] == 'Pernambuco') & (df['faixa_etaria'] == '0') & (df['ano'] == 2000)]

print(f.head())