import time
start_time = time.time()

### part 1
def disk_to_block(input):
    id = 0
    i = 0
    block = []
    id_count = []
    spaces = []
    while i < len(input):
        if i % 2 == 0:
            id_count.append([int(input[i]),len(block)])
            block += [id]*int(input[i])
        else:
            spaces.append([int(input[i]),len(block)])
            block += [None]*int(input[i])
            id += 1
        i += 1
    return block, id_count, spaces

def move_block1(block):
    moved = block[:]
    i = 0
    j = len(moved)-1
    while i < j:
        while moved[i] != None:
            i += 1
        while moved[j] == None:
            j -= 1
        if i < j:
            moved[i] = moved[j]
            moved[j] = None
    return moved

### part 2

def move_block2(block, id_count, spaces):
    moved = block[:]
    last_id = len(id_count)-1
    while last_id > 0:
        for i, arr in enumerate(spaces[:last_id]):
            space, index = arr
            if space >= id_count[last_id][0]:
                moved[index:index+id_count[last_id][0]] = moved[id_count[last_id][1]:id_count[last_id][1]+id_count[last_id][0]]
                moved[id_count[last_id][1]:id_count[last_id][1]+id_count[last_id][0]] = [None]*id_count[last_id][0]
                spaces[i] = [space - id_count[last_id][0],index + id_count[last_id][0]]
                break
        last_id -= 1
    return moved

def find_sum(block):
    i = 0
    sum = 0
    while i<len(block):
        if block[i] != None:
            sum += block[i]*i
        i += 1
    return sum 

test_data = "2333133121414131402"
with open('09_disk_fragmenter.txt', 'r') as file:
    input = file.read() 

block, id_count, spaces = disk_to_block(input)
print(find_sum(move_block1(block)))
print(find_sum(move_block2(block,id_count,spaces)))
print("--- %s seconds ---" % (time.time() - start_time))