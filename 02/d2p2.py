lines = open('d2/d2.txt').read().splitlines()

valid_passwords = 0

for line in lines:
    policy, password = line.split(':')
    policy = policy.strip()
    password = password.strip()

    # Policy
    policy_split = policy.split('-')

    letter = policy[-1:]
    first = int(policy_split[0]) - 1
    second = int(policy_split[1][:-2]) - 1

    # Positions
    first_letter = None
    second_letter = None

    if len(password) >= first:
        first_letter = password[first]

    if len(password) >= second:
        second_letter = password[second]

    if (first_letter == letter) ^ (second_letter == letter):
        valid_passwords += 1

print(f"The puzzle answer is: {valid_passwords}")
