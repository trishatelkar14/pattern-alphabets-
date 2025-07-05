def pattern_Z():
    size = int(input("Enter height of Z (min 3): "))
    ch = input("Enter character to use (default 'Z'): ") or "Z"

    if size < 3:
        print("Please enter a height of at least 3.")
        return

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or i + j == size - 1:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_Z()
