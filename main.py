import requests

def fetch_pokemon_data(pokemon_name):
# Using API requests in order to get pokemon info
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
# Printing pokemon name, type and stats ready to ask user if they do want to to add to the team
        return {"name": name, "types": types, "stats": stats}
    else:
        return None

def add_pokemon_to_team(team, pokemon_name, pokemon_data):
# Function to add the pokemon to the list called 'team'
    # pokemon_name = input("Enter a Pokemon to check stats: ")
    # pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data:
        if len(team) < 6:
            team.append(pokemon_data)
            print(f"{pokemon_data['name']} added to your team!")
        else:
            print("Your team is full! (max 6 Pokemon)")

    # print(f"\n{team}\n")
    
def check_stats():
    # Function to add the pokemon to the list called 'team'
    pokemon_name = input("Enter a Pokemon to check stats: ")
    pokemon_data = fetch_pokemon_data(pokemon_name)
    print(pokemon_data)
    if pokemon_data:
        ans = input(f"Would you like to add {pokemon_name} to your team? (Y/N) ").lower()
        if ans == "y" or ans == "yes":
            add_pokemon_to_team(team, pokemon_name, pokemon_data)
        elif ans == "n" or ans == "no":
            print("Thats ok, who do you want to check next?")
            check_stats()
        else:
            print("I didn't understand that.")
            check_stats()
    else:
        print("That isn't a Pokemon")
        check_stats()

    check_stats()

team = []
def main():
    check_stats()


if __name__ == "__main__":
    main()