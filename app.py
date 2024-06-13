from flask import Flask, request, render_template, redirect, url_for, flash
#import requests
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.get('/')
def get(d):
    return d


#class PessoaJuridica(db.Model):
    #razao_social = db.Column(db.String(100))
    #cnpj = db.Column(db.String(20), primary_key=True)
    #ie = db.Column(db.String(100))
    #contato = db.Column(db.String(100))
    #telefone = db.Column(db.String(20))
    #celular = db.Column(db.String(20))
    #email = db.Column(db.String(50))
    #endereco = db.Column(db.String(100))
    #cep = db.Column(db.String(20))
    #bairro = db.Column(db.String(30))
    #cidade = db.Column(db.String(30))
    #estado = db.Column(db.String(30))

    
#class ParticipanteEvento(db.Model):
    #nome = db.Column(db.String(50))
    #email = db.Column(db.String(50))
    #telefone = db.Column(db.String(20))
    #celular = db.Column(db.String(20))
    #cpf = db.Column(db.String(20))
    #cargo = db.Column(db.String(60))

if __name__ == '__main__':
    app.run(debug=True)

