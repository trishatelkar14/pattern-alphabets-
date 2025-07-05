def pattern_Y():
    size = int(input("Enter height of Y (odd number, min 5): "))
    ch = input("Enter character to use (default 'Y'): ") or "Y"
    if size < 5 or size % 2 == 0:
        print("Please enter an odd number ≥ 5.")
        return
    mid = size // 2
    for i in range(size):
        for j in range(size):
            if (i == j and i < mid) or (i + j == size - 1 and i < mid) or (j == mid and i >= mid):
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_Y()
