# (value,weight,volume)
items = [(1,1,1),(6,2,10),(18,5,3),(22,6,2),(28,7,2)]
total_weight = 11
total_volume = 15
# Initialize opt table
opt = [[(0,0) for _ in range(total_weight+1)] for _ in range(len(items)+1)]
# Populate opt table
for item_idx in range(len(items)):
    for weight in range(1,total_weight+1):
        if items[item_idx][1]>weight:
            opt[item_idx+1][weight] = opt[item_idx][weight]
        else:
            include_val = items[item_idx][0]+opt[item_idx][weight-items[item_idx][1]][0]
            exclude_val = opt[item_idx][weight][0]
            if include_val<exclude_val:
                opt[item_idx+1][weight] = opt[item_idx][weight]
            else:
                new_volume = items[item_idx][2]+opt[item_idx][weight-items[item_idx][1]][1]
                if new_volume>total_volume:
                    opt[item_idx+1][weight] = opt[item_idx][weight]
                else:
                    opt[item_idx+1][weight] = (include_val,new_volume)
# Print table
print('Opt table:')
header = ' '.join([f'{str(elem):9s}' for elem in range(total_weight+1)])
print('   '+header)
print(' '+'-'*(len(header)+2))
for i,row in enumerate(opt):
    print(f'{i}| '+' '.join([f'{str(elem):9s}' for elem in row]))

# Print best solution
print(f'Best value is {opt[len(items)][total_weight][0]}')
weight = total_weight
volume = total_volume
item_idx = len(items)
chosen_items = []
while weight!=0 and volume!=0 and item_idx>0:
    if opt[item_idx][weight][0]!=opt[item_idx-1][weight][0]:
        chosen_items.append(items[item_idx-1])
        weight -= items[item_idx-1][1]
        volume -= items[item_idx-1][2]
    item_idx-=1
print(f'Total weight used: {total_weight-weight}, Total volume used: {total_volume-volume}')
print('Items chosen were: ',chosen_items)



