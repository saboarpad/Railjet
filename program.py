#Információk

print("\x1B[3m" + "\nIKT Python programozás projekt feladat (vonat foglalás)" + "\x1B[0m")
print("\033[1m" + '\033[96m' + "Csoport: Kánnár Márton, Szabó Árpád, (Menyhárt Alex?)" + "\033[0m" + '\033[0m')
print('\033[93m' + '-'*60, "\n" + '\033[0m')
print("\033[1m" + "BUDAPEST ---> BÉCS" + "\033[0m")

#Adatszerkezetek és a változók létrehozása

kocsi_reggel = [['O']*15,['O']*15,['O']*15,['O']*15]
kocsi_deli = [['O']*15,['O']*15,['O']*15,['O']*15]
kocsi_este = [['O']*15,['O']*15,['O']*15,['O']*15]
napszak = None
oszlop = None
sor = None
foglalasok_szama = None
nev = None
foglalasok = []
nev_foglalas = {}
sikertelen = 0
sikeres = 0

#Bekeres
def beker(i : int):
    print(f"{i+1}. hely foglalása")
    global nev
    nev = input("Adja meg a nevét! ")
    napszak = input("Adja meg mikor szeretne indulni?(Reggel\Délben\Este)")
    while  napszak !="Reggel" and napszak !="Este" and napszak !="Délben":
        napszak = input("Hibás indulási időpont\nKérjük a megadott listából válasszon\nReggel\nDélben\nEste\n")

    while True:
        try:
            oszlop = int(input("Kérem, adja meg melyik oszlopban szeretne űlni (1~4)!:"))
            if 1 <= oszlop <= 4:
                break  
            else:
                print("Nincs ilyen oszlop!\n Adjon meg egy létező oszlopot! (1~4)")
        except ValueError:
            print("Nincs ilyen oszlop!\n Adjon meg egy létező oszlopot! (1~4)")

    while True:
        try:
            sor = int(input("Kérem, adja meg melyik sorban szeretne űlni (1~15)!:"))
            if 1 <= sor <= 15:
                break  
            else:
                print("Nincs ilyen sor!\nAdjon meg egy létező sort! (1~15)")
        except ValueError:
            print("Nincs ilyen sor!\nAdjon meg egy létező sor! (1~15)")
    if napszak =='Reggel':
        if kocsi_reggel[oszlop-1][sor-1]=='X':
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            global sikertelen
            sikertelen += 1 
        else:
            print("Sikeres foglalás!")
            global sikeres
            sikeres += 1
            kocsi_reggel[oszlop-1][sor-1]='X'
            global nev_foglalas
            nev_foglalas = {
                'Név' : nev,
                'Indulás' : napszak,
                'Sor' : sor,
                'Oszlop' : oszlop,
            }
            global foglalasok
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}
    if napszak =='Délben':
        if kocsi_deli[oszlop-1][sor-1]=='X':
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            sikertelen += 1
        else:
            print("Sikeres foglalás!")
            sikeres += 1
            kocsi_deli[oszlop-1][sor-1]='X'
            nev_foglalas = {
                'Név' : nev,
                'Indulás' : napszak,
                'Sor' : sor,
                'Oszlop' : oszlop,
            }
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}
    if napszak =='Este':
        if kocsi_este[oszlop-1][sor-1]=='X':
            print("Sikertelen foglalás!\nA választott hely foglalt!")
            sikertelen +=1
        else:
            print("Sikeres foglalás!")
            sikeres += 1
            kocsi_este[oszlop-1][sor-1]='X'
            nev_foglalas = {
                'Név' : nev,
                'Indulás' : napszak,
                'Sor' : sor,
                'Oszlop' : oszlop,
            }
            foglalasok.append(nev_foglalas)
            nev_foglalas = {}


def bekeres_tobbszor():
    while True:
        try:
            foglalasok_szama = int(input("Adja meg hány helyet szeretne foglalni: "))
            if  0 < foglalasok_szama:
                break  
            else:
                print("Legalább egy helyet kell foglalnia!\nAdja meg újra hány helyet szeretne foglalni! ")
        except ValueError:
            print("Kérjük a foglalni kívánt helyek számát egész számban adja meg!")
    for i in range(foglalasok_szama):
        beker(i)

bekeres_tobbszor()
bekeres_folytatasa = input("Szeretne még helyeket foglalni? (Igen/Nem) ")
if bekeres_folytatasa == "Igen" or bekeres_folytatasa == "igen":
    bekeres_tobbszor() 
