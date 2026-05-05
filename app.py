from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuário')
def usuario():
    usuario = {'Nome:''Marina', 'Email:' 'marinaoligomes53@gmail.com'}
    return render_template('index.html', title='Página inicial',
     usuario=usuario)

@app.route('/contato')
def contato():
    nome = "Marina"
    return render_template('index.html', title='Página inicial', nome=nome)
    
if __name__ == '__main__':
    app.run()