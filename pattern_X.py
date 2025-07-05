def pattern_X():
    size = int(input("Enter the height of X (odd number, min 3): "))
    ch = input("Enter character to use (default 'X'): ") or "X"

    if size < 3 or size % 2 == 0:
        print("Please enter an odd number >= 3.")
        return

    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_X()
