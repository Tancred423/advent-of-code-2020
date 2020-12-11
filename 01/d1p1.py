lines_int = [int(x) for x in open('01/input.txt').read().splitlines()]

for line in lines_int:
    missing = 2020 - line
    if missing in lines_int:
        print(f"The puzzle answer is: {line * missing}")
        break
