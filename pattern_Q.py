def pattern_Q():
    height = int(input("Enter height of Q (minimum 7): "))
    ch = input("Enter character to use: ") or "Q"
    width = height  # for proportion
    tail_row = height - 2
    tail_col = width - 2
    for i in range(height + 1):  # One extra row for tail
        for j in range(width):
            if (
                (i == 0 and 1 <= j <= width - 2) or                          # Top border
                (i == height - 1 and 1 <= j <= width - 2) or                # Bottom border
                (1 <= i <= height - 2 and (j == 1 or j == width - 2)) or    # Side borders
                (i == tail_row and j == width - 2) or                       # Tail start
                (i == height and j == width - 1)                            # Tail end
            ):
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()
pattern_Q()
