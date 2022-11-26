# Find all buy-sell pairs to maximize profit
# Use dp approach: find best profit in the range (start,end)
# values = [2,5,7,1,4,3,1]
values = [100, 180, 260, 310, 40, 535, 695]
n = len(values)
dp = [[(0,-1,-1) if i>=j else (-1,-1,-1) for j in range(n)] for i in range(n)]

def max_profit(start,end,level=0):
    if start>=end:return 0
    # print(' '*level,'Entering',start,end)
    if dp[start][end][0]!=-1:
        # print(' '*level,'Found, Exiting',start,end)
        return dp[start][end][0]
    profit = 0
    best_start = start
    best_end = start
    for i in range(start,end):
        for j in range(i+1,end+1):
            if values[j]>values[i]:
                # print(' '*level,'Trying',i,j)
                current_profit = values[j]-values[i]+max_profit(start,i-1,level+4)+max_profit(j+1,end,level+4)
                if current_profit>profit:
                    profit = current_profit
                    best_start = i
                    best_end = j
                # print(' '*level,'Done Tring',i,j)
    dp[start][end] = (profit,best_start,best_end)
    # print(' '*level,'Found, Exiting',start,end)
    return profit

max_val = max_profit(0,n-1)
print()
print('b\s',' '.join([f'{str(i):15s}' for i in range(n)]))
for j,elem in enumerate(dp):
    print(j,' ',' '.join([f'{str(i):15s}' for i in elem]))

index = 0
best_stocks = []
while index<n:
    if dp[index][n-1]==0:
        break
    best_stocks.append((dp[index][n-1][1],dp[index][n-1][2]))
    index = dp[index][n-1][2]+1
print('Chosen stocks:')
for elem in best_stocks:
    print(f'{elem}: {values[elem[1]]}-{values[elem[0]]} = {values[elem[1]]-values[elem[0]]}')
print('Total',max_val)