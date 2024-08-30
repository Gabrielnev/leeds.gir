import requests

def consulta_cnpj(cnpj):
    # Remover caracteres não numéricos do CNPJ
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Validar o comprimento do CNPJ
    if len(cnpj) != 14:
        raise ValueError("O CNPJ deve ter 14 dígitos.")
    
    # Construir a URL da API
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    
    try:
        # Realizar a requisição para a API
        response = requests.get(url)
        
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            dados = response.json()
            if 'status' in dados and dados['status'] == 'ERROR':
                print("Erro na consulta: ", dados.get('message', 'Desconhecido'))
            else:
                return dados
        else:
            print(f"Erro na requisição: {response.status_code}")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def exibir_informacoes(dados):
    if dados:
        print(f"Nome: {dados.get('nome')}")
        print(f"Nome Fantasia: {dados.get('fantasia')}")
        print(f"CNPJ: {dados.get('cnpj')}")
        print(f"Atividade Principal: {', '.join(atividade['text'] for atividade in dados.get('atividade_principal', []))}")
        print(f"Endereço: {dados.get('logradouro')}, {dados.get('numero')} - {dados.get('bairro')}, {dados.get('municipio')} - {dados.get('uf')}, {dados.get('cep')}")
        print(f"Telefone: {dados.get('telefone')}")
        print(f"Email: {dados.get('email')}")
    else:
        print("Nenhuma informação disponível.")

def main():
    cnpj = input("Digite o CNPJ da empresa (com ou sem máscara): ")
    dados_empresa = consulta_cnpj(cnpj)
    exibir_informacoes(dados_empresa)

if __name__ == "__main__":
    main()
