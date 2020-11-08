from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('about.html')


@app.route('/loja')
def loja():
    return render_template('loja.html')


@app.route('/portifolio')
def portifolio():
    return render_template('portfolio.html')


@app.route('/contato')
def contato():
    return render_template('contact.html')


@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

if __name__ == '__main__':
    app.run()
