import random

vihollisen_hp=10
pelaajan_hp=10

def vuorot():
    random=random.randint(0,1)
    while True:
        if random==1:
            print()
            print("Pelaajan vuoro")
            valinta1=input("Hyökkäätkö vai juoksetko karkuun?: h = hyökkää, j =juokse")
            if valinta1=="h":
                hyökkäys()
                if vihollisen_hp==1:
                    voittaminen()
                    break

            else:
                random=random.randint(0,1)
                if random==1:
                    print("Pääsit karkuun")
                    break
                else:
                    pelaajan_hp-=1
                    print("Älä ole pelkuri")
                    print("Pelaajan HP:", pelaajan_hp)
                    if pelaajan_hp==0:
                        kuoleminen()
                        break

        else:
            print("Vihollisen vuoro")
            valinta2=input("Puolustatko vai juoksetko karkuun?: p = puolusta, j = juokse")
            if valinta2=="p":
                puolustus()
            else:
                random=random.randint(0,1)
                if random==1:
                    print("Onnistuit pakenemaan")
                    break
                else:
                    print("Älä ole pelkuri")
                    print("Pelaajan HP:", pelaajan_hp)
                    if pelaajan_hp==0:
                        kuoleminen()
                        break
       
        if random==1:
            random=0
        else:
            random=1

def hyökkäys():
    random=random.randint(0,1)
    if random==1:
        vihollisen_hp-=1
        print("Hyökkäys onnisui")
        print("Vihollisen HP:", vihollisen_hp)
    else:
        print("Hyökkäys onnisui")

def puolustus():
    random=random.randint(0,1)
    if random==0:
        pelaajan_hp-=1
        print("Puolustus epäonnistui")
        print("Pelaajan HP:", pelaajan_hp)
        if pelaajan_hp==0:
            kuoleminen()
    else:
        print("Onnistuit torjumaan hyökkäyksen")

def kuoleminen():
    print("Kuolit viholliselle")
    pelaajan_hp+=10

def voittaminen():
    print("Tapoit vihollisen")
    pelaajan_hp+=1
    print("Sait yhden HP:n lisää")
    print("Pelaajan HP:", pelaajan_hp)

def päädyit_taisteluun():
    print("Päädyit taisteluun!")
    print("Vihollisen HP:", vihollisen_hp)
    print("Pelaajan HP:", pelaajan_hp)
    vuorot()

testi=str(input())
if testi == "t":
    päädyit_taisteluun()
