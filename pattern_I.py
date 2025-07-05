def pattern_I(n):
    width = n // 2 + 1  # Proportional width
    middle = width // 2  # Middle column for vertical bar
    for i in range(n):
        for j in range(width):
            if i == 0 or i == n - 1 or j == middle:
                print("I", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
num = int(input("Enter the height of the pattern: "))
pattern_I(num)
