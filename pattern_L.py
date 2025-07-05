def pattern_L():
    height = int(input("Enter the height of the letter L: "))
    width = height // 2  # Width can be half of height for proportion

    for i in range(height):
        for j in range(width):
            if j == 0 or i == height - 1:
                print("L", end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_L()
