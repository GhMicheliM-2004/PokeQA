# Define URL base para o serviço PokeQA (exemplo: "/pokemon/nome_do_pokemon")
from flask import Blueprint, make_response, jsonify

user_bp = Blueprint('pokeQA', __name__, template_folder='../templates')

@user_bp.route('/')
def get_index():
    return '''
        <h1>Bem-vindo à API PokeQA</h1>
    '''

@user_bp.route('/<string:nome>')
def get_pokemon_by_name(nome):
    return '''
        <h1>Aqui vai a lógica para buscar o Pokémon pelo nome
    '''
    # from backend.services.pokeQA_service import busca_pokemon_nome
    # resultado = busca_pokemon_nome(nome)
    # return make_response(
    #     jsonify(resultado)
    # )
    # from backend.services.pokeQA_service import busca_pokemon_nome, busca_info_pokemon
    # resultado_pokemon = busca_pokemon_nome(nome)
    # if "error" not in resultado_pokemon:
    #     resultado_info = busca_info_pokemon(resultado_pokemon)
    #     return make_response(
    #         jsonify(resultado_info)
    #     )
    # else:
    #     return make_response(
    #         jsonify({"error": "Pokémon não encontrado"})
    #     )

@user_bp.route('/<int:pokemon_id>')
def pokemon_by_id(pokemon_id):
    return '''
        <h1>Aqui vai a lógica para buscar o Pokémon pelo ID
    '''
    # from backend.services.pokeQA_service import busca_pokemon_id
    # resultado = busca_pokemon_id(pokemon_id)
    # return make_response(
    #     jsonify(resultado)
    # )
    # from backend.services.pokeQA_service import busca_pokemon_nome, busca_info_pokemon
    # resultado_pokemon = busca_pokemon_nome(nome)
    # if "error" not in resultado_pokemon:
    #     resultado_info = busca_info_pokemon(resultado_pokemon)
    #     return make_response(
    #         jsonify(resultado_info)
    #     )
    # else:
    #     return make_response(
    #         jsonify({"error": "Pokémon não encontrado"})
    #     )

@user_bp.route('/pokedex')
def get_pokedex():
    return '''
        <h1>Aqui vai a lógica para retornar a Pokédex completa
    '''
    # Aqui vai uma adição no sistema onde posso selecionar quais pokemon que eu tenho em minha coleção e imprimir um relatório

