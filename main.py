import os
import sys
from functies import help_cli, toon_alle_entries, add, show, \
    edit_hp, edit_ac, delete_entry, save_initiative_lijst, load_initiative_lijst

initiative_lijst :dict = {}

if __name__ == "__main__":
    print("DnD combat tracker")
    print("Typ 'help' voor een lijst van alle commands")
    while True:
        command = input(": ").lower()
        if command == "exit":
            sys.exit(0)

        elif command == "list":
            toon_alle_entries(initiative_lijst)

        elif command == "add":
            add(initiative_lijst)

        elif command == "delete":
            delete_entry(initiative_lijst)

        elif command == "show":
            show(initiative_lijst)

        elif command == "edit_hp":
            edit_hp(initiative_lijst)

        elif command == "edit_ac":
            edit_ac(initiative_lijst)

        elif command == "save":
            save_initiative_lijst(initiative_lijst)

        elif command == "load":
            initiative_lijst = load_initiative_lijst()

        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif command == "help":
            help_cli()

        print("Invalid command")
