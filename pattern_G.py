def pattern_G(n):
    width = n // 2 + 1  # Proportional width
    for i in range(n):
        for j in range(width):
            if (i == 0 or i == n - 1 or j == 0 or
                (i >= n // 2 and j == width - 1) or
                (i == n // 2 and j >= width // 2)):
                print("G", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example use
num = int(input("Enter the height of the pattern: "))
pattern_G(num)
