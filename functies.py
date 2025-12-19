def help():
    print("""Commands:
          Help
            Toont alle commands
          Exit
            Stopt het programma
          List
            Toont alle invatie entries in volgorde
          Add
            Voegt een invatie entry toe
          Delete
            Verwijdert een invatie entry
          Show
            Toont de hit points en armor class van een invatie entry
          Edit_hp
            Verandert de hit points van een invatie entry
          Edit_ac
            Verandert de armor class van een invatie entry
          """)

def add(initiative_lijst:dict) -> dict:
    # kies nieuw invatie om toe te voegen
    try:
      invatie : int = int(input("Invatie van de nieuwe entry: "))
      if initiative_lijst.get(invatie):
         print("Gekozen invatie bestaat al")
         if input("Kies je een ander invatie? y/n").lower() == "y":
            invatie : int = int(input("Invatie van de nieuwe entry: "))
         else:
            return
    except:
      print("Type de invatie van de nieuwe entry als een nummer bv:1")
      invatie : int = int(input("Invatie van de nieuwe entry: "))
      if initiative_lijst.get(invatie):
         print("Gekozen invatie bestaat al")
         if input("Kies je een ander invatie? y/n").lower() == "y":
            invatie : int = int(input("Invatie van de nieuwe entry: "))
         else:
            return
    
    # kies naam
    naam : str = input("Naam van de nieuwe entry: ")
    if naam.strip() == "":
       print("TIP: Geef de nieuw invatie entry een naam")
       naam : str = input("Naam van de nieuwe entry: ")
    
    # kies hit points nieuwe invatie entry
    try:
      hp : int = int(input("Hit points van de nieuwe entry: "))
    except:
      print("Type de hit points van de nieuwe entry als een nummer bv:1")
      hp : int = int(input("Hit points van de nieuwe entry: "))

    # kies armor class nieuwe invatie entry
    try:
      ac : int = int(input("Armor class van de nieuwe entry: "))
    except:
      print("Type de armor class van de nieuwe entry als een nummer bv:1")
      ac : int = int(input("Armor class van de nieuwe entry: "))

    # voeg nieuwe entry toe aan de lijst
    initiative_lijst.setdefault(invatie, {})
    
    initiative_lijst[invatie]["NAAM"] = naam
    initiative_lijst[invatie]["HP"] = hp
    initiative_lijst[invatie]["AC"] = ac

    return initiative_lijst

def toon_alle_entries(initiative_lijst:dict) -> None:
  lijst : list = list(initiative_lijst.keys())
  lijst.sort(reverse=True)
  for item in lijst:
     print(f'{item}. {initiative_lijst[item]["NAAM"]}')

def edit_hp(initiative_lijst:dict) -> dict:
  lijst : list = list(initiative_lijst.keys())
  lijst.sort(reverse=True)
  for item in lijst:
    print(f'{int(lijst.index(item))}. {initiative_lijst[item]["NAAM"]}')

  gekozen_entry :int = int(input("Welke wil je bewerken? "))
  gekozen_entry :int = lijst[gekozen_entry]

  print()
  print(f'De huidige hp van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["HP"]}')
  verander_hp_hoeveelheid : int = int(input(f'Hoeveel wil je aan de hp van {initiative_lijst[gekozen_entry]["NAAM"]} toevoegen ? '))
  print()

  initiative_lijst[gekozen_entry]["HP"] += verander_hp_hoeveelheid

  return initiative_lijst

def show(initiative_lijst:dict) -> None:
  lijst : list = list(initiative_lijst.keys())
  lijst.sort(reverse=True)
  for item in lijst:
    print(f'{int(lijst.index(item))}. {initiative_lijst[item]["NAAM"]}')

  gekozen_entry :int = int(input("Van welke wil je de hp en ac zien? "))
  gekozen_entry :int = lijst[gekozen_entry]

  print()
  print(f'De hit points van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["HP"]}')
  print(f'De armor class van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["AC"]}')
  print()

  return

def edit_ac(initiative_lijst):
  lijst : list = list(initiative_lijst.keys())
  lijst.sort(reverse=True)
  for item in lijst:
    print(f'{int(lijst.index(item))}. {initiative_lijst[item]["NAAM"]}')

  gekozen_entry :int = int(input("Welke wil je bewerken? "))
  gekozen_entry :int = lijst[gekozen_entry]

  print()
  print(f'De huidige armor class van {initiative_lijst[gekozen_entry]["NAAM"]}: {initiative_lijst[gekozen_entry]["HP"]}')
  verander_ac_hoeveelheid : int = int(input(f'Wat wil je dat de ac van {initiative_lijst[gekozen_entry]["NAAM"]} wordt ? '))
  print()

  initiative_lijst[gekozen_entry]["AC"] = verander_ac_hoeveelheid

  return initiative_lijst