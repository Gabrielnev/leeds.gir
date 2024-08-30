from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Função para consultar a API ReceitaWS
def consulta_empresa(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota de busca
@app.route('/buscar', methods=['POST'])
def buscar():
    cnpj = request.form.get('cnpj')
    if cnpj:
        dados_empresa = consulta_empresa(cnpj)
        if dados_empresa:
            return render_template('resultados.html', empresa=dados_empresa)
        else:
            return "Erro ao buscar a empresa. Verifique o CNPJ e tente novamente."
    return "CNPJ não fornecido."

if __name__ == '__main__':
    app.run(debug=True)
