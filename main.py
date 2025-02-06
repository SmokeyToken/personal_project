import requests

def fetch_pokemon_data(pokemon_name):
    # Using API requests to get Pokémon info
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        stats = data["stats"]  # Keep stats as a list of dictionaries
        return {"name": name, "types": types, "stats": stats}
    else:
        return None

def add_pokemon_to_team(team, pokemon_data):
    # Function to add the Pokémon to the list called 'team'
    if pokemon_data:
        if len(team) < 6:
            team.append(pokemon_data)
            print(f"{pokemon_data['name']} added to your team!")
        else:
            print("Your team is full! (max 6 Pokémon)")

def check_stats(team):
    # Function to check Pokémon stats and add to the team
    while True:
        pokemon_name = input("Enter a Pokémon to check stats: ")
        pokemon_data = fetch_pokemon_data(pokemon_name)

        if pokemon_data:
            print(f"\nName: {pokemon_data['name']}")
            print(f"Types: {', '.join(pokemon_data['types'])}")
            print("Stats:")
            for stat in pokemon_data["stats"]:
                print(f"  {stat['stat']['name']}: {stat['base_stat']}")

            ans = input(f"\nWould you like to add {pokemon_data['name']} to your team? (Y/N) ").lower()
            if ans == "y" or ans == "yes":
                add_pokemon_to_team(team, pokemon_data)
                break  # Exit the loop after adding the Pokémon
            elif ans == "n" or ans == "no":
                print("That's okay. Let's check another Pokémon.")
            else:
                print("I didn't understand that. Please enter Y or N.")
        else:
            print("That isn't a valid Pokémon. Please try again.")

def display_team(team):
    if not team:
        print("Your team is empty.")
    else:
        print("Your team:")
        for pokemon in team:
            stats_str = ", ".join([f"{s['stat']['name']}: {s['base_stat']}" for s in pokemon['stats']])
            print(f"- {pokemon['name']} ({', '.join(pokemon['types'])}) ({stats_str})")

def main():
    team = []
    while True:
        print("\n1. Add Pokémon to team")
        print("2. View team")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_stats(team)
        elif choice == "2":
            display_team(team)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()