def fel5():
    for i in range(60, -70, -1):
        if i == -69:
            print(f"{i}")
        else:
            print(f"{i},", end="")

    print("\n")
    f = 60
    while f > -70:
        if f == -69:
            print(f"{f}")
        else:
            print(f"{f},", end="")
        f = f - 1

    print("\n")