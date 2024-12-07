import time
start_time = time.time()

def get_data(string):
    data = []
    lines = string.split('\n')
    for line in lines:
        target, line_input = line.split(':')
        target = int(target)
        line_input = line_input.split()
        line_input = [int(val) for val in line_input]
        data.append([target, line_input])
    return data

def possible_ans_1(target, vals):
    if len(vals) == 1:
        possible = [vals[0]]
    elif len(vals) == 2:
        possible = [vals[0]+vals[1], vals[0]*vals[1]]
    else:
        sum_results = possible_ans_1(target, [vals[0]+vals[1]]+vals[2:])
        prod_results = possible_ans_1(target, [vals[0]*vals[1]]+vals[2:])
        possible = sum_results+prod_results
    possible = [p for p in possible if p <= target]
    return possible

def possible_ans_2(target, vals):
    if len(vals) == 1:
        possible = [vals[0]]
    elif len(vals) == 2:
        possible = [vals[0]+vals[1], vals[0]*vals[1], int(str(vals[0])+str(vals[1]))]
    else:
        sum_results = possible_ans_2(target, [vals[0]+vals[1]]+vals[2:])
        prod_results = possible_ans_2(target, [vals[0]*vals[1]]+vals[2:])
        cat_results = possible_ans_2(target, [int(str(vals[0])+str(vals[1]))]+vals[2:])
        possible = sum_results+prod_results+cat_results
    possible = [p for p in possible if p <= target]
    return possible

def total_calibration_result(data):
    total_1 = 0
    total_2 = 0
    # target is the first element, values are a list, second element
    for d in data:
        possible_1 = possible_ans_1(d[0], d[1])
        if d[0] in possible_1:
            total_1 += d[0]
            total_2 += d[0]
            continue
        possible_2 = possible_ans_2(d[0], d[1])
        if d[0] in possible_2:
            total_2 += d[0]
    return total_1, total_2

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open('07_bridge_repair.txt', 'r') as file:
    input_data = file.read() 

data = get_data(input_data)
print(total_calibration_result(data))
print("--- %s seconds ---" % (time.time() - start_time))