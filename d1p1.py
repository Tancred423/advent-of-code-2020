from puzzle_input import lines_int

for line in lines_int:
    missing = 2020 - line
    if missing in lines_int:
        print(f"The puzzle answer is: {line * missing}")
        break
