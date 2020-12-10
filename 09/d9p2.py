lines_int = [int(x) for x in open('d9/d9.txt').read().splitlines()]

n = 144381670
found = False

i = 0
while i < len(lines_int):
    curr = lines_int[i]

    j = i

    set = []

    while j < len(lines_int):
        curr_j = lines_int[j]

        set.append(curr_j)

        if len(set) > 1 and sum(set) == n:
            print(f"The puzzle result is: {min(set) + max(set)}")
            found = True
            break
        elif len(set) > 1 and sum(set) > n:
            break

        j += 1

    if found:
        break

    i += 1
