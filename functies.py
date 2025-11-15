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

def add(invaties:dict) -> dict:
    # kies nieuw invatie om toe te voegen
    try:
      invatie : int = int(input("Invatie van de nieuwe entry: "))
      if invaties.get(invatie):
         print("Gekozen invatie bestaat al")
         if input("Kies je een ander invatie? y/n").lower() == "y":
            invatie : int = int(input("Invatie van de nieuwe entry: "))
         else:
            return
    except:
      print("Type de invatie van de nieuwe entry als een nummer bv:1")
      invatie : int = int(input("Invatie van de nieuwe entry: "))
      if invaties.get(invatie):
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
    invaties.setdefault(invatie, {})
    
    invaties[invatie]["NAAM"] = naam
    invaties[invatie]["HP"] = hp
    invaties[invatie]["AC"] = ac

    return invaties