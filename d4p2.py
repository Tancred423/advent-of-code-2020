from puzzle_input import lines
import re

# New input with a single string per passport
passports = []
tmp_passport = ''

for line in lines:
    if not line:
        passports.append(tmp_passport.strip())
        tmp_passport = ''
    else:
        tmp_passport += f"{line} "

passports.append(tmp_passport.strip())


def represents_int(s):
    # Check for valid int (digits only)
    try:
        int(s)
        return True
    except ValueError:
        return False


# Check if each entry-string contains all mandatory keys
# and then if the values are valid
valids = 0

for passport in passports:
    if all(x in passport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        pairs = passport.split(' ')
        valid = True

        for pair in pairs:
            key, value = pair.split(':', 1)

            if key == 'byr':
                if not represents_int(value) or len(value) != 4 or not int(value) in range(1920, 2002 + 1):
                    valid = False
                    break
            elif key == 'iyr':
                if not represents_int(value) or len(value) != 4 or not int(value) in range(2010, 2020 + 1):
                    valid = False
                    break
            elif key == 'eyr':
                if not represents_int(value) or len(value) != 4 or not int(value) in range(2020, 2030 + 1):
                    valid = False
                    break
            elif key == 'hgt':
                if value.endswith('cm'):
                    val = value[:-2]
                    if not represents_int(val) or not int(val) in range(150, 193 + 1):
                        valid = False
                        break
                elif value.endswith('in'):
                    val = value[:-2]
                    if not represents_int(val) or not int(val) in range(59, 76 + 1):
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif key == 'hcl':
                if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                    valid = False
                    break
            elif key == 'ecl':
                if not value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    valid = False
                    break
            elif key == 'pid':
                if not represents_int(value) or len(value) != 9:
                    valid = False
                    break

        if valid:
            valids += 1

print(f"The puzzle answer is: {valids}")
