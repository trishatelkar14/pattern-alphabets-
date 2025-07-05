def pattern_D(n):
    width = n // 2 + 1  # Dynamically scale width
    for i in range(n):
        for j in range(width):
            if j == 0 or \
               (j == width - 1 and i != 0 and i != n - 1) or \
               ((i == 0 or i == n - 1) and j < width - 1):
                print("D", end=" ")
            else:
                print(" ", end=" ")
        print()

# Input from user
num = int(input("Enter the height of the pattern: "))
pattern_D(num)
