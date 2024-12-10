import time
start_time = time.time()

def string_to_mat(s):
    return [[int(num) for num in list(row)] for row in s.split('\n')]

def score_trail(data):
    dir = [-1, 1, -1j, 1j]
    num_rows = len(data)
    num_cols = len(data[0])
    trails1 = {}
    trails2 = {}
    def in_bound(pos):
        return 0 <= pos.real < num_rows and 0 <= pos.imag < num_cols

    def add_trail(head, pos, curr):
        if data[int(pos.real)][int(pos.imag)] == curr:
            if curr == 9:
                if head in trails1:
                    trails1[head].add(pos)
                    trails2[head].append(pos)
                else:
                    trails1[head] = set([pos])
                    trails2[head] = [pos]
            for d in dir:
                next_pos = pos + d
                if in_bound(next_pos):
                    add_trail(head, next_pos, curr+1)

    for r in range(num_rows):
        for c in range(num_cols):
            curr = 0
            pos = r + c*1j
            add_trail(pos,pos,curr)

    count1 = 0
    count2 = 0
    for pos in trails1:
        count1 += len(trails1[pos])
        count2 += len(trails2[pos])
    return count1, count2

test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
with open('10_hoof_it.txt', 'r') as file:
    input = file.read() 

data = string_to_mat(input)
print(score_trail(data))
print("--- %s seconds ---" % (time.time() - start_time))