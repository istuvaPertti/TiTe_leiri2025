import random

map_height = 16
map_width = 16

pelaajay =50
pelaajax =50

view_range = 10

total_mapy = 100
total_mapx = 100

def empty():
    pass

def treasure():
    pass

laatat = ["1","2"]

def generate_map(total_mapy,total_mapx,laatat):
    return {(x,y):random.choice(laatat)
            for x in range(total_mapx)
            for y in range(total_mapy)}
                
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
                    print("██",end="")
        print()
    print()
    print()
    print()
    print()     
    print()

def ylös():
    global pelaajay
    pelaajay -=1

def alas():
    global pelaajay
    pelaajay += 1

def oikealle():
    global pelaajax
    pelaajax += 1

def vasemmalle():
    global pelaajax
    pelaajax -= 1


while True:

    render_map(pelaajax,pelaajay,kartta,view_range)

    key = input()

    if key == "w":
        ylös()

    elif key == "s":
        alas()

    elif key == "d":
        oikealle()

    elif key == "a":
        vasemmalle()


  


    
            