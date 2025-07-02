import pandas as pd

mapeamento = {
    # Primeira lista → Padrão da segunda lista
    "Amapá": "Amapá",
    "Ceará": "Ceará",
    "Espírito Santo": "Espírito Santo",
    "Goiás": "Goiás",
    "Maranhão": "Maranhão",
    "Paraná": "Paraná",
    "Piauí": "Piauí",
    "Rondônia": "Rondônia",
    "São Paulo": "São Paulo",
    "Paraíba": "Paraíba",
    "Pará": "Pará",
}
df = pd.read_csv("C:/Users/isaias/Documents/ufpb/sigerip/dados/dados1/metricas_erro_combinado.csv")
df["Local"] = df["Local"].replace(mapeamento)
print(df["Local"].unique())
#salvar o dataframe corrigido
df.to_csv("C:/Users/isaias/Documents/ufpb/sigerip/dados/dados1/metricas_erro_combinado_.csv", index=False)