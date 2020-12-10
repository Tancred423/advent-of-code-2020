import math
lines = open('d5/d5.txt').read().splitlines()

seat_ids = []

for line in lines:
    # Rows on plane
    x = 0
    y = 127

    for c in line[:-4]:
        if c == 'F':
            y = math.floor((x + y) / 2)
        else:
            x = math.ceil((x + y) / 2)

    if line[6] == 'F':
        row = x
    else:
        row = y

    # Columns on plane
    a = 0
    b = 7

    for c in line[-3:]:
        if c == 'L':
            b = math.floor((a + b) / 2)
        else:
            a = math.ceil((a + b) / 2)

    seat_ids.append(row * 8 + a)  # a and b are always the same

seat_ids.sort()
print(f"The puzzle result is: {seat_ids[-1]}")
