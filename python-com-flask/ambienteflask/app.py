from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'daniel'

#####################################################
@app.route('/')
def home():
    return render_template('login.html')

################################################# Criando rota /algumacoisa e retornando a renderiz do html previamente criado e salvo na pasta templates 
# (deve ter esse nome) e ficar dentro da pasta do seu ambiente virtual.
#nesse app.route especifico eu estou puxando os dados do input digitados no html
@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get("email")
    senha = request.form.get("password")
    ################################################################
    #with open abre o arquivo, as tem a funcao de dar nome ao arquivo,
    #json.load(usuariosTemp) abre o arquivo e associa ele a variavel usuarios
    
#abrindo um doc json previamente criado e os dados de email e senha foram colocados manualmente para comparar com email e senha do valor difitado
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)  
        cont = 0
        for usuario in usuarios:
            cont += 1
            if usuario['nome'] == nome and usuario ['senha'] == senha:
                return render_template('areadocliente.html')

            if cont>= len(usuarios):
                flash('USUARIO INVALIDO')
                return redirect('/')

        


if __name__ in '__main__':
    app.run(debug=True)
