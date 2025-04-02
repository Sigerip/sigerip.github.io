import pandas as pd

ambos = pd.read_csv('tabua_ambos(3).csv', encoding='latin1', sep=';')
feminino = pd.read_csv('tabua_mulheres(1).csv', encoding='latin1', sep=';')
masculino = pd.read_csv('tabua_homens(2).csv', encoding='latin1', sep=';')
data = {
    'Ano': ambos['Ano'],
    'local': ambos['Local'],
    'faixa_etaria': ambos['Grupo Etário'],
    'ambos': ambos['nMx'],
    'feminino': feminino['nMx'],
    'masculino': masculino['nMx']
}



df = pd.DataFrame(data)
df.to_csv('taxa_mortalidade.csv', index=False)
print(df.head())
print(df.tail())
#data.to_csv('tabua_concatenada.csv', index=False)