#comentário em Python
#importando o flask na aplicação
from flask import Flask, render_template 
#render_template renderiza as páginas HTML

#carregando o flask em uma variável
#declarando variável no python:
app = Flask(__name__, template_folder='views')
#__name__  é uma variável de aambiente python que tem o nome do módulo atual.

#CRIANDO A ROTA PRINCIPAL DO SITE
@app.route('/')
#def serve para criar funções no python
def home():
    return render_template ('index.html')
@app.route('/games')
def games():
    return render_template ('games.html')
@app.route('/consoles')
def consoles():
    return render_template ('consoles.html')

#iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) #ligando o modo de depuração (reinicia automático)
    #.run() -> inicia um servidor
    #verificando se o app.py for o arquivo principal ele inicia o servidor.
