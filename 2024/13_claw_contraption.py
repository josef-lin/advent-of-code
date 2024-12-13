import numpy as np
import time
start_time = time.time()

np.set_printoptions(formatter={'all': lambda x: f'{x:.0f}'}) 

def input_to_blocks(data):
    def extract_button(line):
        parts = line.split(',')
        return [int(parts[0].split('X+')[1]),int(parts[1].split('Y+')[1])]
   
    def extract_prize(line):
        parts = line.split(',')
        return [int(parts[0].split('X=')[1]),int(parts[1].split('Y=')[1])] 
    
    blocks = data.strip().split('\n\n')
    buttons = []
    prizes = []
    for block in blocks:
        lines = block.split('\n')
        buttons.append(np.array([extract_button(lines[0]), extract_button(lines[1])], dtype=np.float64))
        prize = np.array(extract_prize(lines[2]), dtype = np.float64)
        # prize += np.array([10000000000000,10000000000000], dtype = np.float64)
        prizes.append(prize)

    return buttons, prizes

def solve(buttons, prizes):
    i = 0
    costs = np.array([[3,1]])
    cost = [0]
    while i < len(buttons):
        button = buttons[i]
        prize = prizes[i]
        presses = np.dot(np.linalg.inv(button.T),prize)
        # presses = np.round(presses) 
        check_integral = np.all([np.isclose(x,round(x)) for x in presses])
        # equal = np.array_equal(prize, np.dot(button.T,presses))
        if check_integral:
        # if equal:
            cost += np.dot(costs,presses)
        i += 1
    return cost 

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open('13_claw_contraption.txt', 'r') as file:
    data = file.read() 

buttons, prizes = input_to_blocks(data)
print(solve(buttons, prizes))

print("--- %s seconds ---" % (time.time() - start_time))