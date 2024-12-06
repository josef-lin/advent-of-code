def string_to_mat(s):
    return [list(row) for row in s.strip().split('\n')]

turn_right = {'^':'>', '>':'v', 'v':'<', '<':'^'}
directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

def get_inital_pos(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                return(i, j)
    return None

def get_path(data):
    pos = get_inital_pos(data)
    data = [row[:] for row in data]
    if pos == None:
        return None
    dir = '^'
    path = set()
    while True:
        path.add(pos)
        data[pos[0]][pos[1]]=dir
        next_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        if not (0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0])):
            break
        while data[next_pos[0]][next_pos[1]] in ['#','O']:
            dir = turn_right[dir]
            data[pos[0]][pos[1]]=dir
            next_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        data[pos[0]][pos[1]] = 'X'
        pos = next_pos
    return path

def check_loop(data):
    pos = get_inital_pos(data)
    if pos == None:
        return None
    dir = '^'
    obstacles = set()
    while True:
        next_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        if not (0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0])):
            break
        while data[next_pos[0]][next_pos[1]] in ['#','O']:
            if ((pos,dir) in obstacles):
                return True
            else:
                obstacles.add((pos,dir))
            dir = turn_right[dir]
            next_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        pos = next_pos
    return False

def count_obstruction_pos(data):
    count = 0
    path = get_path(data)
    for pos in path:
        new_data = [row[:] for row in data]
        new_data[pos[0]][pos[1]] = 'O'
        if check_loop(new_data):
            count += 1
    return count

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
with open('06_guard_gallivant.txt', 'r') as file:
    input = file.read() 

data = string_to_mat(input)
print(len(get_path(data)))
print(count_obstruction_pos(data))
