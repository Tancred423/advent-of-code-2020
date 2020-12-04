from puzzle_input import lines

valid_passwords = 0

for line in lines:
    policy, password = line.split(':', 1)
    policy = policy.strip()
    password = password.strip()

    # Policy
    policy_split = policy.split('-')

    letter = policy[-1:]
    min_amount = int(policy_split[0])
    max_amount = int(policy_split[1][:-2])

    # Amount
    letter_amount = password.count(letter)

    if letter_amount >= min_amount and letter_amount <= max_amount:
        valid_passwords += 1

print(f"The puzzle answer is: {valid_passwords}")
