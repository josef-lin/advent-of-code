def invalid_id_double(ids):
    total = 0
    for product_range in ids:
        start, end = product_range
        for id_num in range(start, end + 1):
            str_id = str(id_num)
            length = len(str_id)
            if length % 2 == 1:
                continue
            if str_id[:length // 2] != str_id[length // 2:]:
                continue
            total += id_num
    return total

def invalid_id_mult(ids):
    total = 0
    for product_range in ids:
        start, end = product_range
        for id_num in range(start, end + 1):
            valid = True
            str_id = str(id_num)
            length = len(str_id)
            for mult in range(1, length // 2 + 1):
                if length % mult != 0:
                    continue
                first_part = str_id[:mult]
                if first_part * (length // mult) == str_id:
                    valid = False
            if not valid:
                total += id_num
    return total

test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

input_file = open('02-gift-shop.txt')
ids = []
for product_range in input_file.read().split(','):
    parts = product_range.split('-')
    start = int(parts[0])
    end = int(parts[1])
    ids.append((start, end))
        
print(invalid_id_double(ids))
print(invalid_id_mult(ids))