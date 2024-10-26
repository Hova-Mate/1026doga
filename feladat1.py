def fel1():
    k = 1
    talat = 0

    while talat < 10:
        ky = ((2 ** k) + 1) ** 2 - 2
        print(f"{ky}, ", end="")
        talat = talat + 1
        k = k + 1

    print("\n")