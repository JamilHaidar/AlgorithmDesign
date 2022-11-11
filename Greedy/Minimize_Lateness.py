# schedule all jobs to minimize maximum lateness
# jobs = [(time_needed,due time),...]
jobs = [(3,6),(2,8),(1,9),(4,9),(3,14),(2,15)]
jobs = sorted(jobs,key=lambda x:x[1])
final_jobs = [(0,jobs[0][0])]
max_lateness = 0
lateness_explanation = 'no lateness'
for i,job in enumerate(jobs[1:]):
    final_jobs.append((final_jobs[-1][1],final_jobs[-1][1]+job[0]))
    lateness = max(0,final_jobs[-1][1]-job[1])
    if lateness>max_lateness:
        max_lateness = lateness
        lateness_explanation = f'{max_lateness} lateness for job {i+2}: {job}\ndue (t={job[1]}), finished (t={final_jobs[-1][1]})'
print(final_jobs)
print(lateness_explanation)