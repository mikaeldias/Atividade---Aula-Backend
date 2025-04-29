from flask import Flask, request
from flask import render_template

app = Flask(__name__)

user = ['Mikael', 'Yasmin', 'Matheus', 'Claudia', 'Robson']
password = ['123', '456', '789', '1011', '1213']

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_verificacao = request.form.get('usuario') 
        senha_verificacao = request.form.get('senha')
        if usuario_verificacao in user and senha_verificacao in password:
            logado = True
            return render_template('usuario.html', usuario = usuario_verificacao, logado = logado)
        else:
            logado = False
            return render_template('usuario.html',  usuario = usuario_verificacao)
    return render_template('index.html')
@app.route('/login')
def telaInicial():
    return render_template('usuario.html')
