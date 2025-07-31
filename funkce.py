def vyber_povolani():
    print("Zvol si své povolání:")
    print("1 - Nájemný žoldák")
    print("2 - Hacker")
    print("3 - Plíživec")
    
    volba = input("Tvoje volba: ")
    
    if volba == "1":
        return "Nájemný žoldák"
    elif volba == "2":
        return "Hacker"
    elif volba == "3":
        return "Plíživec"
    else:
        return "Pan tajemný"

