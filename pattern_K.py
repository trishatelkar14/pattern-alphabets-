def pattern_K(height):
    for i in range(height):
        for j in range(height // 2 + 1):
            if j == 0:
                print("K", end=" ")
            elif i < height // 2 and j == (height // 2) - i:
                print("K", end=" ")
            elif i >= height // 2 and j == i - height // 2 + 1:
                print("K", end=" ")
            else:
                print(" ", end=" ")
        print()

# Take user input
user_height = int(input("Enter the height of the pattern (odd number recommended): "))
pattern_K(user_height)
