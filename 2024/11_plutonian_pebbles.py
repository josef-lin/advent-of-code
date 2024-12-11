import time
start_time = time.time()

def string_to_list(s):
    return [int(num) for num in s.split(' ')]

def evolve(data):
    # MAX_ITER = 25
    # MAX_ITER = 75
    MAX_ITER = 250
    counter = {num:1 for num in data}
    i = 0
    while i < MAX_ITER:
        new_counter = {}
        for num, count in counter.items():
            if num == 0:
                new_counter[1] = count + new_counter.get(1,0)
            elif len(str(num)) % 2 == 0:
                half = len(str(num)) // 2
                left = int(str(num)[:half])
                right = int(str(num)[half:]) 
                new_counter[left] = count + new_counter.get(left,0)
                new_counter[right] = count + new_counter.get(right,0)
            else:
                new_counter[2024*num] = count + new_counter.get(2024*num,0)
        counter = new_counter
        i += 1
    return sum(counter[num] for num in counter)


test_data = """125 17"""
with open('11_plutonian_pebbles.txt', 'r') as file:
    data = file.read() 

data = string_to_list(data)
print(evolve(data))
print("--- %s seconds ---" % (time.time() - start_time))