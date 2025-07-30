def vyber_povolani():
    print("Zvol si své povolání:")
    print("1 - Válečník")
    print("2 - Kouzelník")
    print("3 - Zloděj")
    
    volba = input("Tvoje volba: ")
    
    if volba == "1":
        return "Válečník"
    elif volba == "2":
        return "Kouzelník"
    elif volba == "3":
        return "Zloděj"
    else:
        return "Neznámý tulák"

def pozdrav(jmeno):
    print("Zdravím vás, vážený pane " + jmeno + "!")

def mas_dost_penez(mas, cena):
    if mas >= cena:
        print("Skvělé! Obchodovat s vámi je radost.")
        print("–– Skořice a Viagra přidána do inventáře ––")
    else:
        print("Je mmi líto pane, ale nemáte na to dost zlatých.")
