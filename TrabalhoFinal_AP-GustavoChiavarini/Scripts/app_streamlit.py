import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados do arquivo CSV
@st.cache
def carregar_dados():
    caminho_arquivo = '1_bases_tratadas/dados_tratados.csv'  # Caminho para o arquivo CSV
    df = pd.read_csv(caminho_arquivo)
    
    # Converte a coluna 'preco2' para valores numéricos, forçando valores não numéricos a se tornarem NaN
    df['preco2'] = pd.to_numeric(df['preco2'], errors='coerce')
    
    return df

# Carregar os dados
dados = carregar_dados()

# Certifique-se de que 'preco2' é uma coluna numérica antes de calcular as estatísticas
if dados['preco2'].isnull().any():
    st.write("Existem valores ausentes na coluna 'preco2' que foram convertidos para NaN.")

# Cálculos das estatísticas
media = dados['preco2'].mean()
mediana = dados['preco2'].median()
desvio_padrao = dados['preco2'].std()

# Exibir as estatísticas
st.write(f"### Estatísticas da Coluna 'preco2'")
st.write(f"- **Média**: {media:.2f}")
st.write(f"- **Mediana**: {mediana:.2f}")
st.write(f"- **Desvio Padrão**: {desvio_padrao:.2f}")

# Gráfico de Histogram
st.write("### Histograma de 'preco2'")
fig, ax = plt.subplots()
sns.histplot(dados['preco2'].dropna(), kde=True, ax=ax)  # Remove NaN antes de plotar
st.pyplot(fig)

# Gráfico de Boxplot
st.write("### Boxplot de 'preco2'")
fig, ax = plt.subplots()
sns.boxplot(x=dados['preco2'], ax=ax)
st.pyplot(fig)

# Gráfico de Barra (utilizando a contagem de preços por intervalos)
st.write("### Gráfico de Barras de Contagem de Intervalos de 'preco2'")
bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Exemplo de intervalos de preços
dados['intervalo_preco'] = pd.cut(dados['preco2'], bins=bins)
fig, ax = plt.subplots()
dados['intervalo_preco'].value_counts().sort_index().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Gráfico de Pizza (distribuição percentual dos preços)
st.write("### Gráfico de Pizza de 'preco2'")
fig, ax = plt.subplots()
dados['intervalo_preco'].value_counts().sort_index().plot(kind='pie', ax=ax, autopct='%1.1f%%')
st.pyplot(fig)
