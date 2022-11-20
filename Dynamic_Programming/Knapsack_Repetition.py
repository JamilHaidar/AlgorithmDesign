total_weight = 10
items = [(30,6),(14,3),(16,4),(9,2)]
dp = [0 for _ in range(total_weight + 1)]
ans = 0
chosen_indices = [-1 for _ in range(total_weight+1)]
for weight in range(total_weight + 1):
    chosen_idx = -1
    for item_idx in range(len(items)):
        if items[item_idx][1] <= weight:
            if dp[weight] < dp[weight-items[item_idx][1]]+items[item_idx][0]:
                dp[weight] = dp[weight-items[item_idx][1]]+items[item_idx][0]
                chosen_idx = item_idx
    if chosen_idx!=-1:
        chosen_indices[weight] = chosen_idx
print('dp:',dp)
print(f'Best value: {dp[total_weight]}')
weight = total_weight
chosen_items = []
while chosen_indices[weight]!=-1:
    chosen_items.append(items[chosen_indices[weight]])
    weight -= items[chosen_indices[weight]][1]
print('Chosen items:',chosen_items)


