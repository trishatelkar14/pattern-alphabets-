def pattern_U():
    height = int(input("Enter height (min 5): "))
    ch = input("Enter character to use: ") or "U"
    width = height // 2 + 2
    for i in range(height):
        for j in range(width):
            if (
                (j == 0 or j == width - 1) and i != height - 1
                or (i == height - 1 and j != 0 and j != width - 1)
            ):
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()
pattern_U()
