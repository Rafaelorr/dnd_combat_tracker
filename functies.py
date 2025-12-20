import json

def get_valid_number(prompt, error_message) -> int:
  """Get a valid integer input."""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print(error_message)

def maak_lijst_van_initiative_lijst(initiative_lijst:dict) -> list:
  lijst : list = list(initiative_lijst.keys())
  lijst.sort(reverse=True)

  return lijst

def kies_entry_in_initiative_lijst(initiative_lijst:dict) -> int:
  lijst = maak_lijst_van_initiative_lijst(initiative_lijst)

  for item in lijst:
    print(f'{int(lijst.index(item))}. {initiative_lijst[item]["NAAM"]}')

  gekozen_entry :int = lijst[get_valid_number("Welke wil je bewerken? ","De entry die kiest moet een nummer zijn, bv:0")]

  return gekozen_entry

def help():
  print("""Commands:
    help: Toont alle commands
    exit: Stopt het programma
    list: Toont alle invatie entries in volgorde
    add: Voegt een invatie entry toe
    delete: Verwijdert een invatie entry
    show: Toont de hit points en armor class van een invatie entry
    edit_hp: Verandert de hit points van een invatie entry
    edit_ac: Verandert de armor class van een invatie entry
    clear: Wist het scherm""")

def add(initiative_lijst:dict) -> dict[dict]:    
  def get_valid_invatie() -> int | None:
    """Get a valid initiative value that doesn't already exist."""
    while True:
      invatie = get_valid_number("Invatie van de nieuwe entry: ","De invatie van de nieuwe entry moet een nummer zijn, bv: 10")
                
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
    
    
    # Get initiative (return None if user cancels)
  invatie = get_valid_invatie()
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
  lijst = maak_lijst_van_initiative_lijst(initiative_lijst)
  for item in lijst:
    print(f'{item}. {initiative_lijst[item]["NAAM"]}')

def edit_hp(initiative_lijst:dict) -> dict[dict]:
  gekozen_entry :int = kies_entry_in_initiative_lijst(initiative_lijst)

  print()
  print(f'De huidige hp van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["HP"]}')
  verander_hp_hoeveelheid :int = get_valid_number(f'Hoeveel wil je aan de hit points van {initiative_lijst[gekozen_entry]["NAAM"]} toevoegen ? ',"De hoeveelheid die je aan de hit points wilt toevoegen moet een nummer zijn, bv: 12")
  print()

  initiative_lijst[gekozen_entry]["HP"] += verander_hp_hoeveelheid

  return initiative_lijst

def show(initiative_lijst:dict) -> None:
  gekozen_entry :int = kies_entry_in_initiative_lijst(initiative_lijst)

  print()
  print(f'De hit points van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["HP"]}')
  print(f'De armor class van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["AC"]}')
  print()

def edit_ac(initiative_lijst) -> dict[dict]:
  gekozen_entry :int = kies_entry_in_initiative_lijst(initiative_lijst)

  print()
  print(f'De huidige armor class van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["AC"]}')
  verander_ac_hoeveelheid : int = get_valid_number(f'Wat wil je dat de armor class van {initiative_lijst[gekozen_entry]["NAAM"]} wordt ? ',"De nieuwe armor class moet een nummer zijn, bv: 10")
  print()

  initiative_lijst[gekozen_entry]["AC"] = verander_ac_hoeveelheid

  return initiative_lijst

def delete_entry(initiative_lijst) -> dict[dict]:
  gekozen_entry :int = kies_entry_in_initiative_lijst(initiative_lijst)

  if input(f'Wil je {initiative_lijst[gekozen_entry]["NAAM"]} verwijderen uit initiative ? y/n ').lower() == "n":
    return
  
  print(f'{initiative_lijst[gekozen_entry]["NAAM"]} is verwijdert')

  del initiative_lijst[gekozen_entry]

  return initiative_lijst

def save_initiative_lijst(initiative_lijst) -> None:
  bestand_naam :str = input("In welk bestand wil je de initiative opslaan: ")

  with open(bestand_naam, "w") as f:
    f.write(json.dumps(initiative_lijst))

def load_initiative_lijst() -> dict:
    bestand_naam = input("Uit welk bestand wil je de initiative laden: ")
    
    try:
        with open(bestand_naam, "r") as f_in:
            initiative_lijst = json.load(f_in)  # use json.load for direct JSON object
        print(f"Initiative lijst succesvol geladen uit {bestand_naam}.")
        print(initiative_lijst)
        return initiative_lijst
    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestand_naam}' is niet gevonden.")
    except json.JSONDecodeError:
        print(f"Fout: Het bestand '{bestand_naam}' bevat ongeldig JSON.")
    return {}  # return een lege dict als er een fout is