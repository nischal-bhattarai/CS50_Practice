name =input("Whats your Name ? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco" | "Snape":
        print("Slytherin")
    case _:
        print("Who?")
            