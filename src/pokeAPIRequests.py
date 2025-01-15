import requests

def validate_pokemon(name):
    """Check if the given name is a valid Pokémon using PokéAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False

def validate_move(move):
    """Check if the given move is valid using PokéAPI."""
    url = f"https://pokeapi.co/api/v2/move/{move.lower().replace(' ', '-')}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False

def get_pokemon_data(name):
    """Fetch Pokémon stats and moves from PokéAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        moves = [move["move"]["name"] for move in data["moves"]]
        return {"stats": stats, "moves": moves}
    return None