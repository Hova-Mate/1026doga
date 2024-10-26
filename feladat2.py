
def fel2():
    vegOsszeg = int(input("kérem adja meg a vég összeget: "))
    kategoria = input("Kérem adja meg hogy milyen kedvezménnye rendelkezik:")

    if vegOsszeg > 10000:
        print("Akció: 5% kedvezmény Nagy összegű vásárlás!")
    elif kategoria == "arany kártyás":
        print("Akció: 10% kedvezményt kap ma!")
    elif kategoria == "ezüst kártyás":
        print("Akció: 5% kedvezményt kap ma!")
    elif kategoria == "bronz kártyás":
        print("Akció: 2% kedvezményt kap ma!")
    elif kategoria == "VIP":
        print("Akció: 20% kedvezményt kap ma!")
    else:
        print("Haloween akció 1% kedvezményt kap")

    print("\n")