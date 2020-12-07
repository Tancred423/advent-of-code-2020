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


# Recusive counting of inner bags

def get_bag_count(bags, bag):
    count = 1  # The bag itself

    # The count of sub bags
    sub_bags = bags[bag]
    for sub_bag, amount in sub_bags.items():
        count += amount * get_bag_count(bags, sub_bag)

    return count


# Minus one because the shiny gold bag doesn't count
count = get_bag_count(bags, 'shiny gold') - 1

print(f"The puzzle result is: {count}")
