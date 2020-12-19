lines = open('13/input.txt').read().splitlines()

earliest = int(lines[0])
buses = lines[1].split(',')

buses_time = {}

for bus in buses:
    if bus.isdigit():
        bus = int(bus)
        buses_time[bus] = bus - earliest % bus

bus = min(buses_time, key=buses_time.get)

print(f"The puzzle result is: {bus * buses_time[bus]}")
