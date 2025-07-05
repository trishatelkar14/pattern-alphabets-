def pattern_F(n):
    width = n // 2 + 1  # Proportional width
    for i in range(n):
        for j in range(width):
            if j == 0 or i == 0 or i == n // 2:
                print("F", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get user input and display pattern
num = int(input("Enter the height of the pattern: "))
pattern_F(num)
