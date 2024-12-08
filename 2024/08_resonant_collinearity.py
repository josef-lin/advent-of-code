import time
start_time = time.time()

def string_to_mat(s):
    return [list(row) for row in s.strip().split('\n')]

def count_antinode(mat):
    antennas = {}
    antinode = set()

    def in_bound(r,c):
        return 0 <= r < len(mat) and 0 <= c < len(mat[0])

    def make_antinode(key, antenna):
        for pos in antennas[key]:
            dr = antenna[0]-pos[0]
            dc = antenna[1]-pos[1]
            ### part 1
            # r_1 = pos[0]-dr
            # c_1 = pos[1]-dc
            # if in_bound(r_1,c_1):
            #     antinode.add((r_1, c_1))
            # r_2 = antenna[0]+dr
            # c_2 = antenna[1]+dc
            # if in_bound(r_2,c_2):
            #     antinode.add((r_2, c_2))

            ### part 2
            last_r = pos[0]
            last_c = pos[1]
            antinode.add((last_r, last_c))
            while True:
                last_r = last_r - dr
                last_c = last_c - dc
                if in_bound(last_r,last_c):
                    antinode.add((last_r, last_c))
                    if mat[last_r][last_c] == '.':
                        mat[last_r][last_c]='#'
                else:
                    break
            
            last_r = antenna[0]
            last_c = antenna[1]
            antinode.add((last_r, last_c))
            while True:
                last_r = last_r + dr
                last_c = last_c + dc
                if in_bound(last_r,last_c):
                    antinode.add((last_r, last_c))
                    if mat[last_r][last_c] == '.':
                        mat[last_r][last_c]='#'
                else:
                    break


    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] not in ['.','#']:
                if mat[r][c] in antennas:
                    make_antinode(mat[r][c],(r,c))
                    antennas[mat[r][c]].append((r,c))
                else:
                    antennas[mat[r][c]] = [(r,c)]
    
    return len(antinode)

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
with open('08_resonant_collinearity.txt', 'r') as file:
    input = file.read() 

data = string_to_mat(input)
print(count_antinode(data))
# for row in data:
#     print(''.join(row))
print("--- %s seconds ---" % (time.time() - start_time))