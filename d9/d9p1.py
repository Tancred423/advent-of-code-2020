lines_int = [int(x) for x in open('d9/d9.txt').read().splitlines()]

i = 25
while i < len(lines_int):
    curr = lines_int[i]
    prevs = lines_int[i - 25:i]
    is_valid = False

    for prev in prevs:
        missing = curr - prev
        if prev != missing and missing in prevs:
            is_valid = True

    if not is_valid:
        print(f"The puzzle result is: {curr}")
        break

    i += 1
