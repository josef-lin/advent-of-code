def count_fresh(ranges, ids):
    count = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                count += 1
                break
    return count

def count_fresh_range(ranges):
    ranges.sort(key=lambda x: x[0])

    fresh_ids = []
    for a, b in ranges:
        if not fresh_ids or a > fresh_ids[-1][1] + 1:
            fresh_ids.append([a, b])
        else: 
            fresh_ids[-1][1] = max(fresh_ids[-1][1], b)
    
    return sum(b - a + 1 for a, b in fresh_ids)


test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

ranges = []
ids = []

input_file = open('05-cafeteria.txt')
ranges_input, ids_input = input_file.read().split('\n\n')
for line in ranges_input.strip().split('\n'):
    parts = line.split('-')
    ranges.append([int(parts[0]), int(parts[1])])

for line in ids_input.strip().split('\n'):
    ids.append(int(line.strip()))

# ranges_input,  ids_input = test.split('\n\n')
# for line in ranges_input.strip().split('\n'):
#     parts = line.split('-')
#     ranges.append([int(parts[0]), int(parts[1])])

# for line in ids_input.strip().split('\n'):
#     ids.append(int(line.strip()))

print(ranges)

print(count_fresh(ranges, ids))
print(count_fresh_range(ranges))