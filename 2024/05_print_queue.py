def generate_rules(rules_string):
    """
    generates a dictionary
    given a key, returns list of numbers that must come after it 
    """
    rules_dict = {}
    lines = rules_string.split('\n')
    for line in lines:
        x, y = line.split('|')
        if x in rules_dict:
            rules_dict[x].append(y)
        else:
            rules_dict[x] = [y]
    return rules_dict

def total_score_correct(rules, updates):
    updates = updates.split('\n')
    total = 0

    def update_score(update):
        order = update.split(',')
        # order = [item.strip() for item in order if item.strip()]
        for i in range(len(order)):
            temp = order[:i]
            for item in temp:
                if rules.get(order[i]) and item in rules.get(order[i]):
                    # print(item, order[i], rules.get(order[i]))
                    return 0
        return int(order[int((len(order)-1)/2)])
    
    for update in updates:
        total += update_score(update)
    
    return total

def total_score_incorrect(rules, updates):
    updates = updates.split('\n')
    total = 0

    def update_score(update):
        order = update.split(',')
        updated = False
        for i in range(len(order)):
            temp = order[:i]
            for item in temp:
                # Check if item is in the rules and swap it with order[i], keep swapping until rules are satisfied
                if rules.get(order[i]) and item in rules.get(order[i]):
                    updated = True
                    # Swap item and order[i] using their indices
                    item_index = order.index(item)  # Find the index of item in the list
                    order[i], order[item_index] = order[item_index], order[i]
        return 0 if not updated else int(order[len(order)//2])

    for update in updates:
        total += update_score(update)
    return total

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
with open('05_print_queue.txt', 'r') as file:
    data = file.read() 

# Split the data by double newlines to separate the different blocks
blocks = data.split('\n\n')

rules = generate_rules(blocks[0])
score_correct = total_score_correct(rules, blocks[1])
print(score_correct)
score_incorrect = total_score_incorrect(rules, blocks[1])
print(score_incorrect)

