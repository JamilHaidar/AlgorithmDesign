# (value,weight,volume)
items = [(1,1,1),(6,2,10),(18,5,3),(22,6,2),(28,7,2)]
total_weight = 11
total_volume = 15
# Initialize opt table
opt = [[[0 for _ in range(total_volume+1)] for _ in range(total_weight+1)] for _ in range(len(items)+1)]
# Populate opt table
for item_idx in range(len(items)):
    for weight in range(1,total_weight+1):
        for volume in range(1,total_volume+1):
            if items[item_idx][1]>weight or items[item_idx][2]>volume:
                opt[item_idx+1][weight][volume] = opt[item_idx][weight][volume]
            else:
                opt[item_idx+1][weight][volume] = max(opt[item_idx][weight][volume],items[item_idx][0]+opt[item_idx][weight-items[item_idx][1]][volume-items[item_idx][2]])

# Print best solution
print(f'Best value is {opt[len(items)][total_weight][total_volume]}')
weight = total_weight
volume = total_volume
item_idx = len(items)
chosen_items = []
while weight!=0 and volume!=0 and item_idx>0:
    if opt[item_idx][weight][volume]!=opt[item_idx-1][weight][volume]:
        chosen_items.append(items[item_idx-1])
        weight -= items[item_idx-1][1]
        volume -= items[item_idx-1][2]
    item_idx-=1
print(f'Total weight used: {total_weight-weight}, Total volume used: {total_volume-volume}')
print('Items chosen were: ',chosen_items)



