lines = open('d6/d6.txt').read().splitlines()

persons = []
count = 0


def checkCount(persons):
    # Convert group list to one string to a char list to a set
    # A set won't have duplicates
    # Then check per char if it's available in all list entries
    count = 0
    for char in set(list(''.join(persons))):
        if all(char in person for person in persons):
            count += 1
    return count


# Building a list with inputs of one group
# Then check the count of chars that are available in all list entries
for line in lines:
    if not line:
        count += checkCount(persons)
        persons.clear()
    else:
        persons.append(line)
count += checkCount(persons)

print(f"The puzzle result is: {count}")
