import random
import os
import main2


view_range = 16






def clear():
    os.system("cls"if os.name=="nt"else"clear")

def empty():
    pass

def treasure():
    pass

laatat = ["1"]
viesti2="Laita kartan koko: "
while True:
    try:
        kartan_koko=int(input(viesti2))
        break
    except:
        viesti2="Yritä uudelleen: "

total_mapy=kartan_koko
total_mapx=kartan_koko

print("")

viesti="laita näköetäisyys: "
while True:
    try:
        FOV=int(input(viesti))
        break
    except:
        viesti="yritä uudelleen: "

view_range=FOV
print("")


pelaajax=round(total_mapx/2)
pelaajay=round(total_mapy/2)

vihollinenx=pelaajax+random.randint(3,7)
vihollineny=pelaajay+random.randint(3,7)

pelaajafalsey=pelaajay

def generate_map(total_mapy,total_mapx,laatat):
    return {(x,y):random.choice(laatat)
            for x in range(total_mapx)
            for y in range(total_mapy)}
                
print("Luodaan maailmaa")
kartta = generate_map(total_mapy,total_mapx,laatat)

def render_map(pelaajax,pelaajay,kartta,view_range):
    for y in range(pelaajay-view_range,pelaajay+view_range+1):
        for x in range(pelaajax-view_range,pelaajax+view_range+1):
            if pelaajax == x and pelaajay == y:
                print("# ",end="")
                continue
            match kartta[(x,y)]:
                case "1":
                    print("  ",end="")
                case "2":
                    print("  ",end="")
                case "seinä":
                    print("██",end="")
                case "ruoho":
                    print("ll",end="")
                case "vihollinen":
                    print("ä",end="")
        print()

def movement():
    key=input()

    if key == "w":
        ylös()

    elif key == "s":
        alas()

    elif key == "d":
        oikealle()

    elif key == "a":
        vasemmalle()
    else:
        print("")


def ylös():
    global pelaajay
    global pelaajafalsey
    pelaajay -=1
    pelaajafalsey +=1

def alas():
    global pelaajay
    global pelaajafalsey
    pelaajay += 1
    pelaajafalsey -=1

def oikealle():
    global pelaajax
    pelaajax += 1

def vasemmalle():
    global pelaajax
    pelaajax -= 1

def house(housex,housey):
    house_width = random.randint(5,10)
    house_height = random.randint(5,10)

    for y in range(house_height):
        for x in range(house_width):
            kartta[housex+x,housey+y]="seinä"
            


for y in range(0,total_mapy):
    for x in range(0,total_mapx):
        if y%10==0 and x%10==0:
            kartta[x,y]="ruoho"

for i in range(400):
    housex=random.randint(0,total_mapx)
    housey=random.randint(0,total_mapy)
    house(housex,housey)

kartta[vihollinenx,vihollineny]="vihollinen"

while True:
    clear()
    render_map(pelaajax,pelaajay,kartta,view_range)
    print("x:", pelaajax)
    print("y:", pelaajafalsey)
    movement()
    if pelaajax== vihollinenx and pelaajay==vihollineny:
        main2.vihollisen_hp=10
        main2.pelaajan_hp=10
        main2.päädyit_taisteluun()