import re

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

regex_sym = ['^\d\.']
regex_num = '\d+'

#input_file = open('gear_ratios.txt')
#inputs = input_file.read()
inputs = test
lines = inputs.split('\n')
for line in lines:
    print(line)
    print(re.findall(regex_sym, line))

    


