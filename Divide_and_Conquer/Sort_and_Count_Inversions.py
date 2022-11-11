# Merge two sorted lists while counting inversions
def merge_and_count(A,B):
    # Total amount of iterations
    total_length = len(A)+len(B)
    merged_list = []
    inversions = 0
    while len(merged_list)!=total_length:
        # Check if one of the lists is empty, done
        if len(A)==0:
            merged_list+=B
            break
        elif len(B)==0:
            merged_list+=A
            break
        # Check left array for inversion
        elif A[0]<=B[0]:
            merged_list.append(A.pop(0))
        else:
            merged_list.append(B.pop(0))
            inversions+=len(A)
    return inversions,merged_list

def sort_and_count(L):
    # Base case: 0 inversions for 1 element list
    if len(L)==1:
        return (0,L)
    # Split list left and right
    left = L[:len(L)//2]
    right = L[len(L)//2:]
    # Sort each list while counting inversions
    left_inversions, left_list = sort_and_count(left)
    right_inversions, right_list = sort_and_count(right)
    # Merge sorted lists while counting inversions
    merging_inversions, L = merge_and_count(left_list,right_list)
    # Return total amount of inversions with sorted and merged list
    return (left_inversions+right_inversions+merging_inversions,L)
songs = [1,5,4,8,10,2,6,9,12,11,3,7]
print(sort_and_count(songs)[0])