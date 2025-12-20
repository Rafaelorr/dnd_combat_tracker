import os
from functies import help, toon_alle_entries, add, show, edit_hp, edit_ac

initiative_lijst :dict = {}

if __name__ == "__main__":
    print("DnD combat tracker")
    print("Typ 'help' voor een lijst van alle commands")
    while True:
        command = input(": ").lower()
        if command == "exit":
            exit()
        
        if command == "list":
            toon_alle_entries(initiative_lijst)
            continue
        
        if command == "add":
            add(initiative_lijst)
            continue

        if command == "delete":
            pass
            continue

        if command == "show":
            show(initiative_lijst)
            continue

        if command == "edit_hp":
            edit_hp(initiative_lijst)
            continue

        if command == "edit_ac":
            edit_ac(initiative_lijst)
            continue

        if command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if command == "help":
            help()
            continue

        print("Invalid command")
