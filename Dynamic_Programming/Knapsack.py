# (value,weight)
items = [(1,1),(6,2),(18,5),(22,6),(28,7)]
total_weight = 11
# Initialize opt table
opt = [[0 for _ in range(total_weight+1)] for _ in range(len(items)+1)]
# Populate opt table
for item_idx in range(len(items)):
    for weight in range(1,total_weight+1):
        if items[item_idx][1]>weight:
            opt[item_idx+1][weight] = opt[item_idx][weight]
        else:
            opt[item_idx+1][weight] = max(opt[item_idx][weight],items[item_idx][0]+opt[item_idx][weight-items[item_idx][1]])        
# Print table
print('Opt table:')
header = ' '.join([f'{str(elem):3s}' for elem in range(total_weight+1)])
print('   '+header)
print(' '+'-'*(len(header)+2))
for i,row in enumerate(opt):
    print(f'{i}| '+' '.join([f'{str(elem):3s}' for elem in row]))

# Print best solution
print(f'Best value is {opt[len(items)][total_weight]}')
weight = 11
item_idx = len(items)
chosen_items = []
while weight!=0:
    if opt[item_idx][weight]!=opt[item_idx-1][weight]:
        chosen_items.append(items[item_idx-1])
        weight -= items[item_idx-1][1]
    item_idx-=1
print('Items chosen were: ',chosen_items)