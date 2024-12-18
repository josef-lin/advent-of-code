import math
import time
start_time = time.time() 

def parse_input(data):
    blocks = data.split('\n\n')
    register = []
    program = []
    for line in blocks[0].split('\n'):
        parts = line.split(': ')
        register.append(int(parts[1]))
                        
    blocks[1] = blocks[1].split(': ')[1]
    program = [int(i) for i in blocks[1].split(',')]

    return register, program

class Solver:
    def __init__(self, register, program):
        self.instruction_pointer = 0
        self.s = ''
        self.register = register
        self.program = program 
        self.combo_operand = {0:0, 1:1, 2:2, 3:3, 4:self.register[0], 5:self.register[1], 6:self.register[2], 7: None}

    def adv(self, x):
        self.register[0] = self.register[0]//(2**self.combo_operand[x])
    def bxl(self, x):
        self.register[1] = self.register[1]^x
    def bst(self, x):
        self.register[1] = self.combo_operand[x] % 8
    def jnz(self, x):
        if self.register[0] != 0:
            self.instruction_pointer = x - 1
    def bxc(self, x):
        self.register[1] = self.register[1]^self.register[2]
    def out(self, x):
        val = self.combo_operand[x]%8
        self.s += str(val) + ','
    def bdv(self, x):
        self.register[1] = self.register[0]//(2**self.combo_operand[x])
    def cdv(self, x):
        self.register[2] = self.register[0]//(2**self.combo_operand[x])
    
    def solve(self):
        opcodes = {0: self.adv,
              1: self.bxl,
              2: self.bst,
              3: self.jnz, 
              4: self.bxc,
              5: self.out,
              6: self.bdv,
              7: self.cdv}
        while self.instruction_pointer < len(self.program):
            self.combo_operand = {0:0, 1:1, 2:2, 3:3, 4:self.register[0], 5:self.register[1], 6:self.register[2], 7: None}
            opcode = self.program[self.instruction_pointer]
            self.instruction_pointer += 1
            operand = self.program[self.instruction_pointer]
            opcodes[opcode](operand)
            self.instruction_pointer += 1
        return self.register, self.s[:-1]

def step(A):
    B = A % 8
    B = B ^ 3
    C = A // (2**B)
    B = B ^ 5
    B = B ^ C
    return B % 8

def test_step(A):
    A = A // 8
    return A % 8

for i in range(8):
    print(step(i))

def find(A, digit = 0):
    if step(A) != program[-(digit+1)]:
    # if test_step(A) != program[-(digit+1)]:
        return 
    
    if digit == len(program) - 1:
        As.append(A)
    else:
        print(A)
        for B in range(8):
            find(A*8+B, digit + 1)

test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

test_data = """Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

with open('17_chronospatial_computer.txt', 'r') as file:
    data = file.read() 

register, program = parse_input(data)
p = Solver(register, program)
print(register)
print(program)
print(p.solve())
As = []
for a in range(8):
    find(a)
print(As)

print("--- %s seconds ---" % (time.time() - start_time))