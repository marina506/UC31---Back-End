from flask import Flask, render_template
from flask import request

app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/atividade.get', methods = ['GET'])
def atividade():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    return "nome {} e curso {} e cidade {}". format(nome, curso, cidade)

if __name__ == 'main':
    app.run(debug=True)