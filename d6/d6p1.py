lines = open('d6/d6.txt').read().splitlines()

# New input with only one string per group
inputs = ''.join(['-' if not line else line for line in lines]).split('-')
sum = 0

# Count length from set from char list from input string
# A set won't have duplicates, so we get the count of unique chars
for input in inputs:
    sum += len(set(list(input)))

print(f"The puzzle result is: {sum}")
