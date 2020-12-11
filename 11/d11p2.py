rows = [list(x) for x in open('11/input.txt').read().splitlines()]


def get_occupied(r, s):
    max_len = len(rows[0])
    max_hei = len(rows)

    seats = []

    # Move top left
    i = 1

    while True:
        y = r - i
        x = s - i

        if y >= 0 and x >= 0:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move top
    i = 1

    while True:
        y = r - i
        x = s

        if y >= 0:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move top right
    i = 1

    while True:
        y = r - i
        x = s + i

        if y >= 0 and x < max_len:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move left
    i = 1

    while True:
        y = r
        x = s - i

        if x >= 0:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move right
    i = 1

    while True:
        y = r
        x = s + i

        if x < max_len:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move bottom left
    i = 1

    while True:
        y = r + i
        x = s - i

        if y < max_hei and x >= 0:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move bottom
    i = 1

    while True:
        y = r + i
        x = s

        if y < max_hei:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    # Move bottom right
    i = 1

    while True:
        y = r + i
        x = s + i

        if y < max_hei and x < max_len:
            if rows[y][x] == '.':
                i += 1
            else:
                seats.append(rows[y][x])
                break
        else:
            break

    return seats.count('#')


state_changed = True

while state_changed:
    state_changed = False
    new_grid = []
    for r, seats in enumerate(rows):
        new_row = []
        for s, seat in enumerate(seats):
            adjacent = get_occupied(r, s)
            if seat == 'L' and adjacent == 0:
                seat = '#'
                state_changed = True
            elif seat == '#' and adjacent >= 5:
                seat = 'L'
                state_changed = True
            new_row.append(seat)
        new_grid.append(new_row)
    rows = new_grid[:]

count = 0
for row in rows:
    count += row.count('#')

print(f"The puzzle result is: {count}")
