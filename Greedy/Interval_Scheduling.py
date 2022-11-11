# find maximum subset of mutually compatible jobs.
iterative = False # set to True for step by step
# jobs = [(start_time,finish_time),...]
jobs = [(0,6),(1,4),(3,5),(3,8),(4,7),(5,9),(6,10),(8,11)]
jobs = sorted(jobs,key=lambda x: x[1])

max_subset = [jobs[0]]
if iterative:
    print('Sorted jobs by finish time:',jobs)
    print(f'Inserted {jobs[0]}')
for job in jobs[1:]:
    success = False
    if job[0]>=max_subset[-1][1]:
        max_subset.append(job)
        success = True
    if iterative:
        print(f'Considering {job}')
        _ = input()
        print('Updated subset:',max_subset)
print('\nFinal set:',max_subset)