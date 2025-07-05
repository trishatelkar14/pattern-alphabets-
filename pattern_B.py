def pattern_B(n):
    width = n // 2 + 1  # Dynamic width based on height
    for i in range(n):
        for j in range(width):
            if (j == 0 or
                (i == 0 and j != width - 1) or
                (i == n // 2 and j != width - 1) or
                (i == n - 1 and j != width - 1) or
                (j == width - 1 and (i != 0 and i != n // 2 and i != n - 1))):
                print("B", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get user input and call the function
num = int(input("Enter the height of the pattern: "))
pattern_B(num)
