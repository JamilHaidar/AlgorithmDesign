# Exercise from Fall 2019
# Given prices of rods of specific lengths (length 1, price 1), (length 2, price 5), etc.
# Find best way to cut a rod to get most price out of it 

# Initialize price list (0 added for rod size 0)
# prices = [0,2,1,8,9,10,17,17,20,24,30] # Uncomment this to see final cuts raveled
prices = [0,1,5,8,9,10,17,17,20,24,30]
# Initialize best known rod prices
dp={0:prices[0],1:prices[1]}
# Initialize best known cuts for each rod length
best_cuts={0:(0,0),1:(0,1)}

def cut(rod):
    # If subproblem already solved, return its solution
    if rod in dp:
        return dp[rod]
    # Initialize best price to not cutting rod
    max_price = prices[rod]
    # Initialize best cut to not cutting rod
    best_cuts[rod] = (0,rod)
    # Loop over possible first slices
    for first_slice in range(1,rod//2 + 1):
        second_slice = rod-first_slice
        # Get optimal price of first slice
        if first_slice not in dp:
            dp[first_slice] = cut(first_slice)
        # Get optimal price of first slice
        if second_slice not in dp:
            dp[second_slice] = cut(second_slice)
        # If found a better price using these slices, use them
        if max_price<dp[first_slice]+dp[second_slice]:
            max_price = dp[first_slice]+dp[second_slice]
            best_cuts[rod] = (first_slice,second_slice)
    return max_price
n = 10
dp[n] = cut(n)
print(dp[n])
for rod_length in range(n,0,-1):
    print(f'rod_length: {rod_length}, best price: {dp[rod_length]}, cuts: {best_cuts[rod_length]}')
    total_cuts = []
    cuts = [best_cuts[rod_length]]
    while len(cuts)>0:
        elem = cuts.pop()
        if elem[0]==0:
            total_cuts.append(elem[1])
        else:
            cuts.append(best_cuts[elem[0]])
            cuts.append(best_cuts[elem[1]])
    total_cuts = sorted(total_cuts)
    print(f'Total cuts:',total_cuts)