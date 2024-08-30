from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

api_base_url = os.getenv("API_BASE_URL")
api_key = os.getenv("API_KEY")
port = int(os.getenv("PORT", 5000))

@app.route('/empresa/<cnpj>', methods=['GET'])
def get_empresa(cnpj):
    try:
        # Faz a requisição à API externa
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(f'{api_base_url}{cnpj}', headers=headers)
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Erro ao buscar dados da empresa'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
