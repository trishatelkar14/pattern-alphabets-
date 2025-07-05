def pattern_O():
    height = int(input("Enter height of O: "))
    width = int(input("Enter width of O: "))
    ch = input("Enter character to use: ")

    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_O()
