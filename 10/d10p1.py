jolts = [int(x) for x in open('d10/d10.txt').read().splitlines()]
jolts.sort()

one_jolt = 0
three_jolt = 1  # 1 because final step

prev = 0
for jolt in jolts:
    if jolt - prev == 1:
        one_jolt += 1
    elif jolt - prev == 3:
        three_jolt += 1

    prev = jolt

print(f"The puzzle result is: {one_jolt * three_jolt}")
