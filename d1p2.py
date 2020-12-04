from puzzle_input import lines_int

found = False

for line in lines_int:
    missing = 2020 - line

    for line2 in lines_int:
        missing2 = missing - line2

        if missing2 in lines_int:
            print(f"The puzzle answer is: {line * line2 * missing2}")
            found = True
            break

    if found:
        break
