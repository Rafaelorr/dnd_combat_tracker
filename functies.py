import json

def get_valid_invatie(initiative_lijst) -> int | None:
    """Get a valid initiative value that doesn't already exist."""
    while True:
        invatie = get_valid_number(
            "Invatie van de nieuwe entry: ",
            "De invatie van de nieuwe entry moet een nummer zijn, bv: 10"
        )

        # Check if initiative already exists
        if initiative_lijst.get(invatie):
            print("Gekozen invatie bestaat al")

            if input("Kies je een ander invatie? y/n: ").lower() != "y":
                return None
            continue

        return invatie

def get_valid_name() -> str:
    """Get a non-empty name for the entry."""
    while True:
        naam = input("Naam van de nieuwe entry: ").strip()

        if naam:
            return naam

        print("TIP: Geef de nieuw invatie entry een naam")

def get_valid_number(prompt, error_message) -> int:
    """Get a valid integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def maak_lijst_van_initiative_lijst(initiative_lijst:dict) -> list:
    """Maakt een lijst van alle waarden in een initiative dict."""
    lijst : list = list(initiative_lijst.keys())
    lijst.sort(reverse=True)

    return lijst

def kies_entry_in_initiative_lijst(initiative_lijst:dict) -> int:
    """Geeft de initative van een bepaalde entry in het initative"""
    lijst = maak_lijst_van_initiative_lijst(initiative_lijst)

    for item in lijst:
        print(f'{int(lijst.index(item))}. {initiative_lijst[item]["NAAM"]}')

    index :int = lijst[get_valid_number(
        "Welke wil je bewerken? ",
        "De entry die kiest moet een nummer zijn, bv:0"
    )]

    return index

def help_cli():
    """Print een lijst van alle commando's en een korte beschrijving van hun functie."""
    print("""
    Commands:
    - help: Toont alle commands
    - exit: Stopt het programma
    - list: Toont alle invatie entries in volgorde
    - add: Voegt een invatie entry toe
    - delete: Verwijdert een invatie entry
    - show: Toont de hit points en armor class van een invatie entry
    - edit_hp: Verandert de hit points van een invatie entry
    - edit_ac: Verandert de armor class van een invatie entry
    - clear: Wist het scherm
    - save: slaat het initiative op in een json bestand
    - load: laad het initiative van een json bestand
    """)

def add(initiative_lijst:dict) -> dict[dict]:
    """Voegt een nieuwe entry toe aan de initative."""
    # Get initiative (return None if user cancels)
    invatie = get_valid_invatie(initiative_lijst)
    if invatie is None:
        return None

    naam = get_valid_name()

    hp = get_valid_number(
      "Hit points van de nieuwe entry: ",
      "Type de hit points van de nieuwe entry als een nummer bv: 1"
    )

    ac = get_valid_number(
      "Armor class van de nieuwe entry: ",
      "Type de armor class van de nieuwe entry als een nummer bv: 1"
    )

    initiative_lijst[invatie] = {
      "NAAM": naam,
      "HP": hp,
      "AC": ac
    }

    return initiative_lijst

def toon_alle_entries(initiative_lijst:dict) -> None:
    """Deze functie print een genummerde lijst van alle entries in de initative lijst."""
    lijst = maak_lijst_van_initiative_lijst(initiative_lijst)

    for item in lijst:
        print(f'{item}. {initiative_lijst[item]["NAAM"]}')

def edit_hp(initiative_lijst:dict) -> dict[dict]:
    """Past de hit points van een initative entry aan."""
    index :int = kies_entry_in_initiative_lijst(initiative_lijst)

    print()
    print(f'De huidige hp van {initiative_lijst[index]["NAAM"]}: {initiative_lijst[index]["HP"]}')
    print()

    verander_hp_hoeveelheid :int = get_valid_number(
        f'Hoeveel wil je aan de hit points van {initiative_lijst[index]["NAAM"]} toevoegen ? ',
        "De hoeveelheid die je aan de hit points wilt toevoegen moet een nummer zijn, bv: 12"
    )

    initiative_lijst[index]["HP"] += verander_hp_hoeveelheid

    return initiative_lijst

def show(initiative_lijst:dict) -> None:
    """Toont de hit points en armor class van een geselecteerde initiative entry."""
    index :int = kies_entry_in_initiative_lijst(initiative_lijst)

    print()
    print(f'De hit points van {initiative_lijst[index]["NAAM"]}: {initiative_lijst[index]["HP"]}')
    print(f'De armor class van {initiative_lijst[index]["NAAM"]}: {initiative_lijst[index]["AC"]}')
    print()

def edit_ac(initiative_lijst) -> dict[dict]:
    """Past de armor class van een initative entry aan."""
    index :int = kies_entry_in_initiative_lijst(initiative_lijst)

    print()
    print(f'De huidige armor class van {initiative_lijst[index]["NAAM"]}: {initiative_lijst[index]["AC"]}')
    print()

    verander_ac_hoeveelheid : int = get_valid_number(
        f'Wat wil je dat de armor class van {initiative_lijst[index]["NAAM"]} wordt ? ',
        "De nieuwe armor class moet een nummer zijn, bv: 10"
    )

    initiative_lijst[index]["AC"] = verander_ac_hoeveelheid

    return initiative_lijst

def delete_entry(initiative_lijst) -> dict[dict]:
    """Verwijdert een geslecteerde entry uit de initative."""
    index :int = kies_entry_in_initiative_lijst(initiative_lijst)

    if input(f'Wil je {initiative_lijst[index]["NAAM"]} verwijderen uit initiative ? y/n ').lower() == "n":
        return

    print(f'{initiative_lijst[index]["NAAM"]} is verwijdert')

    del initiative_lijst[index]

    return initiative_lijst

def save_initiative_lijst(initiative_lijst) -> None:
    """Slaat de huidige initative op als een json bestand."""
    bestand_naam :str = input("In welk bestand wil je de initiative opslaan: ")

    with open(bestand_naam, "w", encoding="UTF-8") as f:
        f.write(json.dumps(initiative_lijst))

def load_initiative_lijst() -> dict:
    """Vormt een initiative dict uit het ingegeven json bestand."""
    bestand_naam = input("Uit welk bestand wil je de initiative laden: ")

    try:
        with open(bestand_naam, "r", encoding="UTF-8") as f_in:
            initiative_lijst = json.load(f_in)

        print(f"Initiative lijst succesvol geladen uit {bestand_naam}.")

        return initiative_lijst

    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestand_naam}' is niet gevonden.")

    except json.JSONDecodeError:
        print(f"Fout: Het bestand '{bestand_naam}' bevat ongeldig JSON.")

    return {}
