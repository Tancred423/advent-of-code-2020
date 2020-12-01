with open('d1.txt') as f:
    puzzle_input = f.readlines()

puzzle_input = [int(x.strip()) for x in puzzle_input]

found = False

for val in puzzle_input:
    missing = 2020 - val

    for val2 in puzzle_input:
        missing2 = missing - val2

        if (missing2 in puzzle_input):
            found = True
            break

    if found:
        break

print(val * val2 * missing2)
