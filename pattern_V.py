def pattern_V():
    rows = int(input("Enter height of V (odd number ≥ 3): "))
    ch = input("Enter character to use: ") or "V"
    cols = 2 * rows - 1

    for i in range(rows):
        for j in range(cols):
            if j == i or j == cols - 1 - i:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_V()
