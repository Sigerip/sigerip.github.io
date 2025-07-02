import pandas as pd

df = pd.read_csv("C:/Users/isaias/Documents/ufpb/sigerip/dados/output.csv")
df2 = pd.read_csv("utf8.csv", sep=';')
#df2.to_csv('utf8.csv', encoding='utf-8', index=False)

df_geral = pd.concat([df, df2])
print(df_geral)
df_geral.to_csv('mort_infantil.csv', index=False)