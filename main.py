
from funkce import *

inventory = []
credit = 200

shop_items = {
    "laserová mačeta": 120,
    "kuře na kari v kapsli": 30,
    "kokainový stimpack": 80
}

        
print("""Nacházíš se uprostřed rušných ulic Lunar City, kde tě krom slunce pálí na kůži i výpary z četných pruduchů z budouv,
výfuků ze silných vznášedel a venkovních elektrických stanic.""")
print("""Míhající se světla a vjemy velkoměsta tě na chvíli ohromily natolik, že jsi na chvíli zapomněl, jak se vlastně jmenuješ.
Bylo by dobré si to připomenout.""")
name = input("Pod jakým jménem tě mají znát obyvatelé Lunar City? ")

print(f"""Od chvíle, co tvé motorkářské boty vstoupili do města, tě tvé náhodné i
účelné známosti znají pod jménem {name}. Bylo by dobré, kdyby to prozatím tak zůstalo.""")
print("""Lunar City nabízí spousta zajímavých příležitostí. Stojíš na náměstí Sunrise Plaza
a světla neonů se odráží od tvé terénní motorky.""")
print("Před tebou svítí výloha s nějrůznějšími zajímavými předměty, které nejnovější technologie nabízí.")
print("Nalevo tě lákají svůdné úsměvy a rudá záře červených 'výloh' s tanečnicemi. Všechny koukají tvým směrem.")
print("Napravo je bar se zářícím nápisem 'UNDERGROUND' s podtitulem 'Pro somráky tu máme držkový cocktail'.")

print("=" * 40)
print("Kam to bude jako první?")
print("1 – Brodel")
print("2 – Bar")
print("3 – Obchod")
print("=" * 40)
while True:
    roam = input("> ")

    if roam == "1":
        print(f"""Bordel jsem ještě nenaprogramoval, ale je hezky vidět, na co myslíš jako první :-)
neboj {name}, všechno bude! \nKam dál?""")
    elif roam == "2":
        print("Bar je prozatím úplně zavřený, ještě jsem tam nic nanapsal. Snad se brzy otevře. \nKam dál?")
    elif roam == "3":
        print("""Vcházíš do obchodu, kde to s otevřením dveří roztomile zacinká. Kdy by to byl řekl, že v roce
2089 se budou ještě používat kovové zvonky. Staromilské, ale roztomilé. Zpoza rohu se vynoří postava.""")
        break
    else:
        print("Zmateně stojíš a nemůžeš se rozhodnout. Pár děveček na tebe mezitím pokřikuje.")

#VSTUP DO OBCHODU
        
print("=" * 40)
print(f"Obchodník: Vítejte, vítejte {name}! To je ale milé překvapení.")
print("1 – Odkud víte jak se jmenuju?")
print("2 – Zdravím, pěkné vetešnictví tu vedete.")
print("3 – Otočit se a odejít")
print("=" * 40)

while True:
    seller_answer = input("> ")

    if seller_answer == "1":
        print("Obchodnik: Vaše jméno není úplně neznáme a navíc... mám pár ptáčků, kteří rádi cvrlikají.")
        print(f"Obchodník: V každém případě, co Vám, {name}, můžu nabídnout?")
        break

    elif seller_answer == "2":
        print("Obchodník: Jaké vetešnictví?! Mám tady prvotřídní zboží od zbraní, přes stimulanty až po sběratelské kousky!")
        print(f"Obchodník: V každém případě, co Vám, {name}, můžu nabídnout?")
        break

    elif seller_answer == "3":
        print("Jen co jsi do obchodu přišel, už z něj zase odcházíš. Na tohle nemáš čas.")
        print("A já neměl čas dodělat zbytek, takže... --KONEC HRY--")
        exit()

    else:
        print("Nevíš co říct. Trapná chvilka, kdy na sebe v tichosti koukáte.")

#SAMOTNÝ OBCHOD - TRANSAKCE
print("\nObchodník vysune z pultu platformu s nápisem 'horké zboží' a s očekáváním se podívá na tebe.")
for item, price in shop_items.items():
    print(f"– {item} ({price} kreditů)")

print(f"V tvém zorném poli zabliká vpravo nahoře stav tvého konta – {credit} kreditů.")
print("Napiš název položky, kterou chceš koupit. Jakmile budeš chtít skončit, napiš 'konec'")

while True:
    choice = input("> ").strip()

    if choice.lower() == "konec":
        break
    elif choice in shop_items:
        price = shop_items[choice]
        if credit >= price:
            credit -= price
            inventory.append(choice)
            print("*" * 40)
            print(f"Koupil jsi {choice}. Zbývá ti ještě {credit} kreditů.")
            print("*" * 40)
            print("Co to bude dál?")
        else:
            print("Obchodník: Na tohle nemáte dost kreditů!")
    else:
        print("Obchodník: Tuhle položku tu nemám. Vybírejte z toho co vidíte.")

