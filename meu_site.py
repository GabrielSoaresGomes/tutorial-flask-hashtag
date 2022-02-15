from flask import Flask

app = Flask(__name__)

# CRIAR PÁGINA

# -> route: www.google.com/"route"
# -> função: O que deverá ser exibido na página

@app.route("/")
def index():
    return "Essa é a página principal!"

app.run()