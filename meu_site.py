from flask import Flask

app = Flask(__name__)

# CRIAR PÁGINA

# -> route: www.google.com/"route"
# -> função: O que deverá ser exibido na página

@app.route("/")
def index():
    return "Essa é a página principal! Vamos que vamos!"

if __name__ == "__main__": #Quando rodar o arquivo direto(abrindo o .py no terminal por exemplo), irá rodar essa função
    app.run(debug=True)