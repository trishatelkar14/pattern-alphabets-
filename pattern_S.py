def pattern_S():
    size = int(input("Enter height (min 7): "))
    ch = input("Enter character: ") or "S"
    for i in range(size):
        for j in range(size // 2 + 1):
            if (
                i == 0 or i == size // 2 or i == size - 1
                or (j == 0 and i < size // 2)
                or (j == size // 2 and i > size // 2)
            ):
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()
pattern_S()
