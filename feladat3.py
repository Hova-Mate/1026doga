def fel3():
    for i in range(-200, 150):
        if i % 5 == 0:
            print(f"{i}@", end="")

    print("\n")

    f = -200
    while f < 150:
        if f % 5 == 0:
            print(f"{f}@", end="")
        f += 1

    print("\n")