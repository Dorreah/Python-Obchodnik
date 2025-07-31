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

def reputation_change(char_name, rep_change):
    reputation_system[char_name] += rep_change
    if rep_change > 0:
        print(f"--Reputace s {char_name} vzrostla o {rep_change}--")
    elif rep_change < 0:
        print(f"--Reputace s {char_name} klesla o {abs(rep_change)}--")
    else:
        print(f"--Reputace s {char_name} zůstává stejná--")
    print(f"Aktuální reputace: {reputation_system[char_name]}")
