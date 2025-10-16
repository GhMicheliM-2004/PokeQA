# Inicializa o servidor web Flask
from flask import Flask, make_response, jsonify
# from services.pokeQA_service import busca_pokemon_nome, busca_pokemon_id, busca_info_pokemon
from flask import render_template
from teste import data

app = Flask(__name__, template_folder='../templates') # Define o diretório dos templates HTML

# Endpoint da página inicial
@app.route('/')
def get_index():
    return render_template("index.html") # Renderiza o template index.html

# Endpoint para retornar os dados do arquivo teste.py
@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    return make_response(
        jsonify(data)
    )


def main():
    app.run(debug=True)
    # nome = input("Digite o nome do Pokémon: ")
    # if nome():
    #     resultado_nome = busca_pokemon_nome(nome)
    #     print(f"Resultado da busca por nome ({nome}):")
    # else:
    #     pokemon_id = input("Digite o ID do Pokémon: ")
    #     resultado_nome = busca_pokemon_id(pokemon_id)
    #     print(f"\nResultado da busca por ID ({pokemon_id}):")
    # print(resultado_nome)

if __name__ == "__main__":
    main()