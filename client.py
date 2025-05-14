import requests

# URL do servidor
url = 'http://127.0.0.1:5000/enviar'

# Dados que serão enviados
dados = {
    "nome": "Veveto",
    "mensagem": "Oi, servidor!"
}

# Enviar dados com POST
resposta = requests.post(url, json=dados)

# Exibir resposta
print("Resposta do servidor:", resposta.json())
