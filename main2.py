import random

vihollisen_hp = 10
pelaajan_hp = 10

def vuorot():
    randomi=random.randint(0,1)
    while True:
        if randomi==1:
            print()
            print("Pelaajan vuoro")
            valinta1=input("Hyökkäätkö vai juoksetko karkuun?: h = hyökkää, j = juokse ")
            if valinta1=="h":
                hyökkäys()
                if vihollisen_hp==0:
                    voittaminen()
                    break

            elif valinta1=="j":
                randomi=random.randint(0,1)
                if randomi==1:
                    print("Pääsit karkuun")
                    break
                else:
                    print("Älä ole pelkuri")
                    print("Pelaajan HP:", str(pelaajan_hp))
                    if pelaajan_hp==0:
                        kuoleminen()
                        break
            else:
                print("Tuo ei ole komento")
                    
        else:
            print("Vihollisen vuoro")
            valinta2=input("Puolustatko vai juoksetko karkuun?: p = puolusta, j = juokse ")
            if valinta2=="p":
                puolustus()
                if pelaajan_hp==0:
                    kuoleminen()
                    break

            elif valinta2=="j":
                if randomi==1:
                    print("Onnistuit pakenemaan")
                    break
                else:
                    print("Älä ole pelkuri")
                    print("Pelaajan HP:", str(pelaajan_hp))
                    if pelaajan_hp==0:
                        kuoleminen()
                        break
            else:
                print("Tuo ei ole komento")
       
        if randomi==1:
            randomi=0
        else:
            randomi=1

def hyökkäys():
    randomi=random.randint(0,1)
    if randomi==1:
        vihollisen_hp = vihollisen_hp - 1
        print("Hyökkäys onnistui")
        print("Vihollisen HP:", str(vihollisen_hp))
    else:
        print("Hyökkäys epäonnistui")

def puolustus():
    randomi=random.randint(0,1)
    if randomi==1:
        pelaajan_hp = pelaajan_hp - 1
        print("Puolustus epäonnistui")
        print("Pelaajan HP:", str(pelaajan_hp))
    else:
        print("Onnistuit torjumaan hyökkäyksen")

def kuoleminen():
    if pelaajan_hp==0:
        print("Kuolit viholliselle")
        pelaajan_hp = pelaajan_hp - 1

def voittaminen():
    print("Tapoit vihollisen")
    print("Pelaajan HP:", str(pelaajan_hp))

def päädyit_taisteluun():
    print("Päädyit taisteluun!")
    print("Vihollisen HP:", str(vihollisen_hp))
    print("Pelaajan HP:",str(pelaajan_hp))
    vuorot()

testi=str(input())
if testi == "t":
    päädyit_taisteluun()
