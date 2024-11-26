from flask import Flask, jsonify
import pandas as pd

# Criando a aplicação Flask
app = Flask(__name__)

# Função para ler o CSV e retornar o DataFrame
def carregar_dados():
    try:
        # Ajuste o caminho do arquivo CSV conforme sua estrutura de pastas
        df = pd.read_csv('../ArquivosTratados/dados_tratados.csv')
        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

# Rota principal para retornar os dados em formato JSON
@app.route('/dados', methods=['GET'])
def get_dados():
    # Carregar os dados do CSV
    df = carregar_dados()

    if df is not None:
        # Convertendo o DataFrame para JSON
        # Orientação 'records' cria uma lista de dicionários
        dados_json = df.to_dict(orient='records')
        return jsonify(dados_json)  # Retorna os dados como JSON
    else:
        return jsonify({'error': 'Não foi possível carregar os dados.'}), 500

# Rota principal
@app.route('/')
def home():
    return "Bem-vindo à API de Dados de Produtos!"

if __name__ == '__main__':
    # Rodando o servidor Flask
    app.run(debug=True)
