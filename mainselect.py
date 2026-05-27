from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    estado = request.form['estado']
    formacao = request.form['formacao']
    modalidade = request.form.getlist('modalidades')
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    if senha == confirmar_senha:
        return "{} e {} e {} e {} e {}".format(
            nome, email, estado, formacao, modalidade
        )

    else:
        return "As senhas não conferem"