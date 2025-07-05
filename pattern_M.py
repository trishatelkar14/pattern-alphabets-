def pattern_M():
    size = int(input("Enter the height (odd number ≥ 3): "))
    for i in range(size):
        for j in range(size):
            if (
                j == 0 or j == size - 1 or
                (i == j and j <= size // 2) or
                (i + j == size - 1 and j >= size // 2)
            ):
                print("M", end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_M()
