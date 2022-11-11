# find maximum weight subset of mutually compatible jobs
tasks = [(1,4,1),(3,5,2),(0,6,3),(4,7,4),(3,8,5),(5,9,6),(6,10,7),(8,11,8)]
tasks = sorted(tasks,key = lambda x:x[1])

opt = [-1]*len(tasks)
cached_nearest = {}

def nearest(idx):
    nearest = idx-1
    while nearest>-1:
        if tasks[nearest][1]<=tasks[idx][0]:
            cached_nearest[idx] = nearest
            return nearest
        nearest-=1
    cached_nearest[idx] = -1
    return -1
def find_schedule(idx):
    if idx==-1:return 0
    if opt[idx]==-1:
        opt[idx] = max(tasks[idx][2]+find_schedule(nearest(idx)),find_schedule(idx-1))
    return opt[idx]

print('Best schedule weight is: ',find_schedule(len(tasks)-1))

chosen_tasks = []
idx = len(tasks)-1
while idx!=-1:
    if opt[idx-1]<=opt[idx]:
        chosen_tasks.append(tasks[idx])
        idx = cached_nearest[idx]
    else:
        idx -=1
print('Chosen tasks are:',chosen_tasks[::-1])