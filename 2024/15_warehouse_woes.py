import time
start_time = time.time()

def string_to_mat(s):
    blocks = s.split('\n\n')
    grid = []
    loc = None
    for r, line in enumerate(blocks[0].split('\n')):
        row = [char for char in line]
        grid.append(row)
        if loc == None:
            for c, char in enumerate(row):
                if char == '@':
                    loc = r+c*1j
                    break

    dir = {'v':1,'^':-1,'<':-1j,'>':1j}
    return grid, [dir[char] for char in blocks[1].replace('\n','')], loc

def rescale(grid):
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                row += ['#','#']
            elif grid[i][j] == 'O':
                row += ['[',']']
            elif grid[i][j] == '.':
                row += ['.', '.']
            elif grid[i][j] == '@':
                row += ['@','.']
                new_loc = i + 2*j*1j
        new_grid.append(row)
    return new_grid, new_loc

def print_grid(grid):
    s = ''
    for row in grid:
        for char in row:
            s += char
        s += '\n'
    return s

def make_move(grid, move, loc):
    new_grid = [row[:] for row in grid]
    next_move = move+loc
    moves = [loc]
    new_loc = loc
    while (grid[int(next_move.real)][int(next_move.imag)]=='O'):
        moves.append(next_move)
        next_move = moves[-1]+move
    if grid[int(next_move.real)][int(next_move.imag)] == '.':
        moves.append(next_move)
   
    if grid[int(next_move.real)][int(next_move.imag)] != '#': 
        for i in range(len(moves)-1,0,-1):
            new_grid[int(moves[i].real)][int(moves[i].imag)] = new_grid[int(moves[i-1].real)][int(moves[i-1].imag)]
        new_grid[int(loc.real)][int(loc.imag)] = '.'
        if len(moves) > 1:
            new_loc = moves[1]
    return new_grid, new_loc

def make_move_2(grid, start, move):
    new_grid = [row[:] for row in grid]
    new_loc = start
    stack = []
    path = [start]
    visited = set()
    while path:
        loc = path.pop()
        if loc in visited or grid[int(loc.real)][int(loc.imag)] == '.':
            continue
        if grid[int(loc.real)][int(loc.imag)] == '#':
            return new_grid, new_loc
        stack.append([grid[int(loc.real)][int(loc.imag)],loc])
        path.append(loc+move)
        if grid[int(loc.real)][int(loc.imag)] == '[':
            path.append(loc+1j)
        elif grid[int(loc.real)][int(loc.imag)] == ']':
            path.append(loc-1j)
        visited.add(loc)

    if move == 1:
        stack.sort(key=lambda x:x[1].real)
    elif move == -1:
        stack.sort(key=lambda x:-x[1].real)
    elif move == 1j:
        stack.sort(key=lambda x:x[1].imag)
    elif move == -1j:
        stack.sort(key=lambda x:-x[1].imag)

    while stack:
        val, loc = stack.pop()
        new_grid[int((loc+move).real)][int((loc+move).imag)] = val 
        new_grid[int(loc.real)][int(loc.imag)] = '.'
    
    return new_grid, new_loc+move


def get_score(grid):
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                score += 100*r+c
    return score

def get_score_2(grid):
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '[':
                score += 100*r+c
    return score

test_data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# test_data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

# test_data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""

with open('15_warehouse_woes.txt', 'r') as file:
    data = file.read() 

grid, moves, loc = string_to_mat(data)
wide_grid, wide_loc = rescale(grid)
for m in moves:
    grid, loc = make_move(grid, m, loc)
print(print_grid(grid))
print(get_score(grid))

for m in moves:
    wide_grid, wide_loc = make_move_2(wide_grid, wide_loc, m)
print(print_grid(wide_grid))
print(get_score_2(wide_grid))
print("--- %s seconds ---" % (time.time() - start_time))