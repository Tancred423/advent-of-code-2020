# Disclaimer: This solution is cheated and copy pasted because I was too stoopid

lines = [(l[:3], int(l[4:])) for l in open('d8/d8.txt')]


def run(lines):
    A, IP = 0, 0
    e = set()
    while IP < len(lines) and IP not in e:
        e.add(IP)
        i, a = lines[IP]
        if i == 'jmp':
            IP += a-1
        if i == 'acc':
            A += a
        IP += 1
    return IP not in e, A


for l, (i, a) in enumerate(lines):
    if i == 'jmp':
        i = 'nop'
    elif i == 'nop':
        i = 'jmp'
    b, A = run(lines[:l] + [(i, a)] + lines[l+1:])
    if b:
        break

print(f"The puzzle result is: {A}")
