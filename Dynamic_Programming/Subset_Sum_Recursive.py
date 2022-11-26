#Goal: determine if there is a subset of the given set with sum equal to given sum
values = [2,5,4,10,7]
sum = 6
def is_subset_sum(n,current_sum):
    if current_sum==0:return True 
    if n==0:return False
    if values[n-1]>sum: return is_subset_sum(n-1,sum)
    return is_subset_sum(n-1,current_sum) or is_subset_sum(n-1,current_sum-values[n-1])
print(is_subset_sum(len(values),sum))