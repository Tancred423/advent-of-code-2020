import re
lines = open('12/input.txt').read().splitlines()

ns = 0
we = 0
facing = 'east'

directions = ['north', 'east', 'south', 'west']


def get_next_direction(times, clockwise):
    i = directions.index(facing)

    if clockwise:
        return directions[int((i + times) % len(directions))]
    else:
        return directions[int((i - times) % len(directions))]


for line in lines:
    line_split = re.split('(\d+)', line)
    action = line_split[0]
    value = int(line_split[1])

    if action == 'N' or (action == 'F' and facing == 'north'):
        ns += value
    elif action == 'S' or (action == 'F' and facing == 'south'):
        ns -= value
    elif action == 'W' or (action == 'F' and facing == 'west'):
        we += value
    elif action == 'E' or (action == 'F' and facing == 'east'):
        we -= value
    elif action == 'L' or action == 'R':
        times = value / 90
        facing = get_next_direction(times, action == 'R')

print(f"The puzzle result is: {abs(ns) + abs(we)}")
