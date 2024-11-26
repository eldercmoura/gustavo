import pandas as pd

def tratar_dados():
    # Carregar os dados dos arquivos CSV
    tabela_produtos = pd.read_csv('../BasesOriginais/produtos.csv')
    tabela_precos = pd.read_csv('../BasesOriginais/precos.csv')

    # Tratar dados faltantes
    tabela_produtos.dropna(inplace=True)
    tabela_precos.dropna(inplace=True)

    # Tratar dados duplicados
    tabela_produtos.drop_duplicates(inplace=True)
    tabela_precos.drop_duplicates(inplace=True)

    # Tratar outliers
    Q1 = tabela_precos['precos'].quantile(0.25)
    Q3 = tabela_precos['precos'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    tabela_precos = tabela_precos[(tabela_precos['precos'] >= lower_bound) & (tabela_precos['precos'] <= upper_bound)]

    # Salvar os dados tratados
    tabela_produtos.to_csv('../ArquivosTratados/produtos_tratados.csv', index=False)
    tabela_precos.to_csv('../ArquivosTratados/precos_tratados.csv', index=False)

if __name__ == '__main__':
    tratar_dados()
