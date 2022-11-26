#Goal: determine if there is a subset of the given set with sum equal to given sum
values = [2,5,4,10,7]
sum = 6
subsums = {sum}
found = False
for value in values:
    for subsum in list(subsums):
        if subsum-value<0:continue
        if subsum-value==0:
            found=True
            subsums.add(subsum-value)
            break
        subsums.add(subsum-value)
    if found:break
print('Found:',found)