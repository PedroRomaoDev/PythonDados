#%% Uso da biblioteca Streamlit para criação de aplicações web interativas

# Importando a biblioteca
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Criando um título na aplicação
st.title('Análise Interativa de Dados com Streamlit')

# Exibindo texto na aplicação
#t.write('Este é um exemplo de aplicação web simples usando Streamlit.')

# Carregando dados
df_iris = sns.load_dataset('iris')

# =============================================================================
# # Exibindo o DataFrame
st.write('Conjunto de Dados Iris:', df_iris)
# 
# # Criando um gráfico interativo com Seaborn
fig, ax = plt.subplots()
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df_iris, ax=ax)
#plt.title('Relação entre Comprimento e Largura da Sépala')
# 
# # Exibindo o gráfico na aplicação
#st.pyplot(fig)
# =============================================================================

#%% ---------------------------------------------
# Mini Exercício 5:
# Crie uma aplicação Streamlit que permita ao usuário selecionar colunas para plotar um gráfico de dispersão.
# Dica: Use st.selectbox para criar widgets de seleção.
# ---------------------------------------------

# Widgets para seleção de colunas
opcoes_colunas = df_iris.columns.tolist()[:-1]  # Excluindo a coluna 'species'
eixo_x = st.selectbox('Selecione a variável para o eixo X:', opcoes_colunas)
eixo_y = st.selectbox('Selecione a variável para o eixo Y:', opcoes_colunas)

# Criando o gráfico baseado nas seleções
fig2, ax2 = plt.subplots()
sns.scatterplot(x=eixo_x, y=eixo_y, hue='species', data=df_iris, ax=ax2)
plt.title(f'Dispersão entre {eixo_x} e {eixo_y}')

# Exibindo o gráfico na aplicação
st.pyplot(fig2)



#%% ---------------------------------------------
# Desafio:
# Construa uma aplicação utilzando streamlit, onde eu consiga ver o valor ...
# ---------------------------------------------
