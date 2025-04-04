import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import folium
import geobr

dados = pd.read_csv('C:/Users/isaias/Documents/ufpb/sigerip/projeto/dados/dados3/taxas_mortal_inf_mun.csv', encoding='latin-1', sep=';')
dados1 = dados[dados['Ano'] == 2020]
#print(dados1)
cidades_paraiba = pd.read_csv("C:/Users/isaias/Documents/ufpb/sigerip/projeto/dados/dados3/cod_mun.csv", sep=';')
data5 = {
    'nome_municipio': [],
    'valor': [],
    'ano': []
    }


for row1 in dados1.itertuples():
    codigo = row1.cod
    for row in cidades_paraiba.itertuples():
        if codigo == row.cod:
            #print(row)
            data5['nome_municipio'].append(row1.Localidade)
            data5['valor'].append(row1.Taxa)
            data5['ano'].append(row1.Ano)

data1 = pd.DataFrame(data5)
data2 = data1.dropna()
#print(data2)

# Carregar dados dos municípios da Paraíba (código do estado: 25)
paraiba = geobr.read_municipality(code_muni='PB', year=2020)

# Dados de exemplo (substitua com seus dados)
data = {
    'nome_municipio': data2['nome_municipio'],
    'valor': data2['valor']
}
df = pd.DataFrame(data)

paraiba_data = paraiba.merge(df, left_on='name_muni', right_on='nome_municipio')

fig, ax = plt.subplots(figsize=(12, 8))

# Plotar o mapa
paraiba_data.plot(
    column='valor',
    cmap='YlOrRd',  # Escala de cores (pode usar 'viridis', 'plasma', etc.)
    linewidth=0.8,
    ax=ax,
    edgecolor='black',
    legend=True,
    legend_kwds={'label': "Legenda do Heatmap"}
)

# Configurações do gráfico
plt.title('Heatmap dos Municípios da Paraíba')
plt.axis('off')
plt.show()

# Criar mapa centrado na Paraíba
m = folium.Map(location=[-7.1193, -36.8245], zoom_start=7)

# Adicionar dados ao mapa
folium.Choropleth(
    geo_data=paraiba_data,
    name='choropleth',
    data=paraiba_data,
    columns=['name_muni', 'valor'],
    key_on='feature.properties.name_muni',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Legenda do Heatmap'
).add_to(m)

# Salvar ou exibir o mapa
m