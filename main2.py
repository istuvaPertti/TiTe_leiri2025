import random

randomi=random.randint(0,1)

pelaajan_hp=10
vihollisen_hp=10

def päädyit_taisteluun():
    print(pelaajan_hp)
    print("Päädyit taisteluun!")
    while True:
        print("Pelaajan HP: " + str(pelaajan_hp))
        print("Vihollisen HP: " + str(vihollisen_hp))
        valinta=str(input("hyökkää: h, puolusta: p, juokse: j "))
        if valinta == "h":
            if randomi == 0:
                vihollisen_hp=vihollisen_hp - 1
                print("Onnistunut hyökkäys")
                if vihollisen_hp == 0:
                    print("Vihollinen tuhottu")
                    pelaajan_hp=pelaajan_hp + 1
                    break
            else:
                print("Vihollinen torjui hyökkäyksesi")
        elif valinta == "p":
            if randomi == 0:
                print("Hyökkäys torjuttu onnistuneesti")
            else:
                pelaajan_hp=pelaajan_hp - 1
                print("Olit liian hidas")
                if pelaajan_hp == 0:
                    print("Kuolit viholliselle")
                    print("Jotenkin taisit kuitenkin syntyä uudelleen")
                    pelaajan_hp=pelaajan_hp +10
                    break
        elif valinta == "j":
            if randomi == 0:
                print("Pääsit pakenamaan viholliselta")
                break
            else:
                print("Älä ole pelkuri")
        else:
            print("Tuo ei ole komento")

testi=str(input())
if testi == "t":
    päädyit_taisteluun()