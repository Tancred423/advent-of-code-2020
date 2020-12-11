lines = open('04/input.txt').read().splitlines()

# New input with a single string per pair
passports = []
tmp_passport = ''

for line in lines:
    if not line:
        passports.append(tmp_passport.strip())
        tmp_passport = ''
    else:
        tmp_passport += f"{line} "

passports.append(tmp_passport.strip())

# Check if each entry-string contains all mandatory keys
valids = 0

for passport in passports:
    if all(x in passport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        valids += 1

print(f"The puzzle answer is: {valids}")
