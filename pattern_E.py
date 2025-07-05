def pattern_E(n):
    for i in range(n):
        for j in range(n - 2):  # Width is slightly less than height for proportion
            if j == 0 or i == 0 or i == n // 2 or i == n - 1:
                print("E", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get user input
num = int(input("Enter the height of the pattern: "))
pattern_E(num)
