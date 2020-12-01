with open('d1.txt') as f:
    puzzle_input = f.readlines()

puzzle_input = [int(x.strip()) for x in puzzle_input]

for val in puzzle_input:
    missing = 2020 - val
    if (missing in puzzle_input):
        break

print(val * missing)
