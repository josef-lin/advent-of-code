import re
from math import prod
from collections import defaultdict

def is_game_possible(game: str, bag: dict) -> bool:
    # split by ',' to get number and color
    for i, turn in enumerate(game):
        cubes = turn.split(',')
        for item in cubes:
            # remove whitespaces
            item = item.split()
            # item[1] is the color, item[0] is the number pulled
            if int(item[0])>bag[item[1]]:
                return False
    return True

def smallest_possible_bag(game: str) -> int:
    bag = defaultdict(int)
    for i, turn in enumerate(game):
        cubes = turn.split(',')
        for item in cubes:
            # remove whitespaces
            item = item.split()
            # item[1] is the color, item[0] is the number pulled
            if int(item[0])>bag[item[1]]:
                bag[item[1]] = int(item[0])
    return prod([x for x in list(bag.values())])

input_file = open('cube_conundrum.txt')
inputs = input_file.readlines()

total1 = 0
bag = {'red':12, 'green':13, 'blue':14}

total2 = 0

for line in inputs:
    # extracts game number
    game_id = re.search(r"Game (\d+)", line).group(1)

    # remove "Game id:" and split by ';'
    game = line.split(':',1)[1].split(';')
    total1 += int(game_id) if is_game_possible(game, bag) else 0
    total2 += smallest_possible_bag(game)

print(total1)
print(total2)
