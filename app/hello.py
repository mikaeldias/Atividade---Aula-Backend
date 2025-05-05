import uuid
from flask import Flask, request, flash, redirect, url_for
from flask import render_template

app = Flask(__name__)
app.secret_key = 'Mikael_é_fodaaaaa'

user = ['Mikael', 'Yasmin', 'Matheus', 'Claudia', 'Robson']
password = ['123', '456', '789', '1011', '1213']
# dicionario para armazenar musicas
musicas = {}
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_verificacao = request.form.get('usuario') 
        senha_verificacao = request.form.get('senha')
        if usuario_verificacao in user and senha_verificacao in password:
            logado = True
            return render_template('usuario.html', usuario = usuario_verificacao, logado = logado, musicas = musicas)
        else:
            flash('Senha incorreta. Tente novamente.', 'warning')
            return redirect(url_for('login')) # retorna a url correspondente da função
    return render_template('index.html')

@app.route('/usuario', methods=['GET', 'POST'])
def cadastrar_musica():
    if request.method == 'POST':
        # pegar nome cantor
        cantor = request.form.get('cantor')
        musica = request.form.get('musica')

        # cria id diverso
        musica_id = str(uuid.uuid4())

        musicas[musica_id] = {
                'nome': cantor,
                'musica': musica
        }
 
    return render_template('usuario.html', musicas = musicas)

@app.route('/remover/<musica_id>', methods=['POST'])
def remover_musica(musica_id):
    if musica_id in musicas:
        del musicas[musica_id]
        flash('Música Removida com sucesso', 'success')
    else:
        flash('Música não encontrada.', 'danger')
    return redirect(url_for('cadastrar_musica'))
