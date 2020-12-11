jolts = [int(x) for x in open('10/input.txt').read().splitlines()]

# Append 0 (start) and max + 3 (end)
# Then sort
jolts.append(0)
jolts.append(max(jolts)+3)
jolts.sort()

# List as long as input entries for memorization
possibilities = []
for oogabooga in range(0, len(jolts)):
    possibilities.append(0)

# Initial value for first step
possibilities[0] = 1

# Of every number, we take the 3 previous ones and
# check if the difference of each is <= 3 (valid).
# If so, we will add the number of possibilties of that previous number
# to the number of possibilities of the current number. (memorization)
i = 0
while i < len(jolts):
    jolt = jolts[i]

    for r in range(i - 3, i):
        diff = jolt - jolts[r]
        if diff <= 3:
            possibilities[i] += possibilities[r]

    i += 1

# The last entry will then have the sum of all possibilities.
print(f"The puzzle result is: {possibilities[-1]}")
