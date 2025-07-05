def pattern_A(n):
    width = n // 2 + 1  # Adjusting width proportionally
    for i in range(n):
        for j in range(width):
            if ((i == 0 and j != 0 and j != width - 1) or
                (i == n // 2) or
                (j == 0 and i != 0) or
                (j == width - 1 and i != 0)):
                print("A", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get user input
num = int(input("Enter the height of the pattern: "))
pattern_A(num)

