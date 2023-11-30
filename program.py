# Információk
print(
    "\x1B[3m" + "\nIKT Python programozás projekt feladat (vonat foglalás)" + "\x1B[0m"
)
print(
    "\033[1m"
    + "\033[96m"
    + "Csoport: Kánnár Márton, Szabó Árpád, (Menyhárt Alex?)"
    + "\033[0m"
    + "\033[0m"
)
print("\033[93m" + "-" * 60, "\n" + "\033[0m")
print("\033[1m" + "BUDAPEST ---> BÉCS" + "\033[0m")

import random
import json
import ast


# print("debug: tartalom adatszerkezet megnyitása/létrehozása után:\n")
# print(f"reggel: {kocsi_reggel}\n")
# print(f"délben: {kocsi_del}\n")
# print(f"este: {kocsi_este}\n")

# Adatszerkezetek és a változók létrehozása
napszak = None
oszlop = None
sor = None
foglalasok_szama = None
nev = None
foglalasok = []
nev_foglalas = {}
sikertelen = 0
sikeres = 0

# Meglévő foglalások kiolvasása JSON fájlból
try: 
    with open('foglalasok.txt', 'r', encoding='UTF-8') as f:
        foglalasok = json.load(f)
        f.close()
except:
    foglalasok = []

kocsi_reggel = list()
kocsi_del = list()
kocsi_este = list()

# Meglévő adatszerkezet kiolvasása az adatbázisból vagy új adatbázis létrehozása
adatok = list()
try:
    with open("./db.txt", "r") as db:
        for rekord in db:
            adatok.append(rekord.strip())
        kocsi_reggel = ast.literal_eval(adatok[0])
        kocsi_del = ast.literal_eval(adatok[1])
        kocsi_este = ast.literal_eval(adatok[2])
        db.close()
except:
    kocsi_reggel = [["O"] * 15, ["O"] * 15, ["O"] * 15, ["O"] * 15]
    kocsi_del = [["O"] * 15, ["O"] * 15, ["O"] * 15, ["O"] * 15]
    kocsi_este = [["O"] * 15, ["O"] * 15, ["O"] * 15, ["O"] * 15]

# veletlen függvény
def szabade(napszak, oszlop, sor):
    if napszak == "Reggel":
        if kocsi_reggel[oszlop - 1][sor - 1] == "X":
            return 0
        else:
            return 1
    if napszak == "Délben":
        if kocsi_del[oszlop - 1][sor - 1] == "X":
            return 0
        else:
            return 1
    if napszak == "Este":
        if kocsi_este[oszlop - 1][sor - 1] == "X":
            return 0
        else:
            return 1
# Bekeres
def beker(i: int):
    print(f"{i+1}. hely foglalása")
    global nev
    nev = input("Adja meg a nevét! ")
    napszak = input("Adja meg mikor szeretne indulni?(Reggel\Délben\Este)")
    while napszak != "Reggel" and napszak != "Este" and napszak != "Délben":
        napszak = input(
            "Hibás indulási időpont\nKérjük a megadott listából válasszon\nReggel\nDélben\nEste\n"
        )

    veletlen = input("Szertne véletlendszerűen helyet foglalni? (igen = 1, nem = 0) ")
    if int(veletlen) == 1:
        szabad = 0
        while szabad != 1:
            roszlop = random.randint(1, 4)
            rsor = random.randint(1, 15)
            szabad = szabade(napszak, roszlop, rsor)
            oszlop = roszlop
            sor = rsor
        print(f"A kisorsolt hely: {sor}. sor, {oszlop}. oszlop. Jó utat {nev}!")

    else:
        while True:
            try:
                oszlop = int(
                    input("Kérem, adja meg melyik oszlopban szeretne ülni (1~4)!:")
                )
                if 1 <= oszlop <= 4:
                    break
                else:
                    print("Nincs ilyen oszlop!\n Adjon meg egy létező oszlopot! (1~4)")
            except ValueError:
                print("Nincs ilyen oszlop!\n Adjon meg egy létező oszlopot! (1~4)")

        while True:
            try:
                sor = int(input("Kérem, adja meg melyik sorban szeretne ülni (1~15)!:"))
                if 1 <= sor <= 15:
                    break
                else:
                    print("Nincs ilyen sor!\nAdjon meg egy létező sort! (1~15)")
            except ValueError:
                print("Nincs ilyen sor!\nAdjon meg egy létező sor! (1~15)")
    if napszak == "Reggel":
        if kocsi_reggel[oszlop - 1][sor - 1] == "X":
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            global sikertelen
            sikertelen += 1
        else:
            print("Sikeres foglalás!")
            global sikeres
            sikeres += 1
            kocsi_reggel[oszlop - 1][sor - 1] = "X"
            global nev_foglalas
            nev_foglalas = {
                "Név": nev,
                "Indulás": napszak,
                "Sor": sor,
                "Oszlop": oszlop,
            }
            global foglalasok
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}
    if napszak == "Délben":
        if kocsi_del[oszlop - 1][sor - 1] == "X":
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            sikertelen += 1
        else:
            print("Sikeres foglalás!")
            sikeres += 1
            kocsi_del[oszlop - 1][sor - 1] = "X"
            nev_foglalas = {
                "Név": nev,
                "Indulás": napszak,
                "Sor": sor,
                "Oszlop": oszlop,
            }
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}
    if napszak == "Este":
        if kocsi_este[oszlop - 1][sor - 1] == "X":
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            sikertelen += 1
        else:
            print("Sikeres foglalás!")
            sikeres += 1
            kocsi_este[oszlop - 1][sor - 1] = "X"
            nev_foglalas = {
                "Név": nev,
                "Indulás": napszak,
                "Sor": sor,
                "Oszlop": oszlop,
            }
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}

def bekeres_tobbszor():
    while True:
        try:
            foglalasok_szama = int(input("Adja meg hány helyet szeretne foglalni: "))
            if 0 < foglalasok_szama:
                break
            else:
                print(
                    "Legalább egy helyet kell foglalnia!\nAdja meg újra hány helyet szeretne foglalni! "
                )
        except ValueError:
            print("Kérjük a foglalni kívánt helyek számát egész számban adja meg!")
    for i in range(foglalasok_szama):
        beker(i)


bekeres_tobbszor()
bekeres_folytatasa = input("Szeretne még helyeket foglalni? (Igen/Nem) ")
if bekeres_folytatasa == "Igen" or bekeres_folytatasa == "igen":
    bekeres_tobbszor()

# print("debug: tartalom adatszerkezet kiírása előtt:\n")
# print(f"reggel: {kocsi_reggel}\n")
# print(f"délben: {kocsi_del}\n")
# print(f"este: {kocsi_este}\n")

# adatszerkezet mentése az adatbázisba
with open('foglalasok.txt', 'w', encoding='utf-8') as jegyek:
    json.dump(foglalasok, jegyek, ensure_ascii=False)
    jegyek.close()

with open("db.txt", "w", encoding="utf-8") as db:
    print(kocsi_reggel, file=db)
    print(kocsi_del, file=db)
    print(kocsi_este, file=db)
    db.close()