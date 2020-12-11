lines = open('08/input.txt').read().splitlines()


def get_next_index(i, acc):
    line = lines[i]
    if line.startswith('acc'):
        argument = line.split(' ')[1]
        if argument.startswith('+'):
            acc += int(argument[1:])
        else:
            acc -= int(argument[1:])
        i += 1
    elif line.startswith('nop'):
        i += 1
    elif line.startswith('jmp'):
        argument = line.split(' ')[1]
        if argument.startswith('+'):
            i += int(argument[1:])
        else:
            i -= int(argument[1:])

    return (i, acc)


acc, i, used_i = 0, 0, []

while not i in used_i:
    used_i.append(i)
    (i, acc) = get_next_index(i, acc)

print(f"The puzzle result is: {acc}")
