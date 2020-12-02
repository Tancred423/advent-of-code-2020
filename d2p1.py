with open('d2.txt') as f:
    puzzle_input = f.readlines()

puzzle_input = [x.strip() for x in puzzle_input]

valid_passwords = 0

for val in puzzle_input:
    val_split = val.split(':')

    # Policy
    policy = val_split[0].strip()
    policy_split = policy.split('-')

    letter = policy[-1:]
    min_amount = int(policy_split[0])
    max_amount = int(policy_split[1][:-2])

    # Password
    password = val_split[1].strip()

    # Amount
    letter_amount = password.count(letter)

    if letter_amount >= min_amount and letter_amount <= max_amount:
        valid_passwords += 1

print(f'Amount of valid passwords: {valid_passwords}')
