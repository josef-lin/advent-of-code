import time
start_time = time.time()

def string_to_mat(s):
    return [list(row) for row in s.split('\n')]

def find_regions(data):
    dir = [-1, 1, -1j, 1j]
    unaccounted = {x + y * 1j for y in range(len(data)) for x in range(len(data[y]))}
    regions = {}

    def in_bound(point):
        return 0 <= point.real < len(data[0]) and 0 <= point.imag < len(data)

    while unaccounted:
        curr_pos = next(iter(unaccounted))
        char = data[int(curr_pos.real)][int(curr_pos.imag)]
        regions[(char, curr_pos)] = {curr_pos}
        stack = [curr_pos]
        visited = set()
        while stack:
            pos = stack.pop()
            if pos not in visited and pos in unaccounted:
                visited.add(pos)
                if data[int(pos.real)][int(pos.imag)] == char:
                    regions[(char, curr_pos)].add(pos)
                    unaccounted.remove(pos)
                    for d in dir:
                        next_pos = pos+d
                        if in_bound(next_pos):
                            stack.append(next_pos)
    return regions

def get_ans1(regions):
    ans = 0
    dir = [-1, 1, -1j, 1j]
    peri_add = [4,2,0,-2,-4]
    for key in regions:
        area = len(regions[key])
        perimeter = 0
        counted = set()
        while regions[key]:
            pos = regions[key].pop()
            count = 0 
            for d in dir:
                if pos+d in counted:
                    count += 1
            perimeter += peri_add[count]
            counted.add(pos)
        ans += area*perimeter
    return ans

def get_ans2(regions):
    ans = 0
    check_dir = [[-1,-1j],[-1,1j],[1,-1j],[1,1j]]
    for key in regions:
        area = len(regions[key])
        corners = 0
        for pos in regions[key]:
            for dirs in check_dir:
                if ((pos+dirs[0] in regions[key] and pos+dirs[1] in regions[key] and pos+dirs[0]+dirs[1] not in regions[key]) 
                    or (pos+dirs[0] not in regions[key] and pos+dirs[1] not in regions[key])):
                    corners += 1
        ans += area*corners
    return ans

# test_data = """AAAA
# BBCD
# BBCC
# EEEC"""

test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

with open('12_garden_groups.txt', 'r') as file:
    data = file.read() 

data = string_to_mat(data)
regions = find_regions(data)
print(get_ans1(regions))
regions = find_regions(data)
print(get_ans2(regions))
print("--- %s seconds ---" % (time.time() - start_time))