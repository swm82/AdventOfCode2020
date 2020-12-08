import sys
import re

# Verification methods
def check_year(year, minimum, maximum):
    if not re.match('(\d){4}', year):
        return False
    return minimum <= int(year) <= maximum

def byr(year):
    return check_year(year, 1920, 2002)

def iyr(year):
    return check_year(year, 2010, 2020)

def eyr(year):
    return check_year(year, 2020, 2030)

def hgt(height):
    if not re.match('^(\d)+(in|cm)$', height):
        return False
    measurement = int(height[:-2])
    if height.endswith('in'):
        return 59 <= measurement <= 76
    else:
        return 150 <= measurement <= 193

def hcl(color):
    if not re.match('^#([0-9]*|[a-f]*){6}$', color):
        return False
    return True

def ecl(color):
    return color in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def pid(passport):
    if re.match('^(\d){9}$', passport):
        return True
    return False

# Verification dispatcher
def check_passports(passports):
    count = 0
    fields = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid}
    for passport in passports:
        if validate(passport, fields):
            count += 1
    return count

def validate(passport, fields):
    for field, method in fields.items():
        if field not in passport:
            return False
        if not method(passport[field]):
            return False
    return True

def load_data(filename):
    with open(filename) as f:
        data = f.read()
    ids = data.split('\n\n')
    passports = []
    for i in ids:
        fields = i.split()
        fields_map = {}
        for field in fields:
            x, y = field.split(':')
            fields_map[x] = y
        passports.append(fields_map)
    return passports

if __name__ == '__main__':
    filename = 'day4.txt'
    data = load_data(filename)
    print('Valid passports: ' + str(check_passports(data)))