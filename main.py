import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

        print(f"Name: {name}")
        print(f"Types: {', '.join(types)}")
        print("Stats:")
        for stat, value in stats.items():
            print(f" {stat}: {value}")
    else:
        print(f"Pokemon '{pokemon_name}' not found.")

    print(f"Would you like to add {pokemon_name.capitalize()} to your team?")
    ans = input("(Y/N)").lower()


fetch_pokemon_data("pikachu")