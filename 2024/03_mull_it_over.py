import re

def find_mul(s):
    total = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, s)
    for match in matches:
        x, y = map(int, match)
        total += x*y
    return total

def find_mul_do(s, d):
    total = 0
    do = d
    patterns = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"
    matches = re.finditer(patterns, s)
    for match in matches:
        if match.group(0).startswith("mul") and do:
            x = int(match.group(1))
            y = int(match.group(2))
            total += x*y
        elif match.group(0) == "don't()":
            do = False
        elif match.group(0) == "do()":
            do = True
    return total, do

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input_file = open('03_mull_it_over.txt')
print(find_mul(test_string))
print(find_mul_do(test_string, True))
total = 0
total_do = 0
do = True
for line in input_file:
    total += find_mul(line)
    line_total, do = find_mul_do(line, do)
    total_do += line_total
print(total)
print(total_do)