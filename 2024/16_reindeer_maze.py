import heapq
import time
start_time = time.time()

def string_to_mat(s):
    grid = []
    start = None
    end = None
    for r, line in enumerate(s.split('\n')):
        row = [char for char in line]
        grid.append(row)
        if start == None or end == None:
            for c, char in enumerate(row):
                if char == 'S':
                    start = r+c*1j
                    break
                elif char == 'E':
                    end = r+c*1j
                    break
    return grid, start, end

def print_grid(grid):
    s = ''
    for row in grid:
        for char in row:
            s += char
        s += '\n'
    return s

class Position:
    def __init__(self, f_score, g_score, curr, path):
        self.f_score = f_score
        self.g_score = g_score
        self.curr = curr
        self.path = path

    def __lt__(self, other):
        if self.f_score == other.f_score:
            return self.g_score < other.g_score
        return self.f_score < other.f_score

def search(grid, start, end):
    def h_score(curr):
        pos, facing = curr
        diff = pos - end
        if facing in [-1, 1j]:
            turn = 1000
        else:
            turn = 2000
        return turn + abs(diff.real) + abs(diff.imag)
    def neighbor(curr):
        pos, facing = curr
        neighbors = []
        if facing.real == 0:
            neighbors += [(pos,1), (pos,-1)]
        else:
            neighbors += [(pos,1j), (pos,-1j)]
        forward = pos+facing
        if grid[int(forward.real)][int(forward.imag)] != '#':
            neighbors += [(forward, facing)]
        return neighbors
    open_list = []
    # heapq.heappush(open_list, Position(0+h_score((start,1j)), 0, (start, 1j)))
    heapq.heappush(open_list, Position(0+h_score((start,1j)), 0, (start, 1j), [(start, 1j)]))
    # came_from = {}
    g_score = {(start,1j):0}
    all_paths = {(start,1j):[[(start, 1j)]]}
    start_to_end = []
    final_cost = float('inf')
    while open_list:
        obj = heapq.heappop(open_list)
        cost, curr, path = obj.g_score, obj.curr, obj.path
        pos, facing = curr
        if pos == end:
            if cost < final_cost:
                final_cost = cost
                start_to_end = [path]
            elif cost == final_cost:
                start_to_end.append(path)
        if cost < final_cost:
            for n in neighbor(curr):
                if n[1] != facing:
                    tentative_g = cost + 1000
                else:
                    tentative_g = cost + 1
                if n not in g_score or tentative_g <= g_score[n]:
                    g_score[n] = tentative_g
                    f_score = tentative_g + h_score(n)
                    heapq.heappush(open_list, Position(f_score, tentative_g, n, path+[n]))
                    # came_from[n] = (pos, facing)
                    all_paths[n] = [path+[n]]
                elif tentative_g == g_score[n]:
                    all_paths[n].append(path+[n])
    return start_to_end, final_cost

test_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
# test_data = """#####
# ###E#
# #...#
# #.#.#
# #...#
# #S###
# #####"""

with open('16_reindeer_maze.txt', 'r') as file:
    data = file.read() 

grid, start, end = string_to_mat(data)
print(print_grid(grid))
visited = []
paths, cost = search(grid, start, end)
print(cost)
for path in paths:
    for curr in path:
        grid[int(curr[0].real)][int(curr[0].imag)] = 'O'
        if curr[0] not in visited:
            visited.append(curr[0])
# print(visited)
print(len(visited))
print(print_grid(grid))
print("--- %s seconds ---" % (time.time() - start_time))