def pattern_H(n):
    width = n // 2 + 1  # Adjust width proportionally
    for i in range(n):
        for j in range(width):
            if j == 0 or j == width - 1 or i == n // 2:
                print("H", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
num = int(input("Enter the height of the pattern: "))
pattern_H(num)
