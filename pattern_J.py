def pattern_J(n):
    width = n // 2 + 1
    middle = width // 2

    for i in range(n):
        for j in range(width):
            if i == 0 or j == middle or (i == n - 1 and j < middle) or (j == 0 and i >= n - middle):
                print("J", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
num = int(input("Enter the height of the pattern: "))
pattern_J(num)
