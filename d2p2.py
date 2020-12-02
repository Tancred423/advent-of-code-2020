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
    first = int(policy_split[0]) - 1
    second = int(policy_split[1][:-2]) - 1

    # Password
    password = val_split[1].strip()

    # Positions
    first_letter = None
    second_letter = None

    if len(password) >= first:
        first_letter = password[first]

    if len(password) >= second:
        second_letter = password[second]

    if (first_letter == letter) ^ (second_letter == letter):
        valid_passwords += 1

print(f'Amount of valid passwords: {valid_passwords}')
