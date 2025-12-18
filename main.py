from functies import help, toon_alle_entries, add, show, edit_hp, edit_ac

invaties :dict = {}

if __name__ == "__main__":
    print("DnD combat tracker")
    print("Typ 'help' voor een lijst van alle commands")
    while True:
        command = input(": ").lower()
        if command == "exit":
            exit()
        
        if command == "list":
            toon_alle_entries(invaties)
            continue
        
        if command == "add":
            add(invaties)
            continue

        if command == "delete":
            pass
            continue

        if command == "show":
            show(invaties)
            continue

        if command == "edit_hp":
            edit_hp(invaties)
            continue

        if command == "edit_ac":
            edit_ac(invaties)
            continue

        if command == "help":
            help()
            continue

        print("Invalid command")
