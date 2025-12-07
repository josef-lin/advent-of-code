def count(input):
    count_splits = 0
    rows = input.split('\n')
    beam_locations = []
    beam_locations.append({rows[0].find('S')})
    curr_row = 1
    while curr_row < len(rows):
        beam_locations.append(set())
        for loc in beam_locations[curr_row-1]:
            if rows[curr_row][loc] == '^':
                beam_locations[curr_row].add(loc + 1)
                beam_locations[curr_row].add(loc - 1)
                count_splits += 1
            else:
                beam_locations[curr_row].add(loc)
        curr_row += 1

    curr_row = len(rows)-1
    count_timelines = [[0 for _ in range(len(rows[0]))] for _ in range(len(rows))]
    for i in range(len(rows[0])):
        if i in beam_locations[curr_row]:
            count_timelines[curr_row][i] = 1

    while curr_row > 0:
        for loc in beam_locations[curr_row-1]:
            count_timelines[curr_row-1][loc] += count_timelines[curr_row][loc] 
            if rows[curr_row][loc] == '^':
                count_timelines[curr_row-1][loc] += (count_timelines[curr_row][loc - 1] + count_timelines[curr_row][loc + 1])
        curr_row -= 1
    return count_splits, sum(count_timelines[0])

test = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input_file = open('07-laboratories.txt')

# print(count(test))
print(count(input_file.read()))