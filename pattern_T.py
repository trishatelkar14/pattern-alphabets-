def pattern_T():
    height = int(input("Enter height (min 5): "))
    ch = input("Enter character to use: ") or "T"
    width = height if height % 2 != 0 else height + 1  # make center column

    for i in range(height):
        for j in range(width):
            if i == 0 or j == width // 2:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_T()
