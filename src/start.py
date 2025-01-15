from nltk.tokenize import word_tokenize
from pokeAPIRequests import validate_pokemon, validate_move, get_pokemon_data

stats = ["hp", "spAtk", "attack", "defense", "spDef", "speed"]
actions = ["into"]

def process_input(user_input):
    tokens = word_tokenize(user_input)
    pokemon_names = [token for token in tokens if validate_pokemon(token)]
    moves = [token for token in tokens if validate_move(token)]
    extracted_stats = [token for token in tokens if token.lower() in stats]
    extracted_actions = [token for token in tokens if token.lower() in actions]

    result = {"pokemon": {}, "actions": extracted_actions}
    for pokemon in pokemon_names:
        data = get_pokemon_data(pokemon)
        if data:
            result["pokemon"][pokemon] = {
                "stats": data["stats"],
                "moves": moves if moves else data["moves"][:5],
            }
    return result

# Test with sample input
user_input = "Max spAtk Gengar shadow-ball into max hp max bulk Chansey"
output = process_input(user_input)
print(output)