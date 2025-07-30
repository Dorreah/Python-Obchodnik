
from funkce import *
        
penezenka = {"mas": 50}
mas = penezenka["mas"] 
pozdrav("Davide")
obchod = input("""Mohu nabídnout jedno z našich nejlepších koření?
Po takovém život bude chutnat lépe! A nebo tu mám pro vás tyhle plody,
po kterých žádná noc nebude jako předtím. Obojí za skvělých 50 zlatých.
Nabídka jen pro vás, pane. Přijmete ji? (ano/ne) """)

if obchod.lower() == "ano":
    mas_dost_penez(mas, 50)
else:
    print("Tak nic no.")
    
print("Poslyšte ale, ještě jsem o vás moc neslyšel. Co ty jste vůbec zač?")

povolani = vyber_povolani()
print(f"""Aaaaa, vážený {povolani}!
Přeji vám tedy mnoho štěstí.""")
