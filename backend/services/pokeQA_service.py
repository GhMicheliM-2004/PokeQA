# Responsável pela conexão com a API do PokeQA
# Aqui vai os serviços que fazem a ponte entre o Flask e o PokeQA
# Requests para a API do PokeQA

import requests

def busca_pokemon_nome(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    response = requests.get(url)
    
    if response.status_code == 200:
        response_json = response.json()
        response_infos = busca_info_pokemon(response_json)
        return response_infos
    else:
        return {"error": "Pokémon não encontrado"}

def busca_pokemon_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        response_json = response.json()
        response_infos = busca_info_pokemon(response_json)
        return response_infos
    else:
        return {"error": "Pokémon não encontrado"}

def busca_info_pokemon(response_json):
    nome = response_json.get("name")
    id_pokemon = response_json.get("id")
    altura = response_json.get("height")
    peso = response_json.get("weight")
    tipos = [t['type']['name'] for t in response_json.get("types")]
    stats = [{stat['stat']['name']: stat['base_stat'] for stat in response_json.get("stats", [])}]
    # imagem = response_json.get("sprites").get("home").get("front_default")

    return {
        "nome": nome,
        "id": id_pokemon,
        "altura": altura,
        "peso": peso,
        "tipos": tipos,
        "stats": stats,
        #"imagem": imagem
        }

def main():
    # Testa a função de busca por nome
    nome = input("Digite o nome do Pokémon: ")
    resultado_nome = busca_pokemon_nome(nome)
    print(f"Resultado da busca por nome ({nome}):")
    print(resultado_nome)
    
    # Testa a função de busca por ID
    pokemon_id = input("\nDigite o ID do Pokémon: ")
    resultado_id = busca_pokemon_id(pokemon_id)
    print(f"\nResultado da busca por ID ({pokemon_id}):")
    print(resultado_id)

if __name__ == "__main__":
    main()