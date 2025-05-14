from flask import Flask, request, jsonify, render_template #importando bibliotecas

modelo = Flask(__name__) #criando a aplicação

mensagens = [] #criando banco de dados local vazio (lista)
usuarios = {} #Dicionário vazio

@modelo.route('/') #chamando a url
def index():
    return render_template('index.html')  # renderiza o HTML da pasta templates

#Enviar mensagens
@modelo.route('/mensagem', methods=['POST'])
def enviar_mensagem():
    conteudo = request.json
    mensagens.append(conteudo['mensagem'])
    return jsonify({"mensagem": f"{conteudo['nome']}, sua mensagem foi salva!"}), 201 #codigo de confirmacao

#Listar mensagens
@modelo.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens), 200

#Atualizar mensagens
@modelo.route('/usuario/<id>', methods=['PUT'])
def atualizar_usuario(id):
    novo_nome = request.json.get('nome')
    usuarios[id] = novo_nome
    return jsonify({"status": f"Usuário {id} atualizado"}), 200

#Apagar mensagens
@modelo.route('/mensagem/<int:id>', methods=['DELETE'])
def apagar_mensagem(id):
    if id < len(mensagens):
        deletada = mensagens.pop(id)
        return jsonify({"status": "Apagada", "mensagem": deletada}), 200
    return jsonify({"erro": "Mensagem não encontrada"}), 404

if __name__ == '__main__':
    modelo.run(debug=True)
