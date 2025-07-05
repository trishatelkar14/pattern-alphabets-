def pattern_P():
    height = int(input("Enter height of P (>=5): "))
    width = height // 2
    for i in range(height):
        for j in range(width):
            if (
                j == 0                                     # left vertical bar
                or i == 0                                  # top bar
                or (i == height // 2)                      # middle bar
                or (j == width - 1 and i < height // 2)    # right bar on top half
            ):
                print("P", end=" ")
            else:
                print(" ", end=" ")
        print()
pattern_P()
