import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/isaias/Documents/ufpb/sigerip/projeto/dados/mortalidade_infantil.csv')

df = df.drop(columns=["Total"])

# Transformar as colunas de anos em linhas
df_invertido = pd.melt(
    df,
    id_vars=["Localidade"],          # Coluna fixa (não será transformada)
    var_name="Ano",                   # Nome da nova coluna para os anos
    value_name="Dado"                 # Nome da nova coluna para os valores
)

# Converter a coluna 'Ano' para inteiro (opcional, se os anos forem numéricos)
df_invertido["Ano"] = df_invertido["Ano"].astype(int)

# Ordenar por Localidade e Ano (opcional)
df_invertido = df_invertido.sort_values(by=["Localidade", "Ano"])
df_invertido = df_invertido.reset_index(drop=True)

# Exibir resultado
# Filtrar dados para cada localidade (ajuste os nomes conforme seu DataFrame!)
brasil = df_invertido[df_invertido['Localidade'] == 'Brasil']
norte = df_invertido[df_invertido['Localidade'] == 'Norte']
nordeste = df_invertido[df_invertido['Localidade'] == 'Nordeste']
sul = df_invertido[df_invertido['Localidade'] == 'Sul']
sudeste = df_invertido[df_invertido['Localidade'] == 'Sudeste']  # Nome correto
centro_oeste = df_invertido[df_invertido['Localidade'] == 'Centro-Oeste']

paraiba = df_invertido[df_invertido['Localidade'] == 'Paraíba']
joao_pessoa = df_invertido[df_invertido['Localidade'] == '250750 JOAO PESSOA']

plt.figure(figsize=(4, 5))
plt.plot(brasil['Ano'], brasil['Dado'], label='Brasil', color='black', linestyle='-')
#plt.plot(norte['Ano'], norte['Dado'], label='Norte', linestyle='--')
plt.plot(nordeste['Ano'], nordeste['Dado'], label='Nordeste', linestyle='-', color='red')
#plt.plot(sul['Ano'], sul['Dado'], label='Sul', marker='o')
#plt.plot(sudeste['Ano'], sudeste['Dado'], label='Sudeste', marker='s')
#plt.plot(centro_oeste['Ano'], centro_oeste['Dado'], label='Centro-Oeste', marker='^')
plt.plot(paraiba['Ano'], paraiba['Dado'], label='Paraíba', linestyle='-', color='blue')
plt.plot(joao_pessoa['Ano'], joao_pessoa['Dado'], label='João Pessoa', linestyle='-', color='green')


# Personalizar
plt.title('Taxa de Mortalidade Infantil \n(2000-2023)')
plt.xlabel('Ano')
plt.ylabel('Taxa (por 1000 nascidos vivos)')
plt.legend(loc='upper right')  # Legenda fora do gráfico
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()  # Ajustar layout
plt.show()

'''plt.figure(figsize=(4, 5))
plt.plot(joao_pessoa['Ano'], joao_pessoa['Dado'], label='João Pessoa', linestyle='-.')
plt.plot(paraiba['Ano'], paraiba['Dado'], label='Paraíba', linestyle='--')

plt.title('Taxa de Mortalidade Infantil \nParaíba e João Pessoa (2000-2023)')
plt.xlabel('Ano')
plt.ylabel('Taxa (por 1000 nascidos vivos)')
plt.legend(loc='upper right')  # Legenda fora do gráfico
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()  # Ajustar layout
plt.show()'''