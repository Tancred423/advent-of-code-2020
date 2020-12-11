rows = [list(x) for x in open('11/input.txt').read().splitlines()]


def get_occupied(r, s):
    seats = []
    if r > 0:
        seats.append(rows[r - 1][s])            # top
        if s > 0:
            seats.append(rows[r - 1][s - 1])    # top left
        if s < len(rows[0]) - 1:
            seats.append(rows[r - 1][s + 1])    # top right

    if s > 0:
        seats.append(rows[r][s - 1])            # left
    if s < len(rows[0]) - 1:
        seats.append(rows[r][s + 1])            # right

    if r < len(rows) - 1:
        seats.append(rows[r + 1][s])            # bottom
        if s > 0:
            seats.append(rows[r + 1][s - 1])    # bottom left
        if s < len(rows[0]) - 1:
            seats.append(rows[r + 1][s + 1])    # bottom right
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
            elif seat == '#' and adjacent >= 4:
                seat = 'L'
                state_changed = True
            new_row.append(seat)
        new_grid.append(new_row)
    rows = new_grid[:]

count = 0
for row in rows:
    count += row.count('#')

print(f"The puzzle result is: {count}")
