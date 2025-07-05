def pattern_N():
    size = int(input("Enter the height of N (≥ 3): "))
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == j:
                print("N", end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_N()