print("\nTvé aktuální vybavení:")
for item in inventory:
    print(f"– {item}")
print(f"Zbývající počet kreditů: {credit}")
print("-" * 40)

#KONEC TRANSAKCE - POKRAČOVÁNÍ DIALOGU

print(f"Obchodník: Takže {name}, byznys máme za sebou, ale je něco, co si člověk jen tak nekoupí a to je přátelské poklábosení. No, nemám pravdu?")
print("Obchodník: Ačkoli mám kontakty po celém městě, proč si nepohovořit jenom tak mezi čtyřma očima?")
print("\nChvíli se zamyslíš nad jeho slovy a zároveň přemýšlíš, co bys mu na to tak řekl. Co o sobě vlastně víš?")

profession = vyber_povolani()

print(f"A pak sis vzpomněl. Jsi {profession}, ale chceš mu to říct? Je to obchodník a informace jsou přeci jen také komoditou.")
print("Jako kdybys ty sám tohle už dávno nevěděl.")
print("=" * 40)
print("Co mu odpovíš?")
print("1 – Hmmm, proč ne. Neznáš nějaké drby z okolí?")
print("2 – Nevíš o nějaké práci?")
print("3 – Řekni mu něco o své profesi a osobním životě.")
print("4 – Mám co jsem chtěl. Sbohem.")
print("=" * 40)

while True:
    answer_seller = input("> ")
        
    if answer_seller == "1":
        print("""Obchodník: Hehe, chceš mít přehled, co? Na tom není nic špatného, a když jsme u toho, já na tenhle druh informací nejsem zrovna nejlepší spojkou.
Ale jen naivkové si myslí, že bordel je jen o tělesných rozkoších. Jasně, vydělává se tam nejstarším řemeslem, ale kde kdo si tam pustí
hubu na špacír, když vidí nahou ženskou. Obzvláště, když ti slíbí, že udělá COKOLI. Chceš mít ale skutečně přehled? Najdi Tashu.
Snad se nějak... domluvíte, hehe.""")
        print("=" * 40)
        print("1 – A co bar? Tam se nic nedozvím? Chlast taky rozvazuje jazyk.")
        print("2 – Heh, tvý ptáčci toho ví tak málo?")
        print("3 – Ok, díky, to mi stačí.")
        print("=" * 40)
        while True:
            gossip = input("> ")
            if gossip == "1":
                print("""Obchodník: Tam blábolí kdejaký vochlasta a navíc se tam spíše dostaneš do problémů. Nikdy nevíš, do koho zrovna vrazíš a když máš smůlu, je to vo hubu.
Vím, kam tím míříš, ale jestli hledáš trochu mazanější způsob, jak na někoho něco skutečně najít, vzal bych to radši přes bordel.""")
            elif gossip == "2":
                print("""Obchodník: Rejpal, co? Tak hele, jsem obchodník a zajímá mě jen určitá klientela. Nejsem žádný baron ani něčí grandfotr, abych věděl o
kdejakém hovnu. Takže jestli ti není dobrý to, co vím, tak si to zjisti sám.""")
                print("*" * 40)
                reputation_change("obchodnik", -10)
                print("*" * 40)
            elif gossip == "3":
                print("Obchodník: V pohodě, víš kam jít.")
                print("=" * 40)
                print("2 – Nevíš o nějaké práci?")
                print("3 – Řekni mu něco o své profesi a osobním životě.")
                print("4 – Mám co jsem chtěl. Sbohem.")
                print("=" * 40)
                break
            else:
                print("Obchodník na tebe dál kouká, jestli k tomu chceš něco říct.")
    elif answer_seller == "2":
            print("Obchodník: Jasně, to tě nasměruju spíš do baru. Tam se shází podivná sebranka, ale všichni to nejsou úplná hovoda. I přesto doporučuji obezřetnost.")
    elif answer_seller == "3":
            print(f"""Ty: Do Lunar City jsem nepřišel náhodou. Pracuju jako {profession} pro jednoho klienta. Pocházím z pustiny, takže motivaci není těžké uhodnout.
Lepší život. Všechno je lepší, než tam venku.""")
            print("Obchodník: Hmmm, děkuji za úpřímnost a důvěru.")
            print("*" * 40)
            reputation_change("obchodnik", 10)
            print("*" * 40)
    elif answer_seller == "4":
            print("Obchodník: Dobrá, snad brzy na shledanou.")
            break
    else:
            print("Obchodník čeká na tvoji odpoveď. Trapné ticho roste.")
        
print("@" * 40)
print("Odcházíš z obchodu do rušné ulice.")
        






