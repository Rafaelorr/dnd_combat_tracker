from functies import *
invaties :dict = {}

if __name__ == "__main__":
    print("DnD combat tracker")
    print("Typ 'help' voor een lijst van alle commands")
    while True:
        command = input(": ")
        if command.lower() == "help":
            help()
        elif command.lower() == "exit":
            exit()
        elif command.lower() == "list":
            toon_alle_entries(invaties)
        elif command.lower() == "add":
            add(invaties)
        elif command.lower() == "delete":
            pass
        elif command.lower() == "show":
            pass
        elif command.lower() == "edit_hp":
            edit_hp(invaties)
        elif command.lower() == "edit_ac":
            pass
        else:
            print("Invalid command")
            print("Typ 'help' voor een lijst van alle commands")