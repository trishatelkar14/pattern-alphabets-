def pattern_R():
    size = int(input("Enter height of R (min 7): "))
    ch = input("Enter character to use: ") or "R"
    for i in range(size):
        for j in range(size // 2 + 1):
            if (
                j == 0
                or i == 0
                or i == size // 2
                or (j == size // 2 and i < size // 2)
                or (i - j == size // 2 - 1 and i > size // 2)
            ):
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_R()
