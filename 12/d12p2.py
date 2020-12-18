import re
lines = open('12/input.txt').read().splitlines()

ns = 0
we = 0

ns_waypoint = 1
we_waypoint = -10

directions = ['north', 'east', 'south', 'west']


def get_next_coords(times, clockwise):
    y = directions.index('north' if ns_waypoint > 0 else 'south')
    x = directions.index('west' if we_waypoint > 0 else 'east')

    ns_new = 0
    we_new = 0

    if clockwise:
        y_next_dir = directions[int((y + times) % len(directions))]
        x_next_dir = directions[int((x + times) % len(directions))]
    else:
        y_next_dir = directions[int((y - times) % len(directions))]
        x_next_dir = directions[int((x - times) % len(directions))]

    if y_next_dir == 'north':
        ns_new = abs(ns_waypoint)
    elif y_next_dir == 'south':
        ns_new = abs(ns_waypoint) * -1
    elif y_next_dir == 'west':
        we_new = abs(ns_waypoint)
    elif y_next_dir == 'east':
        we_new = abs(ns_waypoint) * -1

    if x_next_dir == 'north':
        ns_new = abs(we_waypoint)
    elif x_next_dir == 'south':
        ns_new = abs(we_waypoint) * -1
    elif x_next_dir == 'west':
        we_new = abs(we_waypoint)
    elif x_next_dir == 'east':
        we_new = abs(we_waypoint) * -1

    return (ns_new, we_new)


for line in lines:
    line_split = re.split('(\d+)', line)
    action = line_split[0]
    value = int(line_split[1])

    if action == 'N':
        ns_waypoint += value
    elif action == 'S':
        ns_waypoint -= value
    elif action == 'W':
        we_waypoint += value
    elif action == 'E':
        we_waypoint -= value
    elif action == 'L' or action == 'R':
        times = value / 90
        (ns_waypoint, we_waypoint) = get_next_coords(times, action == 'R')
    elif action == 'F':
        ns += value * ns_waypoint
        we += value * we_waypoint


print(f"The puzzle result is: {abs(ns) + abs(we)}")
