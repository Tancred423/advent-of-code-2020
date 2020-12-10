lines = open('d7/d7.txt').read().splitlines()

# Building a dictionary with all bags
# bags:
#   key:
#       color
#   value:
#       sub_bags:
#           key:
#               color
#           value:
#               amount

bags = {}

for line in lines:
    key, values = line.split(' bags contain ', 1)

    values_split = values.replace('.', '').replace(
        'bags', '').replace('bag', '').split(',')

    sub_bags = {}

    for value in values_split:
        value = value.strip()
        sub_value_str = value[:1]

        if sub_value_str.isdigit():
            sub_value = int(sub_value_str)
            sub_key = value[2:]
            sub_bags[sub_key] = sub_value

    bags[key] = sub_bags


# Count shiny gold bags

def get_keys(keys):
    # Search for all bags that contains at least one of the keys
    new_keys = []

    for key, value in bags.items():
        for sub_key in value:
            if sub_key in keys:
                new_keys.append(key)

    return new_keys


# Initial run for bags that contain shiny gold directly
keys = get_keys(['shiny gold'])
keys_len = len(set(keys))

while True:
    # Append the bags that contain the bags that contain shiny gold
    keys += get_keys(keys)

    # If the length doesn't change, there are no more bags to collect
    if len(set(keys)) == keys_len:
        break

    # Update to the new amount of keys
    keys_len = len(set(keys))

print(f"The puzzle result is: {keys_len}")
