import heapq
import time
start_time = time.time()

def string_to_mat(s):
    corrupted = []
    lines = s.split('\n')
    for line in lines:
        loc = line.split(',')
        corrupted.append(int(loc[0])+int(loc[1])*1j)
    return corrupted

def print_grid(curr_corrupted, size=70, path = [], queue = []):
    curr_corrupted = set(curr_corrupted)
    path = set(path)
    queue = set([q.pos for q in queue])
    s = ''
    for i in range(size+1):
        for j in range(size+1):
            if i+j*1j in curr_corrupted:
                s += '#'
            elif i+j*1j in path:
                s += 'O'
            elif i+j*1j in queue:
                s += 'X'
            else: 
                s += '.'
        s += '\n'
    return s

class Position:
    def __init__(self, f_score, g_score, pos, path):
        self.f_score = f_score
        self.g_score = g_score
        self.pos = pos
        self.path = path

    def __lt__(self, other):
        if self.f_score == other.f_score:
            return self.g_score < other.g_score
        return self.f_score < other.f_score

def search(corrupted, size=70):
    corrupted = set(corrupted)
    start = 0
    end = size + size*1j
    dir = [1,-1,1j,-1j]

    def in_bound(pos):
        return 0 <= pos.real <= size and 0 <= pos.imag <= size

    def h_score(pos):
        diff = end - pos
        return diff.real + diff.imag
    
    def neighbor(pos):
        neighbors = []
        for d in dir:
            potential = pos+d
            if potential not in corrupted and in_bound(pos):
                neighbors.append(potential)
        return neighbors
    
    open_list = []
    heapq.heappush(open_list, Position(h_score(start), 0, start, [start]))
    came_from = {}
    g_score = {start:0}
    while open_list:
        obj = heapq.heappop(open_list)
        cost, pos, path = obj.g_score, obj.pos, obj.path
        if pos == end:
            return set(path), cost
        for n in neighbor(pos):
            tentative_g = cost + 1
            if n not in g_score or tentative_g < g_score[n]:
                g_score[n] = tentative_g
                f_score = tentative_g + h_score(n)
                heapq.heappush(open_list, Position(f_score, tentative_g, n, path+[n]))
                came_from[n] = pos
        # print(print_grid(corrupted,size,path,open_list))
    return None, cost

test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

with open('18_ram_run.txt', 'r') as file:
    data = file.read() 

corrupted = string_to_mat(data)
print(corrupted)
print(print_grid(corrupted[:1024]))
path, cost = search(corrupted[:1024])
lower, higher = 1024, len(corrupted)
guess = (higher+lower)//2 
while lower < guess < higher:
    path, cost = search(corrupted[:guess])
    if not path:
        higher = guess
    else:
        lower = guess
    guess = (higher+lower)//2
    
print(lower, guess, higher)
print(corrupted[lower])
print("--- %s seconds ---" % (time.time() - start_time))