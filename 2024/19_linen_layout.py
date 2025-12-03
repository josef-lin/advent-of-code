import time
start_time = time.time()

def input_to_patterns_designs(data):
    blocks = data.strip().split('\n\n')
    patterns = blocks[0].split(', ')
    designs = blocks[1].split('\n')
    return patterns, designs

def solve(patterns, designs):
    cache = {} 
    def check(design):
        valid = False
        if design in cache:
            return cache[design]
        for p in patterns:
            if design == p:
                cache[design] = True
                return True
            if design[0:len(p)] == p:
                valid = check(design[len(p):])
        cache[design] = valid
        return valid


    count = 0
    for design in designs: 
        if check(design):
            print(design)
            count += 1
    return count 

test_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

with open('19_linen_layout.txt', 'r') as file:
    data = file.read() 

patterns, designs = input_to_patterns_designs(data)
print(len(patterns))
print(len(designs))
print(solve(patterns, designs))

print("--- %s seconds ---" % (time.time() - start_time))