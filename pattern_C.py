def pattern_C(n):
    width = n // 2 + 1  # Width scales with height
    for i in range(n):
        for j in range(width):
            if (i == 0 or i == n - 1 or j == 0):
                print("C", end=" ")
            else:
                print(" ", end=" ")
        print()

# Input from user
num = int(input("Enter the height of the pattern: "))
pattern_C(num)
