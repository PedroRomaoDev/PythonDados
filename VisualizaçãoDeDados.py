#Matplotlib, Seaborn, Folium e Streamlit

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%% Matplotlib
#Plotar a função seno

# Gerando dados para o eixo x
x = np.linspace(0, 10, 100)
# Calculando o seno de x
y = np.sin(x)

# Criando o gráfico básico
plt.plot(x, y)

# Adicionando título e labels aos eixos
plt.title('Gráfico da Função Seno')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrando o gráfico
plt.show()

#%% ---------------------------------------------
# Mini Exercício 1:
# Plote a função cosseno no mesmo gráfico da função seno 
# ---------------------------------------------
y_cos = np.cos(x)

# Criando o gráfico com as duas funções
plt.plot(x, y, label='Seno')
plt.plot(x, y_cos, label='Cosseno')

# Adicionando título, labels e legenda
plt.title('Gráfico das Funções Seno e Cosseno')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

# Mostrando o gráfico
plt.show()


#%% 

# Definindo o tamanho da figura
plt.figure(figsize=(10, 6))

# Plotando as funções com estilos personalizados
plt.plot(x, y, color='blue', linewidth=2, linestyle='--', label='Seno')
plt.plot(x, y_cos, color='red', linewidth=2, linestyle='-', label='Cosseno')

# Adicionando grid, título, labels e legenda
plt.grid(True)
plt.title('Funções Gasto/Economia')
plt.xlabel('Eixo de Gasto')
plt.ylabel('Eixo Economia')
plt.legend()

# Encontrando os índices dos valores máximos
max_index_sin = np.argmax(y)
max_index_cos = np.argmax(y_cos)

# Coordenadas dos máximos
max_x_sin = x[max_index_sin]
max_y_sin = y[max_index_sin]

max_x_cos = x[max_index_cos]
max_y_cos = y_cos[max_index_cos]

# Adicionando anotações nos pontos máximos de forma dinâmica
plt.annotate('Máximo Gasto', xy=(max_x_sin, max_y_sin), xytext=(max_x_sin + 0.5, max_y_sin - 0.2),
             arrowprops=dict(facecolor='blue', shrink=0.05))
plt.annotate('Máximo Economizado', xy=(max_x_cos, max_y_cos), xytext=(max_x_cos + 0.5, max_y_cos - 0.2),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Salvando o gráfico em um arquivo
plt.savefig('grafico_contas.png')

# Mostrando o gráfico
plt.show()

#%% ---------------------------------------------
# Mini Exercício 2:
# Crie um gráfico personalizado da função tangente no intervalo de -1.5, 1.5
# Adicione títulos, labels, grid e customize as cores e estilos de linha.
# Dica: Use np.tan(x)
# ---------------------------------------------


# Gerando dados para o eixo x, evitando pontos de descontinuidade
x_tan = np.linspace(-1.5, 1.5, 100)
y_tan = np.tan(x_tan)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_tan, y_tan, color='green', linewidth=2, linestyle='-.', label='Tangente')

# Adicionando grid, título, labels e legenda
plt.grid(True)
plt.title('Gráfico da Função Tangente')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

# Definindo limites para o eixo y
plt.ylim(-10, 10)

# Mostrando o gráfico
plt.show()
#%% Seaborn - Visualizações mais complexas
# Exemplo: Gráfico de dispersão com regressão linear

# Carregando um conjunto de dados do Seaborn
df = sns.load_dataset('tips')

# Visualizando as primeiras linhas do DataFrame
print(df.head())

# Criando o gráfico de dispersão com linha de regressão
sns.lmplot(x='total_bill', y='tip', data=df)

# Adicionando título ao gráfico
plt.title('Relação entre Valor da Conta e Gorjeta')

# Mostrando o gráfico
plt.show()

#%% ---------------------------------------------
# Mini Exercício 3:
# Use o Seaborn para criar um gráfico de barras que compare o total médio da conta por dia da semana.
# ---------------------------------------------
# Criando o gráfico de barras
sns.barplot(x='day', y='total_bill', data=df, estimator=np.mean)

# Adicionando título e labels
plt.title('Total Médio da Conta por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Total Médio da Conta')

# Mostrando o gráfico
plt.show()


#%% Uso da biblioteca Folium para criação de mapas interativos
import folium
from folium.plugins import MarkerCluster

# Criando um mapa centralizado em uma coordenada específica
mapa = folium.Map(location=[-15.7797, -47.9297], zoom_start=4)

marker_cluster = MarkerCluster().add_to(mapa)

# Adicionando marcadores para algumas capitais brasileiras
folium.Marker(location=[-23.5505, -46.6333], popup='São Paulo').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1729], popup='Rio de Janeiro').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1749], popup='Rio de Janeiro2').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1749], popup='Rio de Janeiro2').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1749], popup='Rio de Janeiro2').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1749], popup='Rio de Janeiro2').add_to(marker_cluster)
folium.Marker(location=[-22.9068, -43.1749], popup='Rio de Janeiro2').add_to(marker_cluster)
folium.Marker(location=[-15.8267, -47.9218], popup='Brasília').add_to(mapa)
folium.Marker(location=[-12.9777, -38.5016], popup='Salvador').add_to(mapa)

# Exibindo o mapa no Jupyter Notebook 
# mapa

# Salvando o mapa em um arquivo HTML
mapa.save('mapa_brasil.html')

#%% ---------------------------------------------
# 
# ---------------------------------------------

from folium import Icon

# Adicionando marcadores personalizados
folium.Marker(
    location=[-8.0632, -34.8711],
    popup='Recife',
    icon=Icon(color='green', icon='cloud')
).add_to(mapa)

folium.Marker(
    location=[-3.1190, -60.0217],
    popup='Manaus',
    icon=Icon(color='purple')
).add_to(mapa)

folium.Marker(
    location=[-25.4284, -49.2733],
    popup='Curitiba',
    icon=Icon(color='orange', icon='user')
).add_to(mapa)

# Salvando o mapa atualizado
mapa.save('mapa_brasil_atualizado.html')



