# Inicializa o servidor web Flask
from flask import Flask
from flask import render_template
from routes.pokeQA_routes import user_bp

app = Flask(__name__, template_folder='../templates') # Define o diretório dos templates HTML

# Endpoint da página inicial
@app.route('/')
def get_index():
    return render_template("index.html") # Renderiza o template index.html

app.register_blueprint(user_bp, url_prefix ='/pokemon')  # Registra o blueprint para as rotas do PokeQA

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()