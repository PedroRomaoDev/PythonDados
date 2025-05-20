
import pandas as pd

# Carregar os arquivos CSV
movies_df = pd.read_csv('movies.csv').drop(columns='Unnamed: 0')
directors_df = pd.read_csv('directors.csv').drop(columns='Unnamed: 0')

# Desafio 1: Filtrar os filmes de 2015 e ordenar por popularidade
movies_2015 = movies_df[movies_df['year'] == 2015].sort_values(by='popularity', ascending=False)[['title', 'year', 'popularity']]



# Desafio 2: Merge entre diretores e filmes e cálculo da média de receita
merged_df = pd.merge(movies_df, directors_df, left_on='director_id', right_on='id')


directors_revenue = merged_df.groupby('director_name').agg(
    qtd=('title', 'count'),
    media_receita=('revenue', 'mean')
).reset_index()



# Desafio 3: Criar a coluna de lucro e agrupar por gênero
merged_df['lucro'] = merged_df['revenue'] - merged_df['budget']

genero_lucro = merged_df.groupby('gender').agg(
    num_filmes=('title', 'count'),
    total_lucro=('lucro', 'sum')
).reset_index()

