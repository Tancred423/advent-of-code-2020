# Disclaimer: This solution is cheated and copy pasted because I was too stoopid

import math
lines = open('13/input.txt').read().splitlines()

buses = lines[1].split(',')

departures = [(t, int(bus)) for t, bus in enumerate(buses) if bus.isdigit()]
times, deps = zip(*departures)

solved = 1
t = departures[0][0] + departures[0][1]
increment = math.prod(deps[:solved])

while True:
    if all([(t + t_plus) % bus_id == 0 for t_plus, bus_id in departures[:solved + 1]]):
        solved += 1
        increment = math.prod(deps[:solved])
        if solved == len(deps):
            print(f"The puzzle result is: {t}")
            break
    t += increment
