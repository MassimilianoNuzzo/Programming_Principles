'''
Scrivi un programma che chiede all'utente
un nome di un pokemon.
Invia una richiesta GET all'api pokeapi.co,
verifica se ha successo,
e in caso affermativo stampa a schermo 
l'altezza, il peso e il tipo del pokemon.
'''

import requests

try:

    pokemon_name = input('Inserisci il nome di un pokemon: ').strip().lower()

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    response.raise_for_status()

    data = response.json()

    pokemon_height = data['height']/10
    pokemon_weight = data['weight']/10
    pokemon_types = []

    for type_info in data['types']:
        pokemon_types.append(type_info['type']['name'])

    print(f'Altezza: {pokemon_height} m')
    print(f'Peso: {pokemon_weight} kg')
    print(f'Tipi: {', '.join(pokemon_types)}')
    
except requests.exceptions.HTTPError:
    
    print('Errore nella richiesta Http.') 

