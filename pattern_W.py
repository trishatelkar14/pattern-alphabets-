def pattern_W():
    height = int(input("Enter height of W (min 3): "))
    ch = input("Enter character to use (default 'W'): ") or "W"
    if height < 3:
        print("Height must be at least 3.")
        return
    width = 4 * height - 3
    for r in range(height):
        for c in range(width):
            is_char = False
            if c == r:
                is_char = True  
            elif c == 2 * (height - 1) - r:
                is_char = True 
            elif c == 2 * (height - 1) + r:
                is_char = True 
            elif c == 4 * (height - 1) - r:
                is_char = True 
            if is_char:
                print(ch, end="")
            else:
                print(" ", end="")
        print()

pattern_W()
